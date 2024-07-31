import sys
import os
import time
import socket

p = print
oss = os.system
oss("pip install termcolor")
red = "red"
blue = "blue"
green = "green"
white = "white"

from termcolor import colored, cprint
col = colored

p(col("Starting ... ", red)),  oss("cls"), time.sleep(0.4), p(col("Starting ... ", red)),  oss("cls"), time.sleep(0.2), p(col("Starting ... ", red)),  oss("cls"), time.sleep(0.5), p(col("Starting ... ", red)), time.sleep(1.2), oss("cls")

def save_user_data(name):
    with open("user_data.txt", "w") as file:
        file.write(name)

def read_user_data():
    try:
        with open("user_data.txt", "r") as file:
            name = file.read()
            return name
    except FileNotFoundError:
        return None
    
name = read_user_data()

if name:
    p("Welcome back, " + name + "!")
else:
    name = input("Enter your name: ")
    save_user_data(name)
    p(colored("Hello, ", red + name, white + "! Your name has been saved."))

directory = read_user_data

def save_user_data(directory):
    with open("directory_data.txt", "w") as file:
        file.write(directory)

def read_user_data():
    try:
        with open("directory_data.txt", "r") as file:
            directory = file.read()
            return directory
    except FileNotFoundError:
        return None
    
if directory:
    directory = input("Enter your directory: ")
    save_user_data(directory)
    p(col("Your directory has been saved as: " + directory, red))
else:
    print(col("Failed", red))
    
