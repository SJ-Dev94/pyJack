import random

#suits of cards
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#ranks of cards
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
#corresponding values of cards in relation to ranks
values = {'Two': 2, 
          'Three': 3, 
          'Four': 4, 
          'Five': 5,
          'Six': 6,
          'Seven': 7,
          'Eight': 8,
          'Nine': 9,
          'Ten': 10, 
          'Jack': 10,
          'Queen': 10,
          'King': 10,
          'Ace': 11
          }

#Determines whether game is active
activeGame = False


#Creates a card object with a suit and a rank
#adds method to combine suit and rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
           
    def __str__(self):
        return self.rank + ' of ' + self.suit + '\n'

#Creates a deck object 
class Deck(Card):
    def __init__(self):
        self.deck = []
        #outer loop that loops over suits
        for suit in suits:
            #inner loop that loops over ranks
            for rank in ranks:
                #uses the outer and inner loop to append the cards to the deck array
                self.deck.append(Card(suit,rank))
    def __str__(self):
        #holds all of the cards in the deck
        composition = ''
        for card in self.deck:
            composition += card.__str__()
        return 'Card Deck: ' + composition
    def shuffle(self):
        random.shuffle(self.deck)
    def dealCards(self):
        card = self.deck.pop()
        return card
 
class Hand:
    def __init__(self):
        self.cards = []
        self.cardValue = 0
    def addCard(self, card):
        self.cards.append(card)
        self.cardValue += values[card.rank]
    
class playerChips:
    def __init__(self):
        self.playerBank = 500
        self.bet = 0
    def winningHand(self):
        self.startingMoney += self.bet
    def losingHand(self):
        self.playerBank -= self.bet

def bets(playerChips):
    while True:
        try:
            playerChips.bet = int(input('Place your bet: '))
        except inputError:
            print('Bet must be a number between 0-500')   
        else:
            if playerChips.bet >= 500 or playerChips.playerBank <  playerChips.bet:
                print('This bet cannot be made.')
            else:
                break
def hit(deck, hand):
    hand.addCard(deck.deal())

def hitOrStand(deck, hand):
    while True:
        question = input("Hit or Stand? Type 'hit' or 'stand' ")
        if question[0].lower() == 'hit':
            hit(deck,hand)
        elif question[0].lower() == 'stand':
            print ('Stand. Dealers turn.')
            activeGame = False
        else:
            print("Try again")
            continue
        break
deck1 = Deck()
deck1.shuffle()
p1 = Hand()
p1.addCard(deck1.dealCards())
p1.addCard(deck1.dealCards())
p1.cardValue

for card in p1.cards:
    print(card)
    

