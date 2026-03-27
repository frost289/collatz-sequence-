import random
import re
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    n = []
    for i in range(0,length + 1):
        n.append(characters[random.randint(0,len(characters)-1)])
    str(n)
    print(n)




generate_password(5)