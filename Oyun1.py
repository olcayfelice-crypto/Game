import pygame
name = input("What is your name? ")
print(f"Hello", name ,"!")
age = input("What is your age " + name + "?  ")
print("This will not affect your gameplay.")
player = input("Type your player: ")
if player =="1" :
 print("You chose Player 1")
elif player == "2" :
 print("You chose Player 2")
if player == "3":
 print("You chose Player 3")
elif player == "4":
 print("You chose Player 4")
playernumber = input("Please type the number that you want: ")
pygame.init()
print("-------------------")
print(name)
print(playernumber)
print(f"Player" + " " + player)
print("-------------------")
print(" " + " " + "   ")

