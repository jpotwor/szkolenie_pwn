import os
import time

print(os.getcwd())

print(os.listdir('.'))

print(time.ctime(os.path.getmtime('zwierzeta.txt')))
