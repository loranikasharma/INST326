import INST326_Final_Project as pro
import pytest
import builtins
from unittest import mock
import pandas as pd

def test_guess():
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

def test_compare(capsys):
    game = pro.Game("Trial 1")
    df = pd.read_csv("Inst326_Presidents_Info.csv",index_col="Name of President")
    president_one = "George Washington"
    president_two = "John Adams"
    game.compare("George Washington","John Adams","Inst326_Presidents_Info.csv")
    outerr = capsys.readouterr()
    out = outerr.out
    assert out == ("Name of President: " + president_one + "\nNumber President: " + 
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