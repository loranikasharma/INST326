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
import csv


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
        self.leaders = {}
        
    def guess(self,df,player):
        """
        Is the guessing game
        
        Attributes:
            df (data frame): The data frame with information on the presidents
            player (user): Is a user object
        Side effects:
            Decreases score based on correct answer given.
        """
        
        print(("Hello ") + player.name + (". Welcome to the guessing game. The max number ") +
        ("of points you can get is 10 points. For every wrong answer 2 points will be subtracted.") +
        (" Once you reach 0 you lose and the correct answer will be shown. Good luck!"))

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
        
    def compare(self,president_one,president_two,file):
        """
        Compares 2 presidents. For example compares year elected, party affiliation
        and so on. Also does a check to make sure the presidents chosen are properly
        spelled or exists.
    
        Args:
            president_one(string): First president
            president_two(string): Second president
            file (String): path to the file
            
        Returns:
            The information regarding the presidents
        """
        df = pd.read_csv(file,index_col="Name of President") 
        while True:
            try:
                temp = ("Name of President: " + president_one + "\nNumber President: " + 
                    str(df.loc[president_one]["Number President"]) + "\nDate of Birth: " +
                    str(df.loc[president_one]["Date of Birth"]) + "\nState of Origin: " +
                    str(df.loc[president_one]["State of Origin"]) + "\nParty Affiliation: " +
                    str(df.loc[president_one]["Party Affiliation"]) + "\nVice President: " +
                    str(df.loc[president_one]["Vice President"]) + "\nFirst Lady: " + 
                    str(df.loc[president_one]["First Lady"]) + "\nNumber of Years Served: " +
                    str(df.loc[president_one]["Number of years served"]) + "\nNumber of Terms Served: "+
                    str(df.loc[president_one]["Number of terms served"]) + "\nOne Great Act: " +
                    str(df.loc[president_one]["One great act"]) + "\nDate of Death: " +
                    str(df.loc[president_one]["Date of death"]) + "\n" +
                    "\nName of President: " + president_two + "\nNumber President: " + 
                    str(df.loc[president_two]["Number President"]) + "\nDate of Birth: " +
                    str(df.loc[president_two]["Date of Birth"]) + "\nState of Origin: " +
                    str(df.loc[president_two]["State of Origin"]) + "\nParty Affiliation: " +
                    str(df.loc[president_two]["Party Affiliation"]) + "\nVice President: " +
                    str(df.loc[president_two]["Vice President"]) + "\nFirst Lady: " + 
                    str(df.loc[president_two]["First Lady"]) + "\nNumber of Years Served: " +
                    str(df.loc[president_two]["Number of years served"]) + "\nNumber of Terms Served: "+
                    str(df.loc[president_two]["Number of terms served"]) + "\nOne Great Act: " +
                    str(df.loc[president_two]["One great act"]) + "\nDate of Death: " +
                    str(df.loc[president_two]["Date of death"]))
                break
            except KeyError:
                pass
            print("One of the presidents is incorrect please re-enter both president names correcly")
            president_one = input("President 1: ")
            president_two = input("President 2: ")
        return temp    
    
    def questions(self, question,col,df):
        """
        Allows the user to provide information of a president, that the computer
        must guess
        
        Args:
            A question (user input response to question)
            a column from the dataframe
            the dataframe
        Side Effect:
            guesses a president based off of the information provided
        Returns:
            a president guess from the temp dataframe
        """
        answer_1 = input(question)
        temp = df[df[col] == answer_1]
        first_guess = temp["Name of President"].iloc[0]
        comp_guess_1 = input(f'Is {first_guess} the President you were thinking of?(yes or no): ')
        return comp_guess_1, temp
    
    def reverse(self,filepath):
        """
        Allows the user to put in information about a president and get the president
        name.
        
        Args:
            file(string):Path to the file
        Side Effect:
            Prints out the president the user is specifing
        Returns:
            None
        """
        question_col = [('What Party are they Affiliated with? (Please capitalize the first letter): ',"Party Affiliation","I think I have an idea.."),
                        ('Which state were they born in?(Two letter abriviation)',"State of Origin","I think I have my guess... but to be sure..."),
                        ('What is his date of birth (format MM-DD-YYYY)?: ',"Date of Birth","I'll try better next time. Good game!")]

        df2 = pd.read_csv(filepath)
        print("Welcome to game 3! I Will guess the President You're thinking of by the information you provide")
        
        for question, col, response in question_col:
            variable1, df2 = self.questions(question,col,df2)
            if variable1 == "yes":
                print('Good game!')
                return
            elif variable1 == "no":
                print (response)
                
    
     
    
    def score(self,player,file):
        """
        Keeps track of all the scores of all players who have ever played and
        updates the users specific score
        
        Attributes:
            file (string): Name of the file where the leader booard is kept
            player (User): A user object
        
        Side effects:
            Updates the users score on the leaderboards.
        """
        
        self.leaders[player.name] = player.get_score()
        with open("ScoreBoard.csv", "a") as leaderboard:
            writer = csv.writer(leaderboard)
            for key, value in self.leaders.items():
                writer.writerow([key, value])

        
        
def main():
    """
    In the main function the CSV file will be opened. The game instacne and the 
    user instance will be initiated. A file will be created where the users score
    will be tracked. This is also where all of the funcitons/methods will be ran.
    """
    def score_board(file):
        """
        Prints out the leader board
        Args:
            file (string): The file where all of the socres are kept.
        
        Returns:
            prints out the leader boards
        """
        with open(file,"r",encoding= "utf -8") as f:
            for line in f:
                print(line)  
    
    df = pd.read_csv("Inst326_Presidents_Info.csv",index_col="Number President")
    
    print(("Hello! Welcome to the game featuring all of the presidents ")+ 
      ("of the United States! We here at Presidents INC are happy ")+ 
      ("you came to play. Before we get started please enter your ")+
      ("full name and a name you would like to give to the game your about to play.\n"))
    
    name = input("Please enter your name: ")
    game_name = input("Please enter the name you wish to call this trial: ")
    game1 = Game(game_name)
    player = User(name,10)
    
    print(("Now that you have entered the information. It is time for you to pick ") +
    ("the game you want to play. The first is a guessing game where information of a ") +
    ("random president will be given to you and you will have 3 guesses to guess ") +
    ("the correct president. The second option is an interactive expericen where ") +
    ("you will get to choose 2 presidents of the US and see how they differ. The third ") +
    ("choice is when you get to give the information for a president and we guess ") +
    ("the president you are talking about.\n"))
    
    game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3:")
    again = 1
    
    while int(game_choice) <= 0 or int(game_choice) > 3:
         game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3:")
    
    while again == 1:
        if int(game_choice) == 1:
            player.score = 10
            game1.guess(df,player)
            game1.score(player,"ScoreBoard.txt")
        elif int(game_choice) == 2:
            pres1 = input("Enter the first and last name of the first president you want to compare:")
            pres2 = input("Enter the first and last name of the second president you want to compare:")
            print(game1.compare(pres1,pres2,"Inst326_Presidents_Info.csv"))
        elif int(game_choice) == 3:
            game1.reverse("Inst326_Presidents_Info.csv")
        again = input("Would you like to play again? Type 1 for yes or 0 for no: ")
        again = int(again)
        if again == 1:
            game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3:")
            game_choice = int(game_choice)
        
    score_board("ScoreBoard.csv")
       

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
