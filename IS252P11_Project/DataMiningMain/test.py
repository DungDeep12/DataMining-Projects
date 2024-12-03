import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


# Hàm đọc file CSV
def load_file():
    global df
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        try:
            df = pd.read_csv(filepath)
            messagebox.showinfo("Thành công", "Đã tải dữ liệu thành công!")
            display_columns()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc file: {e}")


# Hiển thị danh sách cột để người dùng chọn
def display_columns():
    columns = list(df.columns)
    col1_combo['values'] = columns
    col2_combo['values'] = columns
    messagebox.showinfo("Thông báo", "Hãy chọn các cột để tính toán hoặc áp dụng giải thuật!")


# Hàm tính độ tương quan
def calculate_correlation():
    col1 = col1_combo.get()
    col2 = col2_combo.get()
    if col1 and col2 and col1 in df.columns and col2 in df.columns:
        correlation = df[col1].corr(df[col2])
        messagebox.showinfo("Kết quả", f"Độ tương quan giữa {col1} và {col2}: {correlation:.2f}")
    else:
        messagebox.showerror("Lỗi", "Hãy chọn các cột hợp lệ!")


# Hàm áp dụng thuật toán Apriori và tìm luật kết hợp
def apply_apriori():
    try:
        # Đọc các cột đánh giá từ người dùng
        rating_columns = rating_columns_entry.get().split(",")
        if not all(col.strip() in df.columns for col in rating_columns):
            messagebox.showerror("Lỗi", "Một hoặc nhiều cột không tồn tại trong dữ liệu!")
            return

        # Tạo danh sách giao dịch từ các cột đánh giá
        transactions = []
        for _, row in df.iterrows():
            items = []
            for col in rating_columns:
                score = row[col.strip()]
                if score >= 4:
                    items.append(f"{col.strip()}_good")
                elif score <= 2:
                    items.append(f"{col.strip()}_bad")
            transactions.append(items)

        # Mã hóa giao dịch và áp dụng Apriori
        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        transaction_df = pd.DataFrame(te_ary, columns=te.columns_)

        # Lấy tham số min_support và min_confidence từ người dùng
        min_support = float(min_support_entry.get())
        min_confidence = float(min_confidence_entry.get())

        # Áp dụng thuật toán Apriori
        frequent_itemsets = apriori(transaction_df, min_support=min_support, use_colnames=True)

        # Tìm các luật kết hợp
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence, num_itemsets=len(frequent_itemsets))

        # Hiển thị kết quả
        result_window = tk.Toplevel(root)
        result_window.title("Kết quả Apriori và luật kết hợp")
        text = tk.Text(result_window, wrap="word")

        if rules.empty:
            text.insert("1.0", "Không tìm thấy luật kết hợp nào với các tham số đã cho.")
        else:
            text.insert("1.0", rules.to_string(index=False))

        text.pack(expand=True, fill="both")
        result_window.mainloop()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")


# Giao diện chính
root = tk.Tk()
root.title("Phân tích dữ liệu")
root.geometry("800x600")

# Menu bên phải
menu_frame = tk.Frame(root, width=200, bg="lightblue")
menu_frame.pack(side="right", fill="y")

# Menu tiêu đề
menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 16, "bold"), bg="lightblue")
menu_label.pack(pady=20)

# Nút tải dữ liệu
load_button = tk.Button(menu_frame, text="Tải dữ liệu CSV", command=load_file, bg="white")
load_button.pack(pady=10, fill="x")

# Tính độ tương quan
correlation_label = tk.Label(menu_frame, text="Tính độ tương quan", bg="lightblue", font=("Arial", 12, "bold"))
correlation_label.pack(pady=10)

col1_combo = ttk.Combobox(menu_frame)
col1_combo.pack(pady=5)
col1_combo.set("Chọn cột 1")

col2_combo = ttk.Combobox(menu_frame)
col2_combo.pack(pady=5)
col2_combo.set("Chọn cột 2")

correlation_button = tk.Button(menu_frame, text="Tính độ tương quan", command=calculate_correlation, bg="white")
correlation_button.pack(pady=10, fill="x")

# Giải thuật Apriori
apriori_label = tk.Label(menu_frame, text="Giải thuật Apriori", bg="lightblue", font=("Arial", 12, "bold"))
apriori_label.pack(pady=10)

rating_columns_label = tk.Label(menu_frame, text="Nhập cột đánh giá (cách nhau bằng dấu phẩy):", bg="lightblue")
rating_columns_label.pack(pady=5)

rating_columns_entry = tk.Entry(menu_frame)
rating_columns_entry.pack(pady=5)
rating_columns_entry.insert(0, "Inflight wifi service,Seat comfort")

min_support_label = tk.Label(menu_frame, text="Nhập min_support:", bg="lightblue")
min_support_label.pack(pady=5)

min_support_entry = tk.Entry(menu_frame)
min_support_entry.pack(pady=5)
min_support_entry.insert(0, "0.05")

min_confidence_label = tk.Label(menu_frame, text="Nhập min_confidence:", bg="lightblue")
min_confidence_label.pack(pady=5)

min_confidence_entry = tk.Entry(menu_frame)
min_confidence_entry.pack(pady=5)
min_confidence_entry.insert(0, "0.5")

apriori_button = tk.Button(menu_frame, text="Áp dụng Apriori", command=apply_apriori, bg="white")
apriori_button.pack(pady=10, fill="x")


# Vùng chính để hiển thị thông tin
main_frame = tk.Frame(root, bg="white")
main_frame.pack(side="left", expand=True, fill="both")

welcome_label = tk.Label(main_frame, text="Chào mừng đến ứng dụng phân tích dữ liệu!", font=("Arial", 16), bg="white")
welcome_label.pack(pady=20)

root.mainloop()
