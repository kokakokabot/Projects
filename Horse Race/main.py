from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which horse will win the race? Enter a color: ")
colors= ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_horses = []

for horse_index in range(0, 6):
    new_horse = Turtle(shape="turtle")
    new_horse.color(colors[horse_index])
    new_horse.penup()
    new_horse.goto(x=-230, y=y_positions[horse_index])
    all_horses.append(new_horse)

if user_bet:
    is_race_on = True

while is_race_on:
    


    for horse in all_horses:
        if horse.xcor() > 230:
            is_race_on = False
            winning_color = horse.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} horse is the winner!")
            else:
                print(f"You've lost! The {winning_color} horse is the winner!")


        random_distance = random.randint(0, 10)
        horse.forward(random_distance)



screen.exitonclick()
