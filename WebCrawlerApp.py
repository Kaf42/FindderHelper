'''
使用tkinter实现GUI界面
'''

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import threading
import queue
import json
import os
import pyperclip
from functions import UrlSniffing


class WebCrawlerApp:
    def __init__(self, root):
        # 初始化主窗口
        self.root = root
        self.root.title("网页抓取工具")
        self.root.geometry("400x410")
        self.root.resizable(True, True)

        # 加载配置
        self.config = self.load_config()

        # 创建界面组件
        self.create_widgets()

        # 创建任务队列
        self.task_queue = queue.Queue()
        self.root.after(100, self.process_queue)

        # 状态跟踪
        self.crawling = False
        self.background_image = None

    def create_widgets(self):
        # ===== 顶部控制区域 =====
        control_frame = ttk.LabelFrame(self.root, text="网页抓取控制")
        control_frame.pack(fill=tk.X, padx=10, pady=10, ipadx=5, ipady=5)

        # 网址输入框
        url_frame = ttk.Frame(control_frame)
        url_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(url_frame, text="目标网址:").pack(side=tk.LEFT)
        self.url_entry = ttk.Entry(url_frame, width=60)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # 按钮区域
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(btn_frame, text="开始抓取", command=self.start_crawl).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="复制结果", command=self.copy_results).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="重置结果", command=self.reset_results).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="配置设置", command=self.open_settings).pack(side=tk.LEFT, padx=2)

        # ===== 结果表格区域 =====
        result_frame = ttk.LabelFrame(self.root, text="抓取结果")
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10), ipadx=5, ipady=5)

        # 创建表格
        # self.tree = ttk.Treeview(result_frame, columns=("URL", "Type", "Status"), show="headings")
        self.tree = ttk.Treeview(result_frame, columns=("URL", "Status"), show="headings")
        self.tree.heading("URL", text="网址")
        # self.tree.heading("Type", text="类型")
        self.tree.heading("Status", text="状态")
        self.tree.column("URL", width=280, anchor=tk.W)
        # self.tree.column("Type", width=150, anchor=tk.CENTER)
        self.tree.column("Status", width=50, anchor=tk.CENTER)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # ===== 状态栏 =====
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_config(self):
        """加载配置文件"""
        config_path = "web_crawler_config.json"
        default_config = {
            "chrome_path": r"D:\chrome-win64\chrome.exe",
            "driver_path": r"D:\chrome-win64\chromedriver.exe"
        }

        try:
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    return json.load(f)
        except:
            pass

        return default_config

    def save_config(self):
        """保存配置到文件"""
        with open("web_crawler_config.json", 'w') as f:
            json.dump(self.config, f)

    def start_crawl(self):
        """开始抓取操作（线程安全）[5,6](@ref)"""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("错误", "请输入有效的网址")
            return

        if self.crawling:
            messagebox.showwarning("警告", "当前已有抓取任务正在进行")
            return

        # 更新状态
        self.status_var.set("抓取中...")
        self.crawling = True

        # 启动后台线程执行耗时操作
        threading.Thread(
            target=self.execute_crawl,
            args=(url,),
            daemon=True
        ).start()

    def execute_crawl(self, url):
        """实际执行抓取的函数（在后台线程运行）"""
        try:
            if self.config["chrome_path"] == None or self.config["chrome_path"] == "":
                self.task_queue.put(("update_status", "处理失败"))
                self.task_queue.put(("show_error", f"抓取失败: 未配置chrome路径"))
                return
            if self.config["driver_path"] == None or self.config["driver_path"] == "":
                self.task_queue.put(("update_status", "处理失败"))
                self.task_queue.put(("show_error", f"抓取失败: 未配置driver路径"))
                return

            # 开始抓取
            urls = UrlSniffing(url, self.config["chrome_path"],self.config["driver_path"])
            results = [(url, '200') for url in urls.split('\n')]

            # 将结果添加到队列
            self.task_queue.put(("update_results", results))
            self.task_queue.put(("update_status", "处理完成"))
            self.task_queue.put(("show_completion",))

        except Exception as e:
            self.task_queue.put(("show_error", f"抓取失败: {str(e)}"))
        finally:
            self.crawling = False

    def process_queue(self):
        """处理任务队列（主线程安全）[6,7](@ref)"""
        try:
            while not self.task_queue.empty():
                task_type, *args = self.task_queue.get_nowait()

                if task_type == "update_results":
                    self.update_results(args[0])
                elif task_type == "show_error":
                    messagebox.showerror("错误", args[0])
                elif task_type == "update_status":
                    self.status_var.set(args[0])
                elif task_type == "show_completion":
                    messagebox.showinfo("完成", "抓取完成")

        except queue.Empty:
            pass

        self.root.after(100, self.process_queue)

    def update_results(self, results):
        """更新结果表格"""
        self.reset_results()
        for result in results:
            self.tree.insert("", tk.END, values=result)

    def reset_results(self):
        """重置结果表格"""
        for item in self.tree.get_children():
            self.tree.delete(item)

    def copy_results(self):
        """复制结果到剪切板"""
        results = []
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            results.append(values[0])

        if results:
            pyperclip.copy("\n".join(results))
            messagebox.showinfo("成功", "结果已复制到剪切板")
        else:
            messagebox.showwarning("警告", "没有可复制的结果")

    def open_settings(self):
        """打开配置窗口"""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("配置设置")
        settings_win.geometry("600x160")
        settings_win.transient(self.root)
        settings_win.grab_set()

        # Chrome位置
        chrome_frame = ttk.Frame(settings_win)
        chrome_frame.pack(fill=tk.X, padx=10, pady=10)
        ttk.Label(chrome_frame, text="Chrome位置:").pack(side=tk.LEFT)
        self.chrome_path_var = tk.StringVar(value=self.config["chrome_path"])
        chrome_entry = ttk.Entry(chrome_frame, textvariable=self.chrome_path_var, width=50)
        chrome_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(chrome_frame, text="浏览...",
                   command=lambda: self.browse_file(chrome_entry)).pack(side=tk.LEFT)

        # ChromeDriver位置
        driver_frame = ttk.Frame(settings_win)
        driver_frame.pack(fill=tk.X, padx=10, pady=10)
        ttk.Label(driver_frame, text="ChromeDriver位置:").pack(side=tk.LEFT)
        self.driver_path_var = tk.StringVar(value=self.config["driver_path"])
        driver_entry = ttk.Entry(driver_frame, textvariable=self.driver_path_var, width=50)
        driver_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(driver_frame, text="浏览...",
                   command=lambda: self.browse_file(driver_entry)).pack(side=tk.LEFT)

        # 按钮区域
        btn_frame = ttk.Frame(settings_win)
        btn_frame.pack(fill=tk.X, padx=10, pady=20)
        ttk.Button(btn_frame, text="保存",
                   command=lambda: self.save_settings(settings_win)).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="取消",
                   command=settings_win.destroy).pack(side=tk.RIGHT)

    def browse_file(self, entry_widget):
        """浏览文件选择对话框"""
        file_path = filedialog.askopenfilename(
            title="选择文件",
            filetypes=[("可执行文件", "*.exe"), ("所有文件", "*.*")]
        )
        if file_path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, file_path)

    def save_settings(self, settings_win):
        """保存配置设置"""
        self.config["chrome_path"] = self.chrome_path_var.get()
        self.config["driver_path"] = self.driver_path_var.get()
        self.save_config()
        settings_win.destroy()
        messagebox.showinfo("成功", "配置已保存")


if __name__ == "__main__":
    root = tk.Tk()
    app = WebCrawlerApp(root)
    root.mainloop()