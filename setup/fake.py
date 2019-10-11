import pandas as pd
import random
items = []
prices = []
noOfItems = int(input())
for i in range(noOfItems):
    items.append(input())
    prices.append(input())

# items = ["Dell Inspiron", "Alienware", "AIO PC", "Dell Workstation", "Widescreen Monitor", "Mouse", "Ergonomic Keyboard"]
# prices = [40000, 100000, 60000,100000, 10000,500,600]

data = {'Item': [], 'Rating': [], 'Prices': []}
for row in range(1000):
    itemIndex = random.randint(0, len(items) - 1)
    item = items[itemIndex]
    data['Item'].append(item)
    rating = random.randint(0, 5)
    data['Rating'].append(rating)
    data['Prices'].append(prices[itemIndex])
# print(data)
df = pd.DataFrame(data=data)
df.to_csv('dataset.csv')
print(df)