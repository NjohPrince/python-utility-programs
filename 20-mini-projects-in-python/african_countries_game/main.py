import turtle

import pandas

screen = turtle.Screen()
screen.title("African Countries Game")
image = "blank_africa_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("african_countries.csv")
countries = data.country.to_list()
number_of_countries = len(countries)
guessed_countries = set()
num_of_right_guesses = len(guessed_countries)

while num_of_right_guesses < number_of_countries:
    answer_country = screen.textinput(title=f"{num_of_right_guesses}/{number_of_countries} countries correct",
                                      prompt="What's another country's name?").title()

    if answer_country.lower() == "exit":
        missing_countries = [country for country in countries if country not in guessed_countries]
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        break
    if answer_country in countries:
        guessed_countries.add(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(float(country_data.x), float(country_data.y))
        t.write(f"{answer_country}", align="center")
        num_of_right_guesses = len(guessed_countries)
