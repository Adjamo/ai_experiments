import numpy as np

# Initialize lists to store data and labels
data = []
labels = []

count = 0

# Replace 'your_data_file.txt' and 'your_labels_file.txt' with your file names
with open('data.txt', 'r') as data_file:
    for data_line in data_file:
        data_line = data_line.strip()  # Remove leading/trailing whitespace

        #print("Data Line:", data_line)
        
        #count += 1
        #print('count: '+str(count))
        
        # Check if the data line is not empty
        if data_line:
            # Split the data line and convert to integers if needed
            data_point = [int(x) for x in data_line.split()]
            data.append(data_point)


# Replace 'your_data_file.txt' and 'your_labels_file.txt' with your file names
with open('labels.txt', 'r') as labels_file:
    for label_line in  labels_file:
        label_line = label_line.strip()  # Remove leading/trailing whitespace

        #print("Label Line:", label_line)
        
        #count += 1
        #print('count: '+str(count))
        
        # Check if the label line is not empty
        if label_line:
            data_point_2 = [int(x) for x in label_line.split()]
            # Add the corresponding label to the labels list
            labels.append(data_point_2)
            labels.append(data_point_2)

# Convert data and labels to NumPy arrays
data_array = np.array(data)
labels_array = np.array(labels)

#print(data_array)
#print(labels_array)

print(len(data_array))  # Should be 148
print(len(labels_array))  # Should be 148

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data_array, labels_array, test_size=0.2, random_state=42)

# Initialize and train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

