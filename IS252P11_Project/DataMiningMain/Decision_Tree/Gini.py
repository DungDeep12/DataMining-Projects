import pandas as pd
from chefboost import Chefboost as chef
from chefboost.training import Training

df = pd.read_csv('modified_test.csv')
config = {'algorithm': 'CART'}
df

model = chef.fit(df, config, target_label = 'satisfaction')

df.rename(columns={'satisfaction': 'Decision'}, inplace=True)
Gini_indexs = Training.findGains(df, config)
print(Gini_indexs)

#predict customer satisfaction with new instance
print(chef.predict(model, param = ['Female','disloyal Customer',24,'Business travel','Eco',451,3,0,3,2,5,3,5,5,3,5,4,2,1,5,0,0]))

print(chef.predict(model, param = ['Male','Loyal Customer',50,'Business travel','Business',1525,5,5,2,5,4,5,4,5,5,5,5,4,5,5,2,11]))

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