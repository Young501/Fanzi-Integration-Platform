import os
import zipfile
import rarfile
import re
import shutil

class ArchiveHandler:
    @staticmethod
    def extract_archive(target, source, ui_callback=None):  # 确保这里有 ui_callback 参数
        temp_dir = os.path.join(source, "temp")
        os.makedirs(temp_dir, exist_ok=True)

        try:
            if target.endswith(".rar"):
                with rarfile.RarFile(target) as rf:
                    rf.extractall(temp_dir)
            elif target.endswith(".zip"):
                with zipfile.ZipFile(target, 'r') as zf:
                    zf.extractall(temp_dir)
            else:
                return "Unsupported file format. Only RAR and ZIP are supported."

            for item in os.listdir(temp_dir):
                sub_archive_path = os.path.join(temp_dir, item)
                company_name_match = re.match(r'(.+?)\d+', item)
                if company_name_match:
                    company_name = company_name_match.group(1)
                else:
                    continue

                sub_temp_dir = os.path.join(temp_dir, f"sub_{item}")
                os.makedirs(sub_temp_dir, exist_ok=True)

                if item.endswith(".rar"):
                    with rarfile.RarFile(sub_archive_path) as rf:
                        rf.extractall(sub_temp_dir)
                elif item.endswith(".zip"):
                    with zipfile.ZipFile(sub_archive_path, 'r') as zf:
                        zf.extractall(sub_temp_dir)

                target_folder = os.path.join(source, company_name)
                os.makedirs(target_folder, exist_ok=True)

                for root, _, files in os.walk(sub_temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        match = re.search(r'(\d{4})年(\d{1,2})账期(.*)', file)
                        if match:
                            new_file_name = f"{match.group(1)}年{match.group(2)}月{match.group(3)}"
                            new_file_path = os.path.join(target_folder, new_file_name)
                            shutil.move(file_path, new_file_path)

                            if ui_callback:  # 调用 UI 回调以更新进度
                                ui_callback(f"Processed file: {company_name}{new_file_name}")

            shutil.rmtree(temp_dir)
            return "Processing completed successfully."
        except Exception as e:
            shutil.rmtree(temp_dir, ignore_errors=True)
            return f"Failed to process archives: {str(e)}"