from turtle import Turtle, Screen
import time
import random


# TODO: 1) Create a starting screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.register_shape('images/spa.gif')
screen.register_shape('images/missile.gif')
screen.register_shape('images/asteroid_1.gif')
screen.register_shape('images/asteroid_2.gif')
screen.register_shape('images/asteroid_3.gif')
screen.register_shape('images/boom.gif')


# TODO: 2) Create the player space-ship
spaceship = Turtle()
spaceship.penup()
spaceship.shape('images/spa.gif')
spaceship.setheading(0)
screen.tracer(0)
spaceship.goto(x=0, y=-260)


# TODO: 3) Move the spaceship
def move_left():
    if -280 < spaceship.xcor():
        spaceship.backward(5)


def move_right():
    if 280 > spaceship.xcor():
        spaceship.forward(5)


screen.listen()
screen.onkeypress(fun=move_left, key='Left')
screen.onkeypress(fun=move_right, key='Right')
screen.onkey(fun=screen.bye, key='q')


# TODO: 5) Make the spaceship shoot missiles
game_is_on = True
missile_list = []
asteroid_list = []
asteroid_shapes = ['images/asteroid_1.gif', 'images/asteroid_2.gif', 'images/asteroid_3.gif']
counter = 1

while game_is_on:
    time.sleep(0.01)
    screen.update()

    if counter % 30 == 0:
        missile = Turtle()
        missile.shape('images/missile.gif')
        missile.penup()
        missile.color('white')
        missile.setheading(90)
        missile.speed('slowest')
        missile.goto(x=spaceship.xcor(), y=spaceship.ycor() + 20)
        missile_list.append(missile)

    for a in missile_list:
        a.forward(2)
        if a.ycor() > 310:
            a.hideturtle()
            del a

    counter += 1

    # TODO: 4) Generate random asteroids
    if counter % 100 == 0:
        asteroid = Turtle()
        asteroid.penup()
        asteroid.setheading(270)
        asteroid.speed('slowest')
        asteroid.shape(random.choice(asteroid_shapes))
        asteroid.goto(x=random.randint(-260, 260), y=310)
        asteroid_list.append(asteroid)

    for item in asteroid_list:
        item.forward(0.20)

        for projectile in missile_list:
            if item.distance(projectile) < 22:
                asteroid_list.remove(item)
                missile_list.remove(projectile)
                item.hideturtle()
                item.color('white')
                item.write(arg='KABOOM!', move=False, font=('chiller', 14, 'bold'))
                screen.ontimer(item.clear, 300)

                projectile.shape('images/boom.gif')
                screen.ontimer(projectile.hideturtle, 400)


        if item.ycor() < -300:
            game_is_on = False



screen.exitonclick()
