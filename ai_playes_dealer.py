import numpy as np
import time

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


while True:

	time.sleep(1)
	suit = [i for i in range(10)]# goes up to 9 which is 10
	suit.append(9)#jack
	suit.append(9)#queen
	suit.append(9)#king

	# normalise the cards
	count = 0
	for x in suit:
		suit[count] += 1
		count += 1

	suit = [11 if x==1 else x for x in suit]# swap all 1s for 11

	cards = suit + suit + suit + suit
	shuffle(cards)

	#print(cards)

	dealer_bust = False
	bust = False

	hand = []
	dealer = []

	wobbler = 1
	dont_stick_twice = True

	hand.append( cards.pop(0) )
	dealer.append( cards.pop(0) )
	hand.append(cards.pop(0) )
	dealer.append( cards.pop(0) )

	print('deal')

	# digify:
	print('your hand (save this)')
	print(hand)


	print(digify(hand))  # gives us 0b100000
	print('dealers first card')
	print(dealer[0])
	#print(digify(dealer[0], dealer[1]))  # gives us 0b1011010

	#print(hand[0][0])

	# stick or twist
	print('(s)tick or (t)wist')

	stick_or_twist = 't'
	#print(stick_or_twist) # seems to work...



	#here

		
		

	first_time = True

	# if twist repeat
	while(first_time or prediction in new_predictions == 1):

		
		first_time = False

		# Assume you have a trained model 'clf' and new input data 'new_data_array'
		new_data_array = np.array([[add_zeros(digify(hand))]])

		# Use the trained model to make predictions
		new_predictions = clf.predict(new_data_array)

		print(new_predictions)

		# Interpret the predictions
		for prediction in new_predictions:
			if prediction == 0:
				print("Stick")
			else:
				print("Twist")


		if(prediction in new_predictions == 1):
			stick_or_twist = 't'
		else:
			stick_or_twist = 's'
		
		
		if(stick_or_twist == 't'):
			
			hand.append( cards.pop(0) )
			print('(save this)')
		
		else:# stick

			pass

		print(hand)

		#todo
		if( sum(hand) > 21 ):
			hand = [1 if x==11 else x for x in hand]# swap all 1s for 11
			if( sum(hand) > 21 ):
				print('bust!')
				bust = True
				break

	if(not bust):

		# dealer twists until its >= 18
		while(True):
			if(sum(dealer) < 18 ):
				dealer.append( cards.pop(0) )
			else:
				break
			if(sum(dealer) > 21):
				dealer = [1 if x==11 else x for x in dealer]# swap all 1s for 11
				if(sum(dealer) > 21):
					print('dealer bust!')
					dealer_bust = True
					break


		# check for winner
		if(sum(hand) > sum(dealer)):
			print('you win!')
		else:
			if(dealer_bust):
				print('you win!')
			else:
				if(len(hand) >= 5): # five card trick
					print('you win! (5 card trick!)')
				else:# check for aces
					hand = [1 if x==11 else x for x in hand]# swap all 1s for 11
					if(sum(hand) <= 21):
						if(sum(hand) > sum(dealer)):
							print('you win!')
						else:
							print('you lose!')
							print('dealer had: ' + str(dealer))
					else:
						print('bust! (2)'+str(sum(hand)))

	# save






