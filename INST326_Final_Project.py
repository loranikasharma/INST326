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
            print(f"Sadly you lost! Better luck next time! The correct president was {president.iloc[0]}")
        
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
            Prints out information regarding the presidents
        """
        
        df = pd.read_csv(file,index_col="Name of President")
        
        #while president_one not in df.values:
                #president_one = input("Please enter a valid president for your first option:")
        #while president_two not in df.values:
                #president_two = input("Please enter a valid president for your second option:")
            
        print("Name of President: " + president_one + "\nNumber President: " + 
            str(df.loc[president_one]["Number President"]) + "\nDate of Birth: " +
            str(df.loc[president_one]["Date of Birth"]) + "\nState of Origin: " +
            str(df.loc[president_one]["State of Origin"]) + "\nParty Affiliation: " +
            str(df.loc[president_one]["Party Affiliation"]) + "\nVice President: " +
            str(df.loc[president_one]["Vice President"]) + "\nFirst Lady: " + 
            str(df.loc[president_one]["First Lady"]) + "\nNumber of Years Served: " +
            str(df.loc[president_one]["Number of years served"]) + "\nNumber of Terms Served: "+
            str(df.loc[president_one]["Number of terms served"]) + "\nOne Great Act: " +
            str(df.loc[president_one]["One great act"]) + "\nDate of Death: " +
            str(df.loc[president_one]["Date of death"]) + "\n")

        print("Name of President: " + president_two + "\nNumber President: " + 
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
            
        
    def reverse(self,df2):
        """
        Allows the user to put in information about a president and get the president
        name.
        
        Args:
            file(string):Path to the file
        Returns:
            Prints out the president the user is specifing
        """
        df2 = pd.read_csv("Inst326_Presidents_Info.csv")
        president_name = df2["Name of President"]
        vice_president_name = df2["Vice President"]
        #president_number = df2["Number President"]
        #one_great_act = df2["One great act"]
    
        print("Welcome to game 3! Please provide information for the president you are thinking of, and I will try to guess the president")
        first_letter = input("What does his first name start with?: ")
        print("I see... Let me think of another question")
        vice_first_letter = input("What does his vice president's first name start with?: ")
        print("I think I have my guess... but to be sure...")
        president_birthyear = input("Which year was he born? (format MM-DD-YYYY)?: ")
        
        if president_birthyear in df2.values:
            print(f' Was {df2[df2["Date of Birth"] == date]["Name of President"]} the president you were thinking of?')
        else:
            print("Can I try again?")
        #if first_letter in president_name:
            #print(f' Was {president_name} the president you were thinking of?')
        #else:
            #print("Can I try again?")
        #if vice_first_letter in vice_president_name:
            #print(f' Was {president_name} the president you were thinking of?')
    
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
        #with open("ScoreBoard.csv", "w", newline ='') as leaderboard:
         #   scores = ['Name', 'Score']
          #  add_scores = csv.DictWriter(leaderboard, fieldnames=scores)
           # add_scores.writerow({'Name' : name, 'Score' : score})
            #print(add_scores)
        self.leaders[player.name] = player.get_score()
        #self.leaders['Score'] = score   
        with open("ScoreBoard.csv", "a") as leaderboard:
            writer = csv.writer(leaderboard)
            for key, value in self.leaders.items():
                writer.writerow([key, value])
            #scores = ['Name', 'Score']

            #add_scores = csv.DictWriter(self.leaders, fieldnames=scores)
            #writerow(self.leaders)
            #print(add_scores)
        #df = pd.read_csv(file)
        #df_sort = df.sort(['Score'], ascending=[1, 0])
        #scoreboard_addition = {name : score}
        
        #scoreboard_file = open(file,"w+")
        #scoreboard_file.write(f"{player.name}: {player.get_score()}")
        #scoreboard_file.close()
        
def main():
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
    
    
    """
    In the main function the CSV file will be opened. The game instacne and the 
    user instance will be initiated. A file will be created where the users score
    will be tracked. This is also where all of the funcitons/methods will be ran.
    """
    
    #scoreboard_file = open("ScoreBoard.csv","w+")
    #scoreboard_file = open("ScoreBoard.txt","w+")
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
    ("choice is when you get to give the information fo a president and we guess ") +
    ("the president you are talking about.\n"))
    
    game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3:")
    again = 1
    while int(game_choice) <= 0 or int(game_choice) > 3:
         game_choice = input("Please type 1 for option 1, 2 for option 2 or 3 for option 3:")
    
    while again == 1:
        if int(game_choice) == 1:
            game1.guess(df,player)
            game1.score(player,"ScoreBoard.csv")
        elif int(game_choice) == 2:
            pres1 = input("Enter the first and last name of the first president you want to compare:")
            pres2 = input("Enter the first and last name of the second president you want to compare:")
            while pres1 not in df.values:
                pres1 = input("Please enter a valid president for your first option:")
            while pres2 not in df.values:
                pres2 = input("Please enter a valid president for your second option:")
            game1.compare(pres1,pres2,"Inst326_Presidents_Info.csv")
        elif int(game_choice) == 3:
            game1.reverse("Inst326_Presidents_Info.csv")
        again = input("Would you like to play again? Type 1 for yes or 0 for no: ")
    
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
