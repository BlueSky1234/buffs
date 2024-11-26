'''
#Dbog max level buff tracker
#Legacy code
#MaxLevel = 550
#ML_stat = 2750
#Htc_Grav = 1650
#Mentor_stat = 37
#GC = 1000
#DB = 250
stat_buff = 0.014
lvl_buff = 0.007

MaxLevel = int(input("Level:"))
ML_stat = MaxLevel * 5
Htc_Grav = int(input("How much HTC and Grav:"))
Mentor_stat = int(input("How many mentors:"))
GC = int(input("How many Grand Kias:"))
DB = int(input("How many stat wishes:"))
DB *= 50
curr_max_statbuff = (ML_stat + Htc_Grav + Mentor_stat + GC + DB) * stat_buff

curr_max_lvlbuff = MaxLevel * lvl_buff

#Legacy code
#print("Current max stat buff:", curr_max_statbuff)
#print("Current max level buff:", curr_max_lvlbuff)

print("Your current stat buff:", curr_max_statbuff)
print("Your current level buff:", curr_max_lvlbuff)
'''

from datetime import datetime, timedelta
import pytz
import json

max_error = "You can't exceed the max"
max_level = 550
max_htc = 1100
max_gc = 550
max_db_wishes = 5
max_mentors = 37
max_grand_kai = 1986
level_buff = 0.007
stat_buff = 0.014

#Todays max grand kai points from 12 am UTC
max_grand_kai = 1000
#saving today to a file to be used to calculate the future Grand Kai max since it increases by 2 each day
def saved_time():
    utc_now = datetime.now(pytz.utc)
    midnight_utc = utc_now.replace(hour=0, minute=0, second=0, microsecond=0)
    #Save to file
    with open("saved_date.json", "w") as file:
        json.dump({"midnight_utc": midnight_utc.isoformat()}, file)
def load_saved_time(filename="saved_date.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        midnight_utc = datetime.fromisoformat(data["midnight_utc"]).replace(tzinfo=pytz.utc)
        return midnight_utc
    except FileNotFoundError:
        return None


saved_time_result = load_saved_time()
if saved_time_result is None:
    saved_time()
    saved_time_result = load_saved_time()
    
utc_now = datetime.now(pytz.utc)
today_midnight_utc = utc_now.replace(hour=0, minute=0, second=0, microsecond=0)
days_difference = (today_midnight_utc - saved_time_result).days

max_grand_kai += 2 * days_difference


def stat_buff_multiplier():
    #Get valid level
    print("What level are you?")
    current_level = int(input().strip())
                
    if current_level > max_level:
        print(max_error)
                
    else:
        level_points = current_level * 5
        #Get valid HTC points        
        print("How many points do you have from the Hyperbolic Time Chamber?")
        htc = int(input().strip())
        if htc > max_htc:
            print(max_error)
        else:
            #Get valid GC points
            print("How many points do you have from the Gravity Chamber?")
            gc = int(input().strip())
            if gc > max_gc:
                print(max_error)
            else:
                #Get valid wish points
                print("How many earth stat wishes have you made? 0-5")
                wishes = int(input().strip())
                if wishes > 5:
                    print(max_error)
                else:
                    wish_points = wishes * 50
                    #Get valid mentor points
                    print("How many mentors have you completed?")
                    mentors = int(input().strip())
                    if mentors > max_mentors:
                        print(max_error)
                    else:
                        #Get valid grand kai points
                        print("How much Grand Kai have you done")
                        grand_kai = int(input().strip())
                        if grand_kai > max_grand_kai:
                            print(max_error)
                        else:
                            total_stat_points = sum([level_points, htc, gc, wish_points, grand_kai])
                            print(f"Your current stat buff is: {total_stat_points * stat_buff}")

                        
def level_buff_multiplier():
    print("What level are you?")
    current_level = int(input().strip())
    if current_level > max_level:
        print("You cant exceed the max")
    else:
        print(f"Your current level buff is: {current_level * level_buff}")


def buff_calculator():
    calculating = True
    while calculating:
        try:
            print("""
                  1) Calculate Stat Buff
                  2) Calculate Level Buff
                  3) Quit""")
            choice = int(input().strip())
            if choice == 1:
                stat_buff_multiplier()
            elif choice == 2:
                level_buff_multiplier()
            elif choice == 3:
                print("Good bye!")
                calculating = False
            else:
                print("Use a valid number")
                 
        except ValueError:
            print("Please use a valid whole number")

buff_calculator()
