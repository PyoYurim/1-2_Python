alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'red', 'points' : 15}
alien_2 = {'color' : 'blue', 'points' : 20}

aliens = [alien_0, alien_1, alien_2]

for idx, alien in enumerate (aliens) :
    print(f"{idx+1}번 외계인의 색상 : {alien['color'].capitalize()}")
