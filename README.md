# INST326
Final Project for INST326

This python project is a fun guessing game where the user has to guess a President based off of some information our program provides. 

The code reads in a csv file, turns it into dataframe using pandas then stores the users guesses
to see if they have guessed correctly or incorrectly (providing hints for each 
incorrect answer).

The project consists of two main classes a User class that keeps track of the users attempts, name and score and a Game class that keeps track of the game state and will compare values to the user class

User Class: This class consists of three function: __init__(), get_score(), and sub_score() 
Game Class: This class consists of six functions: __init__(), guess(), compare(), questions(), reverse(), and score()

# Gameplay
There are three games within the project 

#1 In game 1 the user is given facts/infromation related to a specifc president and will have to guess correctly to get points

#2 In game 2 the user can compare two presidents and get information about both

#3 In game 3 the computer will try and guess the president the user is thinking of based on information provided by the user.

# How to Play/Run Program
To play to game/run this python code you need to go into your terminal and type the following command: python3 INST326_Final_Project.py
