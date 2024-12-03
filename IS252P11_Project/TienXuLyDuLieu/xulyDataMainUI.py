import streamlit as st
import pandas as pd

# 1. Tạo tiêu đề cho ứng dụng
st.title("Ứng dụng Tiền xử lý Dữ liệu CSV")

# 2. Upload file CSV
uploaded_file = st.file_uploader("Tải lên file CSV", type=["csv"])
if uploaded_file is not None:
    # Đọc file CSV
    df = pd.read_csv(uploaded_file)
    st.write("Thông tin dữ liệu ban đầu:")
    st.write(df.info())
    st.dataframe(df.head())

    # 3. Xử lý các giá trị null
    st.subheader("Xử lý các giá trị null")
    null_option = st.selectbox("Bạn muốn làm gì với các giá trị null?",
                               ["Không làm gì", "Xóa các dòng chứa giá trị null", "Điền giá trị trung bình"])

    if null_option == "Xóa các dòng chứa giá trị null":
        df = df.dropna()
        st.write("Đã xóa các dòng chứa giá trị null.")
    elif null_option == "Điền giá trị trung bình":
        df.fillna(df.mean(), inplace=True)
        st.write("Đã điền giá trị trung bình cho các cột số.")

    # 4. Loại bỏ các giá trị trùng lặp
    st.subheader("Loại bỏ các giá trị trùng lặp")
    if st.button("Xóa các dòng trùng lặp"):
        df = df.drop_duplicates()
        st.write("Đã xóa các dòng trùng lặp.")

    # 5. Xóa cột đầu tiên
    if st.checkbox("Xóa 2 cột đầu tiên (cột không có tên và cột ID)"):
        df = df.iloc[:, 2:]
        st.write("Đã xóa 2 cột đầu tiên.")

    # 6. Hiển thị thông tin sau khi tiền xử lý
    st.subheader("Thông tin dữ liệu sau khi xử lý:")
    st.write(df.info())
    st.dataframe(df.head())

    # 7. Tải file CSV đã xử lý
    st.subheader("Tải xuống file CSV đã xử lý")
    processed_file = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Tải xuống",
                       data=processed_file,
                       file_name="train_processed.csv",
                       mime="text/csv")
