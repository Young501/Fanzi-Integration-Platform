# 🚀 Fanzi Integration Platform

## 📦 Overview

**Fanzi Integration Platform** is a custom-built application designed specifically for **Fanzi Company** to streamline and manage critical business operations efficiently. The platform focuses on file management, user account administration, and secure access control, providing a comprehensive solution tailored to Fanzi's unique business requirements.

---

## 🌟 Key Features

### 📁 **Archive Extraction**
- Supports extraction of **RAR** and **ZIP** files.
- Automatically organizes extracted files based on company names.
- Renames files intelligently based on specified patterns (e.g., converting "2023年01账期" to "2023年01月").
- Ensures clean file management by removing temporary files after processing.

### 👥 **User Management System**
- Secure login using **email-based verification codes**.
- Distinction between **Admin** and **User** roles:
  - **Admins** can add or delete user accounts and manage system settings.
  - **Users** have access to core file processing features.
- Role-based access control ensures data security.

### 🔐 **Account Initialization**
- Since we do not have a database service, we need to manually create an `accounts.json` file on the first run.
- Default admin accounts are pre-configured:
  - `3296937370@qq.com` (Admin)
  - `530933620@qq.com` (Admin)
  - `yangzechenau@gmail.com` (Admin)

### 📊 **Intuitive User Interface**
- Clean and user-friendly interface designed with **Tkinter**.
- Responsive layout that adjusts dynamically to different screen sizes.
- Tab-based navigation for easy access to different modules.

---

## ⚙️ **How to Use**

1. **Download the Application:**
   - Extract the provided `.zip` file if applicable.

2. **Run the Program:**
   - Double-click `FanziApp.exe` to launch the application.
   - No additional installations are required.

3. **Login Process:**
   - Enter your email address and request a verification code.
   - Enter the received code to log in.

4. **Archive Extraction:**
   - Select an archive file (RAR/ZIP) and choose a destination folder.
   - Click "Extract Archive" to process the file.

5. **Admin Panel (For Admin Users):**
   - Add new user accounts or admins.
   - Delete existing accounts if necessary.

---

## 🔒 **Security & Data Handling**

- All user account data is securely stored in `accounts.json`.
- Verification codes are sent directly to registered email addresses for secure login.
- Role-based access ensures sensitive features are restricted to authorized users only.

---

## 💼 **About the Project**

This platform was developed as a **custom business solution for Fanzi Company**, aiming to optimize file handling workflows and improve internal data management. It integrates seamlessly with Fanzi's existing business processes while offering scalability for future enhancements.

---

## 📧 **Contact**

For support or inquiries, please contact:

- **Developer:** Zechen Yang  
- **Email:** yangzechenau@gmail.com  
- **Company:** Fanzi  

---

## ✅ **Version**

**Fanzi Integration Platform v1.0**

---
