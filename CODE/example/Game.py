import pygame
# pygame.version  显示版本号
import sys
pygame.init()   # 初始化pygame
size = width,height = 320, 240   # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口

# 执行死循环，确保窗口一直显示
while True:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
pygame.quit()  # 退出pygame

