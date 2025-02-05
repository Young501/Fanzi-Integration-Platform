import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from backend.archive_handler import ArchiveHandler

class ArchiveUI:
    def __init__(self, root):
        self.archive_handler = ArchiveHandler()
        self.root = root

        # 主容器
        self.container = tk.Frame(root, padx=20, pady=20, bg="#f9f9f9")
        self.container.grid(sticky="nsew")

        # 设置网格扩展性
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(4, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

        # 标题
        self.title_label = tk.Label(self.container, text="压缩包解压处理", 
                                    font=("Arial", 16, "bold"), bg="#f9f9f9")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky="n")

        # 选择压缩文件
        self.target_label = tk.Label(self.container, text="选择压缩包文件(RAR/ZIP):", font=("Arial", 12), bg="#f9f9f9")
        self.target_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.target_entry = tk.Entry(self.container, font=("Arial", 11))
        self.target_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.target_button = tk.Button(self.container, text="浏览", command=self.browse_target,
                                       bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.target_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        # 分割线
        ttk.Separator(self.container, orient='horizontal').grid(row=2, column=0, columnspan=3, sticky="ew", pady=10)

        # 选择目标文件夹
        self.source_label = tk.Label(self.container, text="选择目标文件夹目录:", font=("Arial", 12), bg="#f9f9f9")
        self.source_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)

        self.source_entry = tk.Entry(self.container, font=("Arial", 11))
        self.source_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.source_button = tk.Button(self.container, text="浏览", command=self.browse_source,
                                       bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.source_button.grid(row=3, column=2, padx=5, pady=5, sticky="ew")

        # 提取按钮
        self.extract_button = tk.Button(self.container, text="解压处理", command=self.extract_archive,
                                        bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.extract_button.grid(row=4, column=0, columnspan=3, pady=10, sticky="ew", padx=20)

        # 输出框
        self.output_text = tk.Text(self.container, height=10, font=("Arial", 10))
        self.output_text.grid(row=5, column=0, columnspan=3, sticky="nsew", pady=5)

    def browse_target(self):
        target_path = filedialog.askopenfilename(filetypes=[("Archive files", "*.rar *.zip")])
        self.target_entry.delete(0, tk.END)
        self.target_entry.insert(0, target_path)

    def browse_source(self):
        source_path = filedialog.askdirectory()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, source_path)

    def extract_archive(self):
        target = self.target_entry.get()
        source = self.source_entry.get()

        if not target or not source:
            messagebox.showerror("Error", "Please select both the archive file and the destination folder.")
            return

        def update_ui(message):
            self.output_text.insert(tk.END, f"{message}\n")
            self.output_text.see(tk.END)

        message = self.archive_handler.extract_archive(target, source, ui_callback=update_ui)
        self.output_text.insert(tk.END, f"{message}\n")
