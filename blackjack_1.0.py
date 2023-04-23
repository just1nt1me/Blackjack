from itertools import product
import random

#create a deck of 52 playing cards
suit = ["Spade" , "Club" , "Diamond" , "Heart"]
number = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
face=["Jack","Queen","King","Ace"]
card_values={}
for i , value in enumerate(number,start=2):
	card_values[value]=i
for value in face:
	if value!="Ace":
		card_values[value]=10
	else:
		card_values[value]=11
deck=list(product(suit,number))
facedeck=list(product(suit,face))
deck.extend(facedeck)
# print(len(deck))
# print(deck)

#function for a player to draw a card from the deck
def draw():
	global playerscore
	card=random.choice(deck)
	list(card)
	display_card="{} of {}s".format(card[1],card[0])
	card_math=card_values[card[1]]
	if card[1]=="Ace" and playerscore+card_math>21:
		card_math=1
	playerscore+=card_math
	# print(playerscore)
	print(display_card)
	deck.remove(card)
	# print(len(deck))
	return playerscore

#function for the dealer to draw a card from the deck
def dealer_draw():
	global dealerscore
	global dealer_card_count
	card=random.choice(deck)
	list(card)
	display_card="{} of {}s".format(card[1],card[0])
	card_math=card_values[card[1]]
	if card[1]=="Ace" and playerscore+card_math>21:
		card_math=1
	if dealer_card_count==0:
		print(display_card)
	dealer_card_count+=1
	dealerscore+=card_math
	# print(dealerscore)
	deck.remove(card)
	# print(len(deck))
	return dealerscore

#contain the game within a function so multiple games can be played
def game():
	global deck
	global playerscore
	global dealerscore
	global dealer_card_count
	while True:
		deck = list(product(suit, number))
		facedeck = list(product(suit, face))
		deck.extend(facedeck)
		playerscore = 0
		dealerscore = 0
		dealer_card_count = 0
		start_game=input("Let's play Blackjack. Ready to start? Enter Yes/No: ")
		if start_game.title()=="Yes":
			print("Player: ")
			draw()
			print("Dealer: ")
			dealer_draw()
			print("Player: ")
			draw()
			dealer_draw()
		draw_again = input("Hit? Yes/No ")
		while draw_again.title() == "Yes" and playerscore <= 21:
			draw()
			if playerscore > 21:
				print(playerscore)
				print("You busted.")
				break
			else:
				draw_again = input("Hit? Yes/No ")

		while dealerscore<17:
			dealer_draw()

		if playerscore <= 21:
			print("Your score:", playerscore)
			print("Dealer's score:", dealerscore)
			if dealerscore>=playerscore and dealerscore<=21:
				print("Dealer wins.")
			else:
				print("You win!")
		play_again=input("Do you want to play again? Enter Yes/No: ")
		if play_again.title()=="No":
			break
game()