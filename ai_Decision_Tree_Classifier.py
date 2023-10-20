import numpy as np


from random import shuffle

def add_zeros(foo):
  # adds preceeding zeros
  bar = foo[2:].zfill(12) # [2:] removes '0b' at the start. zfill usefully fills 8 chars with zeros
  
  return bar

def digify(my_list):
  
  # how to add to binary numbers (which python stores as strings)
  #c = bin(int(a,2) + int(b,2))

  foo = bin(my_list[1]*13+my_list[0]) # 2
  
  if( len(my_list) == 3 ):
    foo = bin(my_list[2]*26+my_list[1]*13+my_list[0]) # 

  if( len(my_list) == 4 ):
    foo = bin(my_list[3]*39+my_list[2]*26+my_list[1]*13+my_list[0]) # 

  if( len(my_list) == 5 ):
    foo = bin(my_list[2]*52+my_list[3]*39+my_list[2]*26+my_list[1]*13+my_list[0]) # 

    # maximum = 52*10 + 39 * 10 + 26 * 10 + 13 * 10 + 10 = 1310
    # = 10100011110, 11 digits

  return foo#bar


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
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Assuming your NumPy array is named 'data' and you have labels for each state in 'labels'.
X_train, X_test, y_train, y_test = train_test_split(data_array, labels_array, test_size=0.2, random_state=42)


# Initialize and train a decision tree classifier (you can choose another model too).
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set.
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy.
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

#########

# testing the model

#print(X_test)

#print( [  10000100])
#quit()
# Assume you have a trained model 'clf' and new input data 'new_data_array'
new_data_array = np.array([ [  11100101]])

# Use the trained model to make predictions
new_predictions = clf.predict(new_data_array)

print(new_predictions)

# Interpret the predictions
for prediction in new_predictions:
    if prediction == 0:
        print("Stick")
    else:
        print("Twist")
        
        







