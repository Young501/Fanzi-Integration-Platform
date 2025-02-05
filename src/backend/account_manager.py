import json
import os

class AccountManager:
    def __init__(self, data_file='accounts.json'):
        self.data_file = data_file

        # 默认管理员账户
        self.default_accounts = {
            "accounts": [
                {"email": "3296937370@qq.com", "role": "admin"},
                {"email": "530933620@qq.com", "role": "admin"},
                {"email": "yangzechenau@gmail.com", "role": "admin"}
            ]
        }

        # 如果 accounts.json 不存在，自动创建并写入默认账户
        if not os.path.exists(self.data_file):
            self._create_default_accounts()

    def _create_default_accounts(self):
        """创建默认的 accounts.json 文件"""
        with open(self.data_file, 'w') as f:
            json.dump(self.default_accounts, f, indent=4)

    def load_accounts(self):
        with open(self.data_file, 'r') as f:
            return json.load(f)["accounts"]

    def save_accounts(self, accounts):
        with open(self.data_file, 'w') as f:
            json.dump({"accounts": accounts}, f, indent=4)

    def get_account_role(self, email):
        accounts = self.load_accounts()
        for account in accounts:
            if account["email"] == email:
                return account.get("role", "user")
        return None

    def add_account(self, email, role='user'):
        accounts = self.load_accounts()
        if any(account["email"] == email for account in accounts):
            return "Account already exists."

        accounts.append({"email": email, "role": role})
        self.save_accounts(accounts)
        return f"Account '{email}' added as '{role}'."

    def delete_account(self, email):
        accounts = self.load_accounts()
        updated_accounts = [account for account in accounts if account["email"] != email]

        if len(accounts) == len(updated_accounts):
            return "Account not found."

        self.save_accounts(updated_accounts)
        return f"Account '{email}' has been deleted."
