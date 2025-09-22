# 第 1 章 Python 数据模型

为什么不是 collections.len() 而是 len(collections)？

> 魔术方法：也成特殊方法，在 Python 中指交由 Python 解释器执行的特殊方法。通常命名采用 `__xxx__`，例如 `__getitem__()` 和 `__len__()`

## 1.1 一摞 Python 风格的纸牌

我们使用一个简单的例子来展示如何实现 `__getitem__` 和 `__len__()` 这两个特殊方法，通过这个例子我们能够见识到特殊方法的强大。

```python
# 一摞Python风格的纸牌
import collections

# 声明纸牌类
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 声明Card实例
card = Card('7', 'hearts')
print(card)         # Card(rank='7', suit='hearts')


# 声明扑克牌
deck = FrenchDeck()
print(len(deck))
print(deck[7])      # Card(rank='3', suit='hearts')
```

首先，我们通过 `collections.namedtuple` 构建了一个简单的类表示一张纸牌。namedtuple 用于构建只有少数属性没有方法的对象，比如数据库条目。

我们声明的 FrenchDeck 类和任何 Python 标准集合类型一样，可以使用 len() 函数来查看一叠牌有多少张：

```python
len(deck)       # 52
```

从一组纸牌中抽取一张特定的纸牌，比如说第一张或最后一张，是很容易的：`deck[0]` 或 `deck[-1]`。这都是有 `__getitem__()` 方法提供的：

```python
deck[0]         # Card(rank='2', suit='spades')
deck[-1]        # Card(rank='A', suit='hearts')
```

从一摞卡牌中随机挑选一张卡牌：

```python
from random import choice
--snip--
choice(deck)        # Card(rank='4', suit='hearts')
```
