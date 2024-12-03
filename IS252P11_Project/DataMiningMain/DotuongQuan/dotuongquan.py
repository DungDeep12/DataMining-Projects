import pandas as pd
import numpy as np

# Đọc file CSV
file_path = 'train_processed.csv'  # Đường dẫn tới file CSV
df = pd.read_csv(file_path)

# Hiển thị các cột trong dataset
print("Các cột trong dataset:", df.columns)

# Chọn 2 thuộc tính để tính độ tương quan
thuoc_tinh_1 = input("Nhập tên thuộc tính 1: ")  # Tên của cột 1
thuoc_tinh_2 = input("Nhập tên thuộc tính 2: ")  # Tên của cột 2

# Tính độ tương quan
if thuoc_tinh_1 in df.columns and thuoc_tinh_2 in df.columns:
    correlation = df[thuoc_tinh_1].corr(df[thuoc_tinh_2])
    print(f"Độ tương quan giữa {thuoc_tinh_1} và {thuoc_tinh_2}: {correlation:.4f}")
else:
    print("Tên cột không tồn tại trong DataFrame!")
