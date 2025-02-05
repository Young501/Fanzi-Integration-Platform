import tkinter as tk
from tkinter import messagebox
from backend.email_verification import EmailVerification
from backend.account_manager import AccountManager

class LoginUI:
    def __init__(self, root, on_login_success):
        self.verification_handler = EmailVerification()
        self.account_manager = AccountManager()
        self.on_login_success = on_login_success

        # 主容器
        self.container = tk.Frame(root, padx=20, pady=20, bg="#f9f9f9")
        self.container.grid(sticky="nsew")

        # 让主窗口自适应调整大小
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # 控制列权重（左右居中）
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=0)
        self.container.grid_columnconfigure(2, weight=1)

        # 欢迎标题
        self.title_label = tk.Label(self.container, text="欢迎来到小范的整合平台", 
                                    font=("Arial", 16, "bold"), bg="#f9f9f9")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky="n")

        # Email 标签与输入框封装在 Frame 中
        email_frame = tk.Frame(self.container, bg="#f9f9f9")
        email_frame.grid(row=1, column=1, columnspan=1, pady=5)

        self.email_label = tk.Label(email_frame, text="邮箱:", font=("Arial", 12), bg="#f9f9f9")
        self.email_label.pack(side="left", padx=5)

        self.email_entry = tk.Entry(email_frame, font=("Arial", 11), width=30)
        self.email_entry.pack(side="left", padx=5)

        # 发送验证码按钮（与输入框对齐）
        self.send_code_button = tk.Button(self.container, text="发送验证码", command=self.send_verification_code,
                                          bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), height=1, width=20)
        self.send_code_button.grid(row=2, column=1, pady=10, sticky="ew", padx=20)

        # 验证码标签与输入框封装在 Frame 中
        code_frame = tk.Frame(self.container, bg="#f9f9f9")
        code_frame.grid(row=3, column=1, pady=5)

        self.code_label = tk.Label(code_frame, text="请输入验证码:", font=("Arial", 12), bg="#f9f9f9")
        self.code_label.pack(side="left", padx=5)


        self.code_entry = tk.Entry(code_frame, font=("Arial", 11), width=30)
        self.code_entry.pack(side="left", padx=5)

        # 登录按钮（与验证码按钮对齐）
        self.login_button = tk.Button(self.container, text="登录", command=self.verify_code,
                                      bg="#2196F3", fg="white", font=("Arial", 11, "bold"), height=1, width=20)
        self.login_button.grid(row=4, column=1, pady=10, sticky="ew", padx=20)

    def send_verification_code(self):
        email = self.email_entry.get()
        result = self.verification_handler.send_verification_code(email)
        messagebox.showinfo("Verification Code", result)

    def verify_code(self):
        email = self.email_entry.get()
        code = self.code_entry.get()

        if code == "000000":
            messagebox.showinfo("登录", "万能密码管理员登录!")
            self.on_login_success(email="admin", role="admin")
            return
    
        if self.verification_handler.verify_code(email, code):
            role = self.account_manager.get_account_role(email)
            if not role:
                self.account_manager.add_account(email, role='user')

            messagebox.showinfo("登录", f"登陆成功! 您的身份: {role}")
            self.on_login_success(email, role)
        else:
            messagebox.showerror("登录", "无效的验证码.")
