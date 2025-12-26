import random
import art
game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)
print("Welcome to the game!")
your_cards = [random.choice(cards), random.choice(cards)]
total = sum(your_cards)
if 11 in your_cards and total > 21:
    your_cards.remove(11)
    your_cards.append(1)
    total = sum(your_cards)
print("your cards are:")
print(your_cards)
print(total)
if total == 21:
    print("you win!")
    game = False
dealer_card = [(random.choice(cards))]
total_dealer= sum(dealer_card)
print("Dealer first card:", dealer_card[0])
while game :
    if input("Do you want to take another card? y for yes or n for no: ") == "y":
        print("your new card is:")
        your_cards.append(random.choice(cards))
        total = sum(your_cards)
        print("your cards are:" , your_cards)
        print("total:" , total)
        if total > 21:
            print("You Lost!")
            game = False
    else:
        game = False
while total_dealer < 17:
    dealer_card.append(random.choice(cards))
    total_dealer = sum(dealer_card)
    if 11 in dealer_card and total_dealer > 21:
        dealer_card.remove(11)
        dealer_card.append(1)
        total_dealer = sum(dealer_card)
print("Dealer cards:", dealer_card)
print("Dealer total:", total_dealer)
if total_dealer == 21:
    print("dealer wins!")
elif total_dealer > 21:
    print("You win! Dealer busted.")
elif total_dealer > total:
    print("dealer wins!")
elif total > total_dealer:
    print("you win!")
elif total_dealer == total:
    print("Draw!")