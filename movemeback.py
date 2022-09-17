 while activeGame:
        hitOrStand(deck1, p1hand)
        showHand(p1hand, d1hand)
        
        if p1hand.cardValue > 21:
            bust(p1hand, d1hand, p1Chips)
            break
        
        if p1hand.cardValue <= 21:
            while d1hand.cardValue < 17:
                hit(deck1, d1hand)
                
        showHand(p1hand, d1hand)
        
    if d1hand.cardValue > 21:
        bust(p1hand, d1hand, p1Chips)
    elif d1hand.cardValue > p1hand.cardValue:
        dealerWin(p1hand, d1hand, p1Chips)
    #elif d1hand.cardValue < p1hand.cardValue:
        #winner(p1hand, d1hand, p1Chips)
    #else:
        #tie(p1hand, d1hand)
    
    print("Players earnings are:", p1Chips)
    
    #newGame = input("Play again? 'Yes' or 'No'")
    #if newGame[0].lower()=='y':
        #activeGame = True
        #continue
    #else:
        #print("Come back soon!")
        #break
    


