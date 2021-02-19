#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[2]:



class Card:
	def __init__(self,rank,suit):
		self.rank=rank
		self.suit=suit
		self.value=values[rank]

	def __str__(self):
		return self.rank+" of "+  self.suit



# In[3]:


class Player:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        self.all_cards=[]
        
    def remove_amt(self,amt):
        self.balance=self.balance-amt
    
    def add_amt(self,amt):
        self.balance=self.balance+amt
        
    def add_one_card(self,card):
        self.all_cards.append(card)
 
    ''''
    def player_current_val(self):
        val=0
        for card in self.all_cards:
            val+=card.value
        if val>21:

            for card in self.all_cards:
                if card.rank=="Ace":
                    while True:
                        choice_of_ace_value=input(f"Do you want to count your {str(card)} as 11 or a 1?(Enter either 11 or 1)")
                        if choice_of_ace_value=='11' or choice_of_ace_value=='1':
                            break
                            
                        else:    
                            print("Please enter either 11 or 1!")
                        
                    
                    if choice_of_ace_value=='1':
                        val=val-10
                        
        return val'''
    
    def player_current_val(self):
        val=0
        for card in self.all_cards:
            val+=card.value
        
        for card in self.all_cards:
            
            if card.rank=="Ace":
                if val>21:
                    val=val-10
        
        
        return val


# In[4]:


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
         return self.all_cards.pop()


# In[5]:


##setup of the game
game_deck=Deck()
player=Player("Shashwat",1000)
computer=Player("Computer")

game_deck.shuffle()

                


# In[11]:


##game logic

#starting a new round
round=1
game_end=False
while game_end==False:
    #making sure both computer and player has no cards at the start
    player.all_cards=[]
    computer.all_cards=[]
    print("round ",round)
    #prompt player for bet amt
    
    '''
    while True:
        bet_amt=int(input("How much do you want to bet?"))
    
        if bet_amt>player.balance:
            continue
        else:
            break
     '''
    bet_amt=int(input("How much do you want to bet?"))
        
    #deal player 2 cards
    
    player.add_one_card(game_deck.deal_one())
    player.add_one_card(game_deck.deal_one())
    print("Your current cards are-")
    for card in player.all_cards:
        print(str(card))
        
    #deal the computer 2 cards
    
    computer.add_one_card(game_deck.deal_one())
    computer.add_one_card(game_deck.deal_one())
    
    print("dealer has two cards , one of which is ", computer.all_cards[0])
        
    while player.player_current_val()<=21:
        current_total=player.player_current_val()
        print("your current total is ", current_total)
        deal_more=input("do you want to be dealt another card?(Y or N)")
        if deal_more=="Y":
            player.add_one_card(game_deck.deal_one())
            print("Your current cards are-")
            for card in player.all_cards:
                print(str(card))
        if deal_more=="N":
            break
            
    if player.player_current_val()>21:
        #bust
        current_total=player.player_current_val()
        print("your current total is ", current_total)
        player.remove_amt(bet_amt)
        print(f"You lost!{bet_amt}, your current balance is {player.balance}")
        if input("ENTER anything to continue, Type N to end")=="N":
            game_end=True
            break
        else:
            round+=1
            continue
            
    else:
        #computer's turn !
        print("computers current cards are-")
        for card in computer.all_cards:
            print(str(card))
        computer_current_value=computer.player_current_val()

        while computer_current_value<=current_total:
            computer.add_one_card(game_deck.deal_one())
            print("computers current cards are-")
            for card in computer.all_cards:
                print(str(card))
            computer_current_value=computer.player_current_val()    
            if computer_current_value>21:
               
                
                #bust
                #for now the player is taking care of the ace mechanic for computer too , could be automated in future
                #let the player know
                print("computer has bust with",computer_current_value)
                #double their bet
                player.add_amt(bet_amt)
                print(f"Your current balance is {player.balance}")
                if input("ENTER anything to continue, Type N to end")=="N":
                    game_end=True
                else:
                    round+=1
                    break
            else:
                continue
                
        
        #out of this while loop and computer hasnt lost yet means computer has won 
        if computer_current_value<=21 and computer_current_value>current_total:
            player.remove_amt(bet_amt)
            print(f"You lost {bet_amt} chips!,computer beat you with {computer_current_value}>{current_total} your current balance is {player.balance}")
            if input("ENTER anything to continue, Type N to end")=="N":
                game_end=True
                break
            else:
                round+=1
                continue
            
        
                
        
            
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




