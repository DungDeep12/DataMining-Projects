import pandas as pd

# 1. Đọc file CSV
file_path = "train.csv"
df = pd.read_csv(file_path)

# 2. Kiểm tra thông tin cơ bản của dữ liệu
print("Thông tin dữ liệu:")
print(df.info())
print("\nNhững dòng đầu tiên của dữ liệu:")
print(df.head())
print("\nKiểm tra các giá trị null:")
print(df.isnull().sum())

# 3. Xử lý các giá trị null
# Bạn có thể chọn loại bỏ hoặc điền các giá trị null, tùy thuộc vào nhu cầu
df = df.dropna()  # Loại bỏ các dòng chứa giá trị null
# Hoặc bạn có thể điền giá trị trung bình/median cho các cột dạng số
# df.fillna(df.mean(), inplace=True)

# 4. Kiểm tra và loại bỏ các giá trị trùng lặp
print("\nSố lượng dòng trùng lặp trước khi xóa:", df.duplicated().sum())
df = df.drop_duplicates()

# 5. Xóa 2 cột đầu tiên
df = df.iloc[:, 2:]

# 6. Kiểm tra dữ liệu sau khi tiền xử lý
print("\nThông tin dữ liệu sau khi xử lý:")
print(df.info())

# 7. Lưu lại file CSV sau khi đã xử lý
df.to_csv("train_processed.csv", index=False)
print("\nDữ liệu đã được lưu vào file train_processed.csv")
