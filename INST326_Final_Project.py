# Group: Christian Thompson, Loranika Sharma, Christopher Marroquin, Jay Patel
# INST326
# Final Project

#pandas
#if statements
import pandas as pd

df = pd.read_csv("INST326 FINAL_Presidents.csv")
print df

class User:
    """
    This class keeps track of the users attempts, name and score
    
    Attributes:
        name(String): Name of user
        attempts(int): Number of attempts
        score(int): The score of the user
    """
    def __init__(self,name):
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
    
    def __init__(self,name):
        """
       Initializes the name of the game.
        Args:
            name(String): Name of game
        
        Side effects:
            Initializes values
        """
        
    def guess(self,ser,player):
    """
    Is the guessing game
    
    Attributes:
        ser(series): A column from the file
        player (user): Is a user object
    Side effects:
        Increases score based on answer given.
    """
        
        
    def compare(self,ser1,ser2):
        """
        This class keeps track of the users attempts, name and score
    
        Attributes:
            ser1(series): Name of user
            der2(series): Number of attempts
        Side effects:
            Prints out information regarding the presidents
        """
        
    def reverse(self,data_frame):
        """
        Allows the user to put in information about a president and get the president
        name.
        
        Attributes:
            data_frame(data frame):The data frame consisting of all the presidents 
        Side effects:
            Prints out the president the user is specifing
        """
    
    def score(self,score,name):
        """
        Keeps track of all the scores of all players who haver ever played and
        updates the users specific score
        
        Attributes:
            name (string)
            score (int)
        
        Side effects:
            prints out the score of everyone who has played.
        """
        
def main():
    """
    In the main function the CSV file will be opened. The game instacne and the 
    user instance will be initiated. A file will be created where the users score
    will be tracked. This is also where all of the funcitons/methods will be ran.
    """
