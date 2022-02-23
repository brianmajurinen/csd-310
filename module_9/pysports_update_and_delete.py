#Brian Majurinen
#Bellevue University
#CYBR410-H331
import mysql.connector
from mysql.connector import errorcode
#Issues adding a user, so went with root
config = {
    "user": "root",
    "password": "!M!ysql123",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):
    """ method to execute an inner join on the player and team table, 
        iterate over the dataset and output the results to the terminal window.
    """

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    # get the cursor object
    cursor = db.cursor()

    # insert player query 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # player data fields 
    player_data = ("Smeagol", "Shire Folk", 1)

    # insert a new player record
    cursor.execute(add_player, player_data)

    # commit the insert to the database 
    db.commit()

    # show all records in the player table 
    show_players(cursor, "Players List")

    # update the newly inserted record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # execute the update query
    cursor.execute(update_player)

    # show all records in the player table 
    show_players(cursor, "Gollum Added")

    # delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    # show all records in the player table 
    show_players(cursor, "Gollum Deleted")

    input("\n\n  Press any key to continue... ")

#Didn't use the error codes here

finally:    
    db.close()
