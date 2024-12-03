import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import graphviz

# Load the data
data = pd.read_csv('train_processed.csv')

# Encode categorical variables
data_encoded = pd.get_dummies(data, columns=['Gender', 'Customer Type', 'Type of Travel', 'Class'])

# Separate features and target variable
X = data_encoded.drop('satisfaction', axis=1)
y = data_encoded['satisfaction'].apply(lambda x: 1 if x == 'satisfied' else 0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Plot the decision tree
plt.figure(figsize=(20,10))
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=['neutral or dissatisfied', 'satisfied'])
plt.show()

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=X.columns,
                                class_names=['neutral or dissatisfied', 'satisfied'],
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree")