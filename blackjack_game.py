
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

def game_logic(foo):
	if( sum(foo) < 16 ):
		return 't'
	else:
		return 's'

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

# if twist repeat
while(stick_or_twist == 't'):

	stick_or_twist = game_logic(hand)
	
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

print(digify(hand))  # gives us 0b100000
print(add_zeros(digify(hand)))


