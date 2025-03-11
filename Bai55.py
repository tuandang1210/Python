import zipfile
import os


def compress_file(file_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=os.path.basename(file_path))
    print(f"Đã nén '{file_path}' thành '{zip_path}'.")


def decompress_file(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(path=extract_dir)
    print(f"Đã giải nén '{zip_path}' vào thư mục '{extract_dir}'.")

if __name__ == "__main__":
    action = input("Bạn muốn nén hay giải nén tệp? (n: nén, g: giải nén): ").lower()

    if action == "n":
        file_path = input("Nhập đường dẫn tệp cần nén: ").strip()
        zip_path = input("Nhập tên (đường dẫn) tệp zip sau khi nén (ví dụ: archive.zip): ").strip()
        if not os.path.isfile(file_path):
            print("Lỗi: Tệp cần nén không tồn tại!")
        else:
            compress_file(file_path, zip_path)

    elif action == "g":
        zip_path = input("Nhập đường dẫn tệp zip cần giải nén: ").strip()
        extract_dir = input("Nhập thư mục đích để giải nén: ").strip()
        if not os.path.isdir(extract_dir):
            os.makedirs(extract_dir)
        if not os.path.isfile(zip_path):
            print("Lỗi: Tệp zip không tồn tại!")
        else:
            decompress_file(zip_path, extract_dir)

    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn 'n' để nén hoặc 'g' để giải nén.")
