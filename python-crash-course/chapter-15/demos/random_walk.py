from random import choice

class RandomWalk:
    """模拟随机游走的类"""
    
    def __init__(self, num_points=5000):
        # 设置游走的点总数
        self.number_points = num_points
        # 记录游走经过的点坐标，初始坐标为 (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        current_point = [0, 0]
        while len(self.x_values) < self.number_points:
            direction = choice([[1, 1], [1, -1], [-1, 1], [-1, -1]])
            current_point[0] += direction[0]
            current_point[1] += direction[1]
            self.x_values.append(current_point[0])
            self.y_values.append(current_point[1])
            
    def desc_points(self):
        i = 0
        while i < len(self.x_values):
            print(f"({self.x_values[i]}, {self.y_values[i]})")
            i += 1