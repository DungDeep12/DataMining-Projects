import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('modified_test.csv')

# Preprocess the data
# Encode categorical variables
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Split the data into features and target
X = df.drop('satisfaction', axis=1)
y = df['satisfaction']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


# Function to preprocess new data
def preprocess_new_data(new_data, label_encoders):
    for column in new_data.select_dtypes(include=['object']).columns:
        if column in label_encoders:
            new_data[column] = label_encoders[column].transform(new_data[column])
    return new_data

# Example new data
new_data = pd.DataFrame({
    'Gender': ['Female'],
    'Customer Type': ['Loyal Customer'],
    'Age': [43],
    'Type of Travel': ['Personal Travel'],
    'Class': ['Eco'],
    'Flight Distance': [1927],
    'Inflight wifi service': [3],
    'Departure/Arrival time convenient': [4],
    'Ease of Online booking': [3],
    'Gate location': [1],
    'Food and drink': [4],
    'Online boarding': [4],
    'Seat comfort': [5],
    'Inflight entertainment': [5],
    'On-board service': [5],
    'Leg room service': [3],
    'Baggage handling': [5],
    'Checkin service': [4],
    'Inflight service': [5],
    'Cleanliness': [3],
    'Departure Delay in Minutes': [0],
    'Arrival Delay in Minutes': [0]
})

# Preprocess the new data
new_data = preprocess_new_data(new_data, label_encoders)

# Make predictions on the new data
new_predictions = model.predict(new_data)

new_predictions_labels = label_encoders['satisfaction'].inverse_transform(new_predictions)
print("Predictions for new data:", new_predictions_labels)

# data is input ny user
data = {
    'Gender': [input("Nhập Gender (Male/Female): ")],
    'Customer Type': [input("Nhập Customer Type (Loyal Customer/Disloyal Customer): ")],
    'Age': [int(input("Nhập Age: "))],
    'Type of Travel': [input("Nhập Type of Travel (Business travel/Personal Travel): ")],
    'Class': [input("Nhập Class (Eco/Eco Plus/Business): ")],
    'Flight Distance': [int(input("Nhập Flight Distance: "))],
    'Inflight wifi service': [int(input("Nhập Inflight wifi service (1-5): "))],
    'Departure/Arrival time convenient': [int(input("Nhập Departure/Arrival time convenient (1-5): "))],
    'Ease of Online booking': [int(input("Nhập Ease of Online booking (1-5): "))],
    'Gate location': [int(input("Nhập Gate location (1-5): "))],
    'Food and drink': [int(input("Nhập Food and drink (1-5): "))],
    'Online boarding': [int(input("Nhập Online boarding (1-5): "))],
    'Seat comfort': [int(input("Nhập Seat comfort (1-5): "))],
    'Inflight entertainment': [int(input("Nhập Inflight entertainment (1-5): "))],
    'On-board service': [int(input("Nhập On-board service (1-5): "))],
    'Leg room service': [int(input("Nhập Leg room service (1-5): "))],
    'Baggage handling': [int(input("Nhập Baggage handling (1-5): "))],
    'Checkin service': [int(input("Nhập Checkin service (1-5): "))],
    'Inflight service': [int(input("Nhập Inflight service (1-5): "))],
    'Cleanliness': [int(input("Nhập Cleanliness (1-5): "))],
    'Departure Delay in Minutes': [int(input("Nhập Departure Delay in Minutes: "))],
    'Arrival Delay in Minutes': [int(input("Nhập Arrival Delay in Minutes: "))],
}

# Tạo DataFrame từ dữ liệu đã nhập
new_data = pd.DataFrame(data)
# Preprocess the new data
new_data = preprocess_new_data(new_data, label_encoders)

# Make predictions on the new data
new_predictions = model.predict(new_data)

new_predictions_labels = label_encoders['satisfaction'].inverse_transform(new_predictions)
print("Predictions for new data:", new_predictions_labels)
