import os
import time

print(os.getcwd())
os.mkdir('new_folder')
time.sleep(2)
os.rename('new_folder', 'new_folder2')
# time.sleep(1)
# os.rmdir('new_folder2')



print("sdf")