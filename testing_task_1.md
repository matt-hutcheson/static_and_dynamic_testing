### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python

class CardGame:


  def checkforAce(self, card):
    if card.value = 1: # error - should be '==' not '='
      return true
    else # error - missing ':' at end of statement
      return false

  dif highest_card(self, card1 card2) # error - should be 'def' not 'dif' and missing ',' between card1 and card2 and missing ':' at end of statement
    if card1.value > card2.value # error - missing ':' at end of statement
      return card
    else # error - missing ':' at end of statement
      return card2
 

 def cards_total(cards): # error indent of section off
   total # error - total not assigned, should be 'total = 0'
   for card in cards:
     total += card.value
     return "You have a total of" + total # error - mixing types, total should be 'str(total)'


```
