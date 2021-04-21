""" A fun guessing game where the user has to guess a President based off of
information provided. 
Reads in a csv file, turn into dataframe with pandas, Stores the user guesses
to see if the've guessed correctly or incorrectly (providing hints for each 
incorrect answer).
"""
# Group: Christian Thompson, Loranika Sharma, Christopher Marroquin, Jay Patel
# INST326
# Final Project

import pandas as pd
from random import random

#Replace comment with a random number generator

class User:
    """
    This class keeps track of the users attempts, name and score
    
    Attributes:
        name(String): Name of user
        attempts(int): Number of attempts
        score(int): The score of the user
    """
    def __init__(self,name,score=0):
        """
        Initializes a user object and creates attempts attributes and a score attribute
        
        Args:
            name(String): Name of user
        
        Side effects:
            Initializes values
        """
    
    def get_score(self):
        """
        Allows the user see what their score is.
        
        Side effects:
            prints out the score of the user.
        """


class Game:
    """
    This class keeps track of the game state and will compare values to the 
    user class
    
    Attributes:
        name(String): Name of user
        series(str): Number of attempts
        score(int): The score of the user
        name: president name
        File: Csv file
    """
    def __init__(self,name):
        """
       Initializes the name of the game.
        Args:
            name(String): Name of game
        
        Side effects:
            Initializes values
        """
        self.name = name
        
    def guess(self,ser,player):
        """
        Is the guessing game
        
        Attributes:
            ser(series): A President name column from the file (exaplain stucture of DF)
            player (user): Is a user object
        Side effects:
            Increases score based on correct answer given.
        """
        
        
    def compare(self,ser1,ser2):
        """
        This class keeps track of the users attempts, name and score
    
        Args:
            ser1(series): Name of user
            der2(series): Number of attempts
        Returns:
            Prints out information regarding the presidents
        """
        
    def reverse(self,data_frame):
        """
        Allows the user to put in information about a president and get the president
        name.
        
        Args:
            data_frame(data frame):The data frame consisting of all the presidents 
        Returns:
            Prints out the president the user is specifing
        """
    
    def score(self,score,name,file):
        """
        Keeps track of all the scores of all players who haver ever played and
        updates the users specific score
        
        Attributes:
            file (string): Name of the file where the leader booard is kept
            name (string): The name of the user
            score (int): The users score
        
        Side effects:
            Updates the users score on the leaderboards.
        """
        
def main():
    """
    In the main function the CSV file will be opened. The game instacne and the 
    user instance will be initiated. A file will be created where the users score
    will be tracked. This is also where all of the funcitons/methods will be ran.
    """
    df = pd.read_csv("INST326 FINAL_Presidents.csv",index_col="Number President")
    print("Hello! Welcome to the game featuring all of the presidents of the United\
          States! We here at Presidents INC are happy you cam to play. Before we\
          get started please enter your full name and a name you would like to give\
          to the game your about to play.")
    name = input("Please enter your name: ")
    game_name = input("Please enter the name you wish to call this game: ")
    game1 = Game(game_name)
    player = User(name,0)
    print("Now that you have entered the information. It is time for you to pick\
        the game you want to play. The first is a guessing game where information of a \
        random president will be given to you and you will have 3 guesses to guess\
        the correct president. The second option is an interactive expericen where\
        you will get to choose 2 presidents of the US and see how they differ. The third\
        choice is when you get to give the information fo a president and we guess\
        the president you are talking about.")
    game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3")
    
    while 0>= game_choice or game_choice >3:
         game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3")
    
    if game_choice == 1:
        ran = random.randint(1,46)
        game1.guess(df.loc[ran],player)
    elif game_choice == 2:
        
    elif game_choice == 3:
        
    
    def score_board(file):
        """
        Prints out the leader of board
        Args:
            file (string): The file where all of the socres are kept.
        
        Returns:
            prints out the leader boards
        """        

#Replace this comment with parse_args function

if __name__ == "__main__":
    """
    """