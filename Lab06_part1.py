"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
import datetime
from datetime import date
player = ['rooney','ronaldo','torres']
a = [date(2012,06,23)]
b = [date(2012,06,25)]
c = [date(2012,06,19)]
d = [date(2012,06,20)]
e = [date(2012,06,21)]
player_stats = {'rooney' : [(a,2),(b,2)],
                'ronaldo' : [(c,0),(d,3)],
                'torres' : [(e,0),(e,1)]
               }
print player_stats[player[0]][1][1]

#### implement highest_score
theMax = 0
num = 0
count = 0
count2 = 0
for player in player_stats:
    while count < 3:
        num = player_stats[player[count]][count2][1]
        if num > theMax:
            theMax = num
            count += 1
            count2 += 1
            break
print 'The highest score is ',theMax


## implement highest_score
##num = 0
##for name in player_stats:
##    print player_stats[


## implement highest_score_for_player



## implement highest_scorer
