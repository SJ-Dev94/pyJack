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
global activeGame

global currentlyPlaying 

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
        oneCard = self.deck.pop()
        return oneCard
 
class Hand:
   
    def __init__(self):
        self.cards = []
        self.cardValue = 0
        self.aces = 0
   
    def addCard(self, card):
        self.cards.append(card)
        self.cardValue += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def modifyAce(self):
        while self.cardValue > 21 and self.aces:
            self.cardValue -= 10
            self.aces -= 1
        
        
    
class playerChips:
    
    def __init__(self):
        self.playerBank = 500
        self.bet = 0
    
    def winningHand(self):
        self.playerBank += self.bet
    
    def losingHand(self):
        self.playerBank -= self.bet


def bets(playerChips):
    while True:
        try:
            playerChips.bet = int(input('Place your bet: '))
        except ValueError:
            print('Bet must be a number between 0-500')   
        else:
            if playerChips.bet >= 500:
                print('This bet cannot be made.')
            else:
                break

def hit(deck, hand):
    hand.addCard(deck.dealCards())
    hand.modifyAce()
    

def hitOrStand(deck, hand): #maybe seperate these into their own functions
    global currentlyPlaying
    
    while currentlyPlaying:
        question = input("Hit or Stand? Type 'hit' or 'stand' ")
        if question[0].lower() == 'hit':
            hit(deck, hand)
        elif question[0].lower() == 'stand':
            print ('Stand. Dealers turn.')
            currentlyPlaying = False
    
        break

def showLimitedHand(player, dealer):
    print("Dealers Hand:")
    print("First Card Hidden and", dealer.cards[1])
    print('Players Hand: \n', player.cards[0],'and', player.cards[1])

def showAllHands(player, dealer):
    print("Dealers Hand", dealer.cards[0])
    print("Dealers Value", dealer.cardValue)
    print("Players Hand", player.cards[0])
    print("Players Value", player.cardValue)
    
#
def playerBust(player, dealer, chips):
    print("Player busts")
    playerChips.losingHand()
    
def playerWinner(self, player, dealer, chips):
    print("Winner")
    playerChips.winningHand(chips)
    
def dealerWin(player, dealer, chips):
    print("Dealer wins!")
    playerChips.losingHand(chips)

def dealerBust(player, dealer, chips):
    print("Dealer Busts")
    playerChips.losingHand(chips)
    
def tie(player, dealer):
    print("It's a tie!")



while True:
    
    currentlyPlaying = True
    
    #opening game text
    print("Welcome to Blackjack. Hit 21 to win!")
    deck1 = Deck()
    deck1.shuffle()
    #player 1
    p1hand = Hand()
    p1hand.addCard(deck1.dealCards()) #revise these
    p1hand.addCard(deck1.dealCards()) #revise these
    
    #dealer1
    d1hand = Hand()
    d1hand.addCard(deck1.dealCards()) #revise these
    d1hand.addCard(deck1.dealCards()) #revise these

    p1Chips = playerChips()
    
    bets(playerChips)
    
    while currentlyPlaying:
        
        showLimitedHand(p1hand, d1hand)
        
        hitOrStand(deck1, p1hand)
        
        if p1hand.cardValue > 21:
            playerBust(p1hand, d1hand, p1Chips)
            break
        
        if p1hand.cardValue <= 21:
            while d1hand.cardValue < 17:
                hit(deck1, d1hand)
                
        showAllHands(p1hand, d1hand)
        
        if d1hand.cardValue > 21:
            dealerBust(p1hand, d1hand, playerChips())
            
        elif d1hand.cardValue > p1hand.cardValue:
            dealerWin(p1hand, d1hand, playerChips())
        
        elif d1hand.cardValue < p1hand.cardValue:
            playerWinner(p1hand, d1hand, playerChips())
        
        else:
            tie(p1hand, d1hand)
    
    print("Players current winnings are:", p1Chips.playerBank )
    
    newRound = input("Play again? Enter 'Yes' or 'No' ")
    
    if newRound[0].lower() == 'Yes':
        continue
    
    else:
        print("See you next time!")

    break        