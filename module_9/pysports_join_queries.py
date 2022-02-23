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

try: 
    #connecting to pysports, this is mostly the code from the course github
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    cursor.execute("SELECT team_id, team_name, mascot FROM team")
 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # iterate over the teams data set and display the results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # iterate over the players data set and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

#Didn't use the error codes here

finally:    
    db.close()
