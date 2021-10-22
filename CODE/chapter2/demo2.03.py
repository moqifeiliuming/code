# 需要在Windows下执行
import os           
import sys
f_handler=open('out.log', 'w')
oldstdout = sys.stdout
sys.stdout=f_handler
os.system('cls')
sys.stdout = oldstdout

