import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    for i in range(0,length + 1):
        print(characters[random.randint(0,length + 1)])


generate_password(5)