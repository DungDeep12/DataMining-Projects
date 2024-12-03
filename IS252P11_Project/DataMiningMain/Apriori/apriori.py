import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc file CSV để kiểm tra nội dung dữ liệu
file_path = 'train_processed.csv'
data = pd.read_csv(file_path)

# Hiển thị thông tin cơ bản về dữ liệu
data.info(), data.head()

# List of service columns
service_columns = [
    'Inflight wifi service', 'Departure/Arrival time convenient',
    'Ease of Online booking', 'Gate location', 'Food and drink',
    'Online boarding', 'Seat comfort', 'Inflight entertainment',
    'On-board service', 'Leg room service', 'Baggage handling',
    'Checkin service', 'Inflight service', 'Cleanliness'
]

# Chuyển đổi các cột dịch vụ sang giá trị nhị phân (True/False)
# Điểm >= 4 là True (hài lòng), điểm < 3 là False (không hài lòng)
df_binary = pd.DataFrame()
for col in service_columns:
    df_binary[f'{col}_high'] = (data[col] >= 4)
df_binary['satisfied'] = (data['satisfaction'] == 'satisfied')

# sử dụng thuật toán Apriori
frequent_itemsets = apriori(df_binary, min_support=0.3, use_colnames=True)

# Trích xuất các luật kết hợp từ các tập mục thường xuyên
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.4, num_itemsets=len(frequent_itemsets))
rules = rules[rules['consequents'] == frozenset({'satisfied'})]

# Hiển thị các tập mục thường xuyên và một số luật kết hợp
print('Tap pho bien:')
print(frequent_itemsets.head())

print('Luat ket hop:')
print(rules)
