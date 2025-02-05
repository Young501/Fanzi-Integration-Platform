import sys
import os
import tkinter as tk
from tkinter import ttk

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from frontend.archive_ui import ArchiveUI
from frontend.login_ui import LoginUI
from frontend.admin_ui import AdminUI

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("小范的整合平台 v1.0")


        self.login_frame = tk.Frame(root)
        self.main_frame = tk.Frame(root)

        # 初始化 Login UI，登录成功后切换到主页面
        self.login_ui = LoginUI(self.login_frame, self.show_main_frame)
        self.login_frame.pack(expand=1, fill='both')

    def show_main_frame(self, email, role):
        self.login_frame.pack_forget()    # 隐藏登录界面
        self.main_frame.pack(expand=1, fill='both')  # 显示主界面

        tab_control = ttk.Notebook(self.main_frame)
        archive_tab = tk.Frame(tab_control)
        tab_control.add(archive_tab, text='压缩包处理')
        ArchiveUI(archive_tab)

        # 只有管理员才能看到 User Management 页面
        if role == "admin":
            admin_tab = tk.Frame(tab_control)

            tab_control.add(admin_tab, text='管理员界面')

            AdminUI(admin_tab)

        tab_control.pack(expand=1, fill='both')

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
