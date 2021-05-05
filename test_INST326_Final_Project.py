import INST326_Final_Project as pro
import pytest
import builtins
from unittest import mock
import pandas as pd

def test_guess():
    """
    Tests to make sure that the guess function works, that the user score is reduced
    and that the dataframe works.
    """
    player = pro.User("Chris",10)
    game = pro.Game("Trial 1")
    df = pd.read_csv("Inst326_Presidents_Info.csv",index_col="Number President")

    with mock.patch("builtins.input", side_effects=["Kevin Gates","Chris Brown", 
                                    "Brad Pitt", "Antonio Gibson","Will Smith"]):
        game.guess(df,player)
        assert player.get_score() == 0
    assert df.iloc[0]["Name of President"] == "George Washington"
    assert df.iloc[0]["State of Origin"] == "VA"
    assert df.iloc[45]["State of Origin"] == "DE"
    assert df.iloc[45]["Name of President"] == "Joseph Biden"
    assert df.iloc[45]["Vice President"] == "Kamala Harris"
    assert df.iloc[18]["Name of President"] == "Rutherford Hayes"

def test_compare():
    """
    Tests the compare method to make sure that the out put is correct
    """
    game = pro.Game("Trial 1")
    df = pd.read_csv("Inst326_Presidents_Info.csv",index_col="Name of President")
    president_one = "George Washington"
    president_two = "John Adams"
    temp = game.compare("George Washington","John Adams","Inst326_Presidents_Info.csv")
    assert temp == ("Name of President: " + president_one + "\nNumber President: " + 
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
    
# def test_reverse():
#     """Tests the reverse method to make sure the output is correct and edge cases have proper error messages
#     """
#     with mock.patch("builtins.input", side_effects= ['Christian','Chris','Jay','Loranika']):
#         #happy cases
#         assert pro.reverse("Democrat", "NJ", "03-18-1837") == "Grover Cleveland" 
#         assert pro.reverse('Democrat', "PA", "04-23-1791") == "James Buchanan" 
#         assert pro.reverse('Republican', "OH", "04-27-1822") == "Ulysses Grant" 
#         assert pro.reverse('Democrat', "MO", "05-08-1884") == "Harry Truman" 
#         assert pro.reverse('Republican', "CA", "01-09-1913") == "Richard Nixon" 
#         #assert pro.reverse('Republican', "TX", "07-06-1946") == "George W. Bush"
#         assert pro.reverse('Republican', 'OH', "08-20-1833") == "Benjamin Harrison" 
#         #edge cases
#         assert pro.reverse("Democrat", "NJ", "03-18-1837") == "grover cleveland" 
#         assert pro.reverse('Democrat', "MO", "05-08-1884") == "harry truman" 
#         assert pro.reverse('Republican', "TX", "07-06-1946") == "George W. Bush" or "George Bush" or "george w. bush"

def test_get_score():
    player = pro.User("Jay",10)
    assert player.get_score() == 10
    player = pro.User("James",8)
    assert player.get_score() == 8
    player = pro.User("Justin",5)
    assert player.get_score() == 5
    player = pro.User("Julien",50)
    assert player.get_score() == 50
    player = pro.User("Eric",12)
    assert player.get_score() == 12
    player = pro.User("Milton",0)
    assert player.get_score() == 0
    player = pro.User("Guy",9)
    assert player.get_score() == 9
    player = pro.User("Kennedy",20)
    assert player.get_score() == 20
    player = pro.User("Tom",2)
    assert player.get_score() == 2
    player = pro.User("Ken",6)
    assert player.get_score() == 6

