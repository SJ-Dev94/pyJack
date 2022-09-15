
#Creates a card object with a suit and a rank
#adds method to combine suit and rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 
           
    def __str__(self):
        return self.rank + 'of' + self.suit

#Creates a deck object 
class Deck:
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
    
deck1 = Deck()
print(deck1)