import pandas as pd
from chefboost import Chefboost as chef
from chefboost.training import Training

df = pd.read_csv('modified_test.csv')
config = {'algorithm': 'ID3'}

model = chef.fit(df, config, target_label = 'satisfaction')

# predict customer satisfaction with new instance
print("\ncustomer satisfaction:")
print(chef.predict(model, param = ['Male','Loyal Customer',44,'Business travel','Business',386,5,5,5,5,2,4,4,4,4,4,4,3,4,3,17,18]))

print("\ncustomer satisfaction:")
print(chef.predict(model, param = ['Female','Loyal Customer',40,'Business travel','Business',2917,2,4,4,4,2,2,3,2,2,2,2,3,2,2,0,0]))

# User input Data
param = [
    input("Nhập Gender (Male/Female): "),
    input("Nhập Customer Type (Loyal Customer/Disloyal Customer): "),
    int(input("Nhập Age: ")),
    input("Nhập Type of Travel (Business travel/Personal Travel): "),
    input("Nhập Class (Eco/Eco Plus/Business): "),
    int(input("Nhập Flight Distance: ")),
    int(input("Nhập Inflight wifi service (1-5): ")),
    int(input("Nhập Departure/Arrival time convenient (1-5): ")),
    int(input("Nhập Ease of Online booking (1-5): ")),
    int(input("Nhập Gate location (1-5): ")),
    int(input("Nhập Food and drink (1-5): ")),
    int(input("Nhập Online boarding (1-5): ")),
    int(input("Nhập Seat comfort (1-5): ")),
    int(input("Nhập Inflight entertainment (1-5): ")),
    int(input("Nhập On-board service (1-5): ")),
    int(input("Nhập Leg room service (1-5): ")),
    int(input("Nhập Baggage handling (1-5): ")),
    int(input("Nhập Checkin service (1-5): ")),
    int(input("Nhập Inflight service (1-5): ")),
    int(input("Nhập Cleanliness (1-5): ")),
    int(input("Nhập Departure Delay in Minutes: ")),
    int(input("Nhập Arrival Delay in Minutes: "))
]

# predict customer satisfaction with the input
prediction = chef.predict(model, param=param)

print("\ncustomer satisfaction:")
print(prediction)