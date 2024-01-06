import pandas as pd
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('CarBot')

trainer = ListTrainer(chatbot)

df = pd.read_csv('data.csv')

conversations = []

for index, row in df.iterrows():
    make = row['Make']
    model = row['Model']
    year = row['Year']
    horsepower = row['Horsepower']
    torque = row['Torque']
    fuel_efficiency = row['Fuel Efficiency']
    safety_rating = row['Safety Rating']
    price = row['Price']

    # سوالات بسته به سازنده
    trainer.train([
        f'What is the model of the {make}?',
        f'The model of the {make} is {model}.',
    ])
    trainer.train([
        f'What is the year of the {make}?',
        f'The year of the {make} is {year}.',
    ])
    trainer.train([
        f'What is the horsepower of the {make}?',
        f'The horsepower of the {make} is {horsepower}.',
    ])
    trainer.train([
        f'What is the torque of the {make}?',
        f'The torque of the {make} is {torque}.',
    ])
    trainer.train([
        f'What is the fuel efficiency of the {make}?',
        f'The fuel efficiency of the {make} is {fuel_efficiency}.',
    ])
    trainer.train([
        f'What is the safety rating of the {make}?',
        f'The safety rating of the {make} is {safety_rating}.',
    ])
    trainer.train([
        f'What is the price of the {make}?',
        f'The price of the {make} is {price}.',
    ])
    trainer.train([
        f'Can you tell me about the {make}?',
        f'The {make} is a {year} model with {horsepower} horsepower and {torque} torque. It has a fuel efficiency of {
            fuel_efficiency} and a safety rating of {safety_rating}. It costs {price}.',
    ])


# موارد مقایسه‌ای
top_horsepower_car = df.loc[df['Horsepower'].idxmax()]
trainer.train([
    'Which car has the highest horsepower?',
    f'The {top_horsepower_car["Make"]} has the highest horsepower with {
        top_horsepower_car["Horsepower"]} horsepower.',
])

top_fuel_efficiency_car = df.loc[df['Fuel Efficiency'].idxmax()]
trainer.train([
    'Which car has the best fuel efficiency?',
    f'The {top_fuel_efficiency_car["Make"]} has the best fuel efficiency with {
        top_fuel_efficiency_car["Fuel Efficiency"]}.',
])

trainer.train(conversations)

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        break

    response = chatbot.get_response(user_input)
    print(f"CarBot: {response}")
