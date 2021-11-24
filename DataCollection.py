import random 
import numpy as np
import math
#first I import numerous libraries that would be necessary to bring the project to life
#random library helps in randomization. Numpy relates to arrays and mathematical functions 

#collect info

#collect total players
player_count=int(input("Enter participant count? "))
team_count=int(input("How many teams do you want "))

player_counts=int(player_count)
team_counts=int(team_count)

#to determine the count of members in each team, the total players count is divided by teams
ratio=int(player_count/team_count)

print(ratio)
print("For this event, you will have ", ratio," players in ", team_count, " teams")
#list to store and hold players for later use 
player_list=[]