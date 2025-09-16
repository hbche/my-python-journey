# 一摞Python风格的纸牌
import collections
from random import choice

# 声明纸牌类
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        """实现len方法"""
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    

# # 声明Card实例
# card = Card('7', 'hearts')
# print(card)         # Card(rank='7', suit='hearts')

# 声明扑克牌
deck = FrenchDeck()
# print(len(deck))    # 52
# print(deck[0])      # Card(rank='2', suit='spades')
# print(deck[-1])     # Card(rank='A', suit='hearts')
print(choice(deck))     # Card(rank='4', suit='hearts')

# for card in reversed(deck):
    # print(card)