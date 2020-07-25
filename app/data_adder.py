import sqlite3
import sys
import datetime
import random
from helper_objects import rl_gamemode_list, rl_vehicle_list

def insert_data(username):
    # insert 20 rows of data each "one minute" apart
    seed_time = datetime.datetime.utcnow()
    time_list = []
    gamemode_list = []
    vehicle_list = []
    fov_list = []
    distance_list = []
    height_list = []
    angle_list = []

    for i in range(20):
        new_time = seed_time + datetime.timedelta(0, 60*i)
        str_time = new_time.strftime("%Y-%m-%d %H:%M:%S")
        time_list.append(str_time)

    username = sys.argv[1]
    
    game_result_list = ['win', 'loss', 'forfeit_win', 'forfeit_loss', 
                        'disconnect']
    
    topper_list = [0, 1]
    
    for item in rl_gamemode_list:
        gamemode_list.append(item[0])

    partied_list = [0, 1]

    team_list = ['orange', 'blue', 'club_colors']

    for item in rl_vehicle_list:
        vehicle_list.append(item[0])

    antenna_list = [0, 1]

    for i in range(60, 121):
        fov_list.append(i)

    for i in range(100, 401, 10):
        distance_list.append(i)

    for i in range(40, 200, 10):
        height_list.append(i)

    for i in range(-15, 1, 1):
        angle_list.append(i)

    notes_string = "This is a seed string from which the notes field will \
                    pick a handful of letters to populate the test db with."

    # Now with the lists populated, I want to select randomly from them and
    # insert into the database.
    conn = sqlite3.connect('rl_stats.db')
    for j in range(20):
        # this will iterate 20 times
        
        conn.execute("INSERT INTO game_data (date_time, username, game_result, \
                    topper, game_mode, partied, team, vehicle, antenna, fov, \
                    distance, height, angle, notes) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                    (time_list[j],
                    username,
                    random.choice(game_result_list),
                    random.choice(topper_list),
                    random.choice(gamemode_list),
                    random.choice(partied_list),
                    random.choice(team_list),
                    random.choice(vehicle_list),
                    random.choice(antenna_list),
                    random.choice(fov_list),
                    random.choice(distance_list),
                    random.choice(height_list),
                    random.choice(angle_list),
                    random.choice(notes_string)))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data(sys.argv[1])