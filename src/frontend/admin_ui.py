import tkinter as tk
from tkinter import messagebox, ttk
from backend.account_manager import AccountManager

class AdminUI:
    def __init__(self, root):
        self.account_manager = AccountManager()
        self.root = root

        # 主容器
        self.container = tk.Frame(root, padx=20, pady=20, bg="#f9f9f9")
        self.container.grid(sticky="nsew")

        # 自适应布局
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(6, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

        # 标题
        self.title_label = tk.Label(self.container, text="管理员界面", 
                                    font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#333")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="n")

        # ⭕ 新用户输入区域封装
        user_frame = tk.Frame(self.container, bg="#f9f9f9")
        user_frame.grid(row=1, column=0, columnspan=2, pady=10)

        # 新邮箱输入
        self.email_label = tk.Label(user_frame, text="新的邮箱:", font=("Arial", 12), bg="#f9f9f9")
        self.email_label.pack(side="left", padx=5)

        self.email_entry = tk.Entry(user_frame, font=("Arial", 11), width=30)
        self.email_entry.pack(side="left", padx=5)

        # ⭕ 角色选择区域封装
        role_frame = tk.Frame(self.container, bg="#f9f9f9")
        role_frame.grid(row=2, column=0, columnspan=2, pady=5)

        self.role_label = tk.Label(role_frame, text="角色选择:", font=("Arial", 12), bg="#f9f9f9")
        self.role_label.pack(side="left", padx=5)

        self.role_combobox = ttk.Combobox(role_frame, values=["user", "admin"], font=("Arial", 11), width=28)
        self.role_combobox.set("user")  # 默认选择普通用户
        self.role_combobox.pack(side="left", padx=5)

        # 添加用户按钮
        self.add_button = tk.Button(self.container, text="添加用户", command=self.add_account,
                                    bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew", padx=20)

        # 分割线
        ttk.Separator(self.container, orient='horizontal').grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)

        # 用户列表标题
        self.user_list_label = tk.Label(self.container, text="用户列表:", font=("Arial", 12, "bold"), bg="#f9f9f9")
        self.user_list_label.grid(row=5, column=0, columnspan=2, sticky="w", padx=5)

        # ⭕ 用户列表 (可滚动)
        self.user_frame = tk.Frame(self.container)
        self.user_frame.grid(row=6, column=0, columnspan=2, sticky="nsew")

        self.user_listbox = tk.Listbox(self.user_frame, font=("Arial", 11))
        self.user_listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.user_frame, orient="vertical", command=self.user_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.user_listbox.config(yscrollcommand=self.scrollbar.set)

        # 删除用户按钮
        self.delete_button = tk.Button(self.container, text="删除选中的用户", command=self.delete_account,
                                       bg="#F44336", fg="white", font=("Arial", 11, "bold"))
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew", padx=20)

        # 初始加载用户列表
        self.load_accounts()

    def load_accounts(self):
        self.user_listbox.delete(0, tk.END)
        accounts = self.account_manager.load_accounts()
        for account in accounts:
            display_text = f"{account['email']} ({account['role']})"
            self.user_listbox.insert(tk.END, display_text)

    def add_account(self):
        email = self.email_entry.get().strip()
        role = self.role_combobox.get().strip().lower()

        if not email or role not in ["user", "admin"]:
            messagebox.showerror("错误", "请输入有效的邮箱地址，并选择 'user' 或 'admin' 身份。")
            return

        result = self.account_manager.add_account(email, role)
        messagebox.showinfo("添加用户", result)
        self.load_accounts()

    def delete_account(self):
        selected_index = self.user_listbox.curselection()
        if not selected_index:
            messagebox.showerror("错误", "请选择要删除的用户。")
            return

        selected_item = self.user_listbox.get(selected_index)
        email = selected_item.split(" (")[0]

        confirm = messagebox.askyesno("确认删除", f"确定要删除用户 {email} 吗？")
        if confirm:
            result = self.account_manager.delete_account(email)
            messagebox.showinfo("删除用户", result)
            self.load_accounts()
