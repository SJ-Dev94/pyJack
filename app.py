import random

#suits of cards
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#ranks of cards
ranks = [
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Jack', 'Queen', 'King', 'Ace'
]
#corresponding values of cards in relation to ranks
values = {
    'Two': 2,
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
                self.deck.append(Card(suit, rank))

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
        self.playerBank += (self.bet * 2)

    def losingHand(self):
        self.playerBank -= self.bet


p1Chips = playerChips()


def bets(playerChips):
    while True:
        try:
            p1Chips.bet = int(input('\nPlace your bet: '))
            div()
        except ValueError:
            div()
            print('Bet must be a number between 0-500')
            div()
        else:
            if p1Chips.bet >= 500:
                print('This bet cannot be made.')
            else:
                break


def hit(deck, hand):
    hand.addCard(deck.dealCards())
    hand.modifyAce()


def hitOrStand(deck, hand):  #maybe seperate these into their own functions
    global currentlyPlaying

    while currentlyPlaying:
        div()
        question = input("\nHit or Stand? Type 'hit' or 'stand'\n ")
        div()

        if question.lower() == 'hit':
            hit(deck, hand)

        elif question.lower() == 'stand':
            print('\nStand. Dealers turn.')
            currentlyPlaying = False
        else:
            print("\ntry again")
            continue

        break


#display functions


def showLimitedHand(player, dealer):
    print("\nDealers Hand:")
    print("\nFirst Card Hidden and", *dealer.cards)
    print('\nPlayers Hand: \n', *player.cards)


def showAllHands(player, dealer):

    print("\nDealers Hand:", '\n', *dealer.cards, '\n')
    print("\nDealers Value:", dealer.cardValue)
    print("\nPlayers Hand:", '\n', *player.cards)
    print("\nPlayers Value", player.cardValue)


def div():
    print('---------------------------------------')


#logic


def playerBust(player, dealer, chips):
    div()
    print("\nPlayer busts\n")
    div()
    p1Chips.losingHand()


def playerWinner(player, dealer, chips):
    div()
    print("\nWinner\n")
    div()
    p1Chips.winningHand()


def dealerWin(player, dealer, chips):
    div()
    print("\nDealer wins!\n")
    div()
    p1Chips.losingHand()


def dealerBust(player, dealer, chips):
    div()
    print("\nDealer Busts\n")
    div()
    p1Chips.winningHand()


def tie(player, dealer):
    div()
    print("\nIt's a tie!\n")
    div()


while True:

    currentlyPlaying = True

    #opening game text
    div()
    print("Welcome to Blackjack. Hit 21 to win!")
    div()
    deck1 = Deck()
    deck1.shuffle()
    #player 1
    p1hand = Hand()
    p1hand.addCard(deck1.dealCards())  #revise these
    p1hand.addCard(deck1.dealCards())  #revise these

    #dealer1
    d1hand = Hand()
    d1hand.addCard(deck1.dealCards())  #revise these
    d1hand.addCard(deck1.dealCards())  #revise these

    bets(p1Chips)

    while currentlyPlaying:

        showAllHands(p1hand, d1hand)

        hitOrStand(deck1, p1hand)

        if p1hand.cardValue > 21:
            playerBust(p1hand, d1hand, p1Chips)
            div()
            showAllHands(p1hand, d1hand)
            div()
            break

    if p1hand.cardValue <= 21:

        if d1hand.cardValue < 17:
            d1hand.addCard(deck1.dealCards())
            div()
            showAllHands(p1hand, d1hand)
            div()

        if d1hand.cardValue > 21:
            div()
            dealerBust(p1hand, d1hand, p1Chips)
            div()
        elif d1hand.cardValue > p1hand.cardValue:
            dealerWin(p1hand, d1hand, p1Chips)

        elif d1hand.cardValue < p1hand.cardValue:
            playerWinner(p1hand, d1hand, p1Chips)
        else:
            tie(p1hand, d1hand)

    print("Players current bankroll:", p1Chips.playerBank)

    newRound = input("Play again? Enter 'y' or 'n':\n")

    if newRound == 'y':
        continue

    else:
        print("See you next time!")

        break
