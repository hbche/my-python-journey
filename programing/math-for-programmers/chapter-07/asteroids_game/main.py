import sys
from model import Ship, Asteroid, PolygonModel
from random import randint
import pygame
from math import pi

ship = Ship()

asteroid_count = 10
asteroids = [Asteroid() for _ in range(0, asteroid_count)]

for ast in asteroids:
    ast.x = randint(-9, 9)
    ast.y = randint(-9, 9)
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

width, height = (400, 400)

def to_pixels(x, y):
    """
    由于笛卡尔坐标系是以屏幕中心为原点，向右和向上分别为x轴正坐标和y轴正坐标
    pygame坐标系，以屏幕左上角为坐标原点，向右和向下才是x轴正坐标和y轴正坐标
    我们现在需要实现将笛卡尔坐标转换为pygame坐标：
    因为多边形的坐标原点在屏幕中心，且分成了-10到10这20个单元格，所以笛卡尔坐标每一个单位长度对应屏幕的400/20像素
    """
    return (width/2 + width*x/20, height/2 - height*y/20)

def draw_poly(screen, polygon_model: PolygonModel, color=GREEN):
    """
    在pygame的屏幕上绘制多边形
    """
    # 获取每个多边形对象的端点坐标
    pixel_points = [to_pixels(x, y) for x, y in polygon_model.transformed()]
    # 以闭合回路在screen上以指定颜色绘制多边形
    pygame.draw.aalines(screen, color, True, pixel_points, 10)
    
def draw_segment(screen, v1, v2, color=RED):
    """
    在屏幕上绘制线段
    """
    pygame.draw.aalines(screen, color, False, [to_pixels(*v1), to_pixels(*v2)], 10)
    
screenshot_mode = False
    
def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode([width, height])
    
    pygame.display.set_caption('Asteroids!')
    
    done = False
    clock = pygame.time.Clock()
    
    # P按键是否被按下，用于存储当前游戏截图
    # p_pressed = False
    
    while not done:
        
        clock.tick()
        
        for event in pygame.event.get():
            # 监听退出程序事件
            if event.type == pygame.QUIT:
                done = True
                
        
        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()
        
        for ast in asteroids:
            ast.move(milliseconds)
            
        if keys[pygame.K_LEFT]:
            ship.rotation_angle += milliseconds * (2*pi/1000)
            
        if keys[pygame.K_RIGHT]:
            ship.rotation_angle -= milliseconds * (2*pi/1000)
            
        # 获取飞船的激光坐标
        laser = ship.laser_segment()
        
        # if keys[pygame.K_p] and screenshot_mode:
        #     p_pressed = True
        # elif p_pressed:
        #     pygame.image.save(screen, f'figures/asteroid_screenshot_{milliseconds}.png')
        #     p_pressed = False
            
        # 绘制屏幕
        screen.fill(WHITE)
        
        # 监听空格绘制激光射线
        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)
            
        # 绘制飞船
        draw_poly(screen, ship)
        
        # 绘制小行星
        for asteroid in asteroids:
            # 如果小行星被激光击中则从屏幕上移除
            if keys[pygame.K_SPACE] and asteroid.does_intersect(laser):
                asteroids.remove(asteroid)
            else:
                draw_poly(screen, asteroid, color=GREEN)
                
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == '__main__':
    if '--screenshot' in sys.argv:
        screenshot_mode = True
        
    main()