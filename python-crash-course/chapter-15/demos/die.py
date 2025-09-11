from random import randint

class Die:
    """模拟骰子"""
    
    def __init__(self, num_sides=6):
        """初始化，默认是六面的骰子"""
        self.num_sides = num_sides
        
    def roll(self):
        """模拟掷骰子"""
        return randint(1, self.num_sides)