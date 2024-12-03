import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  # Thay số 4 bằng số lõi vật lý của máy bạn.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load and Inspect Data

# Load the dataset from the CSV file
data = pd.read_csv('modified_test.csv')

# Inspect the first few rows of the dataset
data.head()

# Preprocess Data
# Handle missing values by filling them with the mean of the column
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Departure Delay in Minutes'] = data['Departure Delay in Minutes'].fillna(data['Departure Delay in Minutes'].mean())
data['Arrival Delay in Minutes'] = data['Arrival Delay in Minutes'].fillna(data['Arrival Delay in Minutes'].mean())


# Extract the relevant columns
columns_of_interest = ['Departure Delay in Minutes', 'Arrival Delay in Minutes']
data_subset = data[columns_of_interest]

# Normalize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data_subset)

# Convert the normalized data back to a DataFrame
data_normalized = pd.DataFrame(data_normalized, columns=columns_of_interest)

# Display the first few rows of the preprocessed data
data_normalized.head()

# Determine the optimal number of clusters using the elbow method
inertia = []
for n in range(1, 11):
    kmeans = KMeans(n_clusters=n, random_state=42)
    kmeans.fit(data_normalized)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()


# Silhouette method to determine the optimal K
try:
    silhouette_scores = []
    k_range = range(2, 11)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data_normalized)
        score = silhouette_score(data_normalized, kmeans.labels_)
        silhouette_scores.append(score)

    plt.figure(figsize=(8, 4))
    plt.plot(k_range, silhouette_scores, marker='o')
    plt.title('Silhouette Score Method')
    plt.xlabel('Number of clusters (K)')
    plt.ylabel('Silhouette Score')
    plt.show()
except Exception as e:
    print(f"Lỗi xảy ra: {e}")


# Apply K-means Clustering

optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
data_normalized['Cluster'] = kmeans.fit_predict(data_normalized)

# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(data_normalized['Departure Delay in Minutes'],
            data_normalized['Arrival Delay in Minutes'],
            c=data_normalized['Cluster'], cmap='viridis')
plt.title('K-means Clustering')
plt.xlabel('Departure Delay in Minutes')
plt.ylabel('Arrival Delay in Minutes')
plt.colorbar(label='Cluster')
plt.show()

# Reduce Noise Using Cluster Centroids

# Calculate the cluster centroids
centroids = kmeans.cluster_centers_

# Replace the original data points with their corresponding cluster centroids
data_reduced_noise = data_normalized.copy()
for i in range(optimal_clusters):
    data_reduced_noise.loc[data_reduced_noise['Cluster'] == i, columns_of_interest] = centroids[i]

# Drop the 'Cluster' column as it's no longer needed
data_reduced_noise.drop(columns=['Cluster'], inplace=True)

# Convert the reduced noise data back to the original scale
data_reduced_noise = scaler.inverse_transform(data_reduced_noise)
data_reduced_noise = pd.DataFrame(data_reduced_noise, columns=columns_of_interest)

# Display the first few rows of the reduced noise data
data_reduced_noise.head()

# Visualize the reduced noise data
plt.figure(figsize=(10, 6))
plt.scatter(data_reduced_noise['Departure Delay in Minutes'],
            data_reduced_noise['Arrival Delay in Minutes'],
            c=kmeans.labels_, cmap='viridis')
plt.title('Reduced Noise Data Using Cluster Centroids')
plt.xlabel('Departure Delay in Minutes')
plt.ylabel('Arrival Delay in Minutes')
plt.colorbar(label='Cluster')
plt.show()

# Visualize Results

# Create scatter plots to compare the original data with the noise-reduced data

# Scatter plot for original data
plt.figure(figsize=(10, 6))
plt.scatter(data['Departure Delay in Minutes'], data['Arrival Delay in Minutes'], alpha=0.5, label='Original Data')
plt.title('Original Data: Departure Delay vs Arrival Delay')
plt.xlabel('Departure Delay in Minutes')
plt.ylabel('Arrival Delay in Minutes')
plt.legend()
plt.show()

# Scatter plot for noise-reduced data
plt.figure(figsize=(10, 6))
plt.scatter(data_reduced_noise['Departure Delay in Minutes'], data_reduced_noise['Arrival Delay in Minutes'],
            alpha=0.5, label='Noise-Reduced Data', c=kmeans.labels_, cmap='viridis')
plt.title('Noise-Reduced Data: Departure Delay vs Arrival Delay')
plt.xlabel('Departure Delay in Minutes')
plt.ylabel('Arrival Delay in Minutes')
plt.colorbar(label='Cluster')
plt.legend()
plt.show()

