import pandas as pd

# Load the uploaded dataset to inspect its structure
file_path = 'train_processed.csv'
data = pd.read_csv(file_path)

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Copy the data for processing
data_cleaned = data.copy()

# Encode categorical features using Label Encoding for simplicity
label_encoders = {}
for col in data_cleaned.select_dtypes(include='object').columns:
    le = LabelEncoder()
    data_cleaned[col] = le.fit_transform(data_cleaned[col])
    label_encoders[col] = le

# Split into features (X) and target (y)
X = data_cleaned.drop(columns=['satisfaction'])
y = data_cleaned['satisfaction']

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn.decomposition import PCA
import numpy as np

# Apply PCA to reduce dimensions while retaining 95% of the variance
pca = PCA(n_components=0.95, random_state=42)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Check the number of components retained and the explained variance ratio
print(pca.n_components_, np.sum(pca.explained_variance_ratio_))

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Apply LDA for dimensionality reduction
lda = LinearDiscriminantAnalysis(n_components=1)  # 1 component for 2 classes
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# Print the shape of the transformed datasets
print("LDA Reduced Dimensions (Train):", X_train_lda.shape)
print("LDA Reduced Dimensions (Test):", X_test_lda.shape)