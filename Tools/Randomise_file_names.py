import random
import os

set_number = "Images/Set "+input("Set Number: ")

for file in os.listdir(set_number):
    os.rename(folder + "/" + file, folder + "/" + str(random.randint(0, 100000000)) + ".jpg")