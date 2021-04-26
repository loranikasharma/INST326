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
import random

#Replace comment with a random number generator

class User:
    """
    This class keeps track of the users attempts, name and score
    
    Attributes:
        name(String): Name of user
        attempts(int): Number of attempts
        score(int): The score of the user
    """
    def __init__(self,name,score):
        """
        Initializes a user object and creates attempts attributes and a score attribute
        
        Args:
            name(String): Name of user
            score (int): The number of points the user starts off with by default
        Side effects:
            Initializes values
        """
        self.name = name
        self.score = score
    
    def get_score(self):
        """
        Allows the user see what their score is.
        
        Side effects:
            returns the score of the player
        """
        return self.score
    
    def sub_score(self,amount):
        """
        Allows for the players score to be subtracted.
        
        Args:
            amount (int): The amount to subtract
        Side effects:
            returns the score of the player
        """
        temp = self.score - amount
        self.score = temp
        return self.score


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
        
    def guess(self,df,player):
        """
        Is the guessing game
        
        Attributes:
            df (data frame): The data frame with information on the presidents
            player (user): Is a user object
        Side effects:
            Decreases score based on correct answer given.
        """
        
        print(f"Hello {player.name}. Welcome to the guessing game. The max number\
        of points you can get is 10 points. For every wrong answer 2 points will be subtracted. \
        Once you reach 0 you lose and the correct answer will be shown. Good luck!")

        ran = random.randint(1,46)
        president = df.iloc[ran]
        l = [1,3,4,7,8,9]

        while player.score >0:
            ran_col = random.choice(l)
            l.remove(ran_col)
            print(f"{df.columns[ran_col]}: {president.iloc[ran_col]}")
            guess = input("Who is the President?:")
            if guess.lower() == president.loc["Name of President"].lower():
                break
            else:
                player.sub_score(2)
            
        if player.get_score() > 0:
            print(f"Congrats! You guessed {president.iloc[0]} correctly and you won with a score of {player.get_score()}!")
        else:
            print(f"Sadly you lost! Better luck next time! The correct president was\
            {president.iloc[0]}")
        
    def compare(self,ser1,ser2):
        """
        Compares 2 presidents. For example compares year elected, party affiliation
        and so on. Also does a check to make sure the presidents chosen are properly
        spelled or exists.
    
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
        Keeps track of all the scores of all players who have ever played and
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
    
    scoreboard_file = open("ScoreBoard.txt","w+")
    df = pd.read_csv("Inst326_Presidents_Info.csv",index_col="Number President")
    
    print("Hello! Welcome to the game featuring all of the presidents of the United\
    States! We here at Presidents INC are happy you cam to play. Before we\
    get started please enter your full name and a name you would like to give\
    to the game your about to play.")
    
    name = input("Please enter your name: ")
    game_name = input("Please enter the name you wish to call this trial: ")
    game1 = Game(game_name)
    player = User(name,10)
    print("Now that you have entered the information. It is time for you to pick\
    the game you want to play. The first is a guessing game where information of a\
    random president will be given to you and you will have 3 guesses to guess\
    the correct president. The second option is an interactive expericen where\
    you will get to choose 2 presidents of the US and see how they differ. The third\
    choice is when you get to give the information fo a president and we guess\
    the president you are talking about.")
    
    game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3:")
    again = 1
    while int(game_choice) <= 0 or int(game_choice) > 3:
         game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3:")
    
    while again == 1:
        if int(game_choice) == 1:
            game1.guess(df,player)
            game1.score(player.score,player.name,scoreboard_file)
        elif int(game_choice) == 2:
            print("do work")
        elif int(game_choice) == 3:
            print("do work")
        again = input("Would you like to play again? Type 1 for yes or 0 for no: ")
    
    scoreboard_file.close()
    
    def score_board(file):
        """
        Prints out the leader of board
        Args:
            file (string): The file where all of the socres are kept.
        
        Returns:
            prints out the leader boards
        """        

def parse_args(arglist):
    """Parse command-line arguments.
    
    one arguments is expected: the path to a CSV file
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with attributes csv_file
    """
    parser = ArgumentParser()
    parser.add_argument("csv_file", help="path to life expectancy CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    main()
