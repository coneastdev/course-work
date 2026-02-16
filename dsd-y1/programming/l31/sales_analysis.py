import numpy as np

weeklySalesData = np.array([120, 135, 150, 98, 175, 200, 143])

print(weeklySalesData)

print(f"the mean is: {weeklySalesData.mean()}")
print(f"the total is: {weeklySalesData.sum()}")
print(f"the max value is: {weeklySalesData.max()}")
print(f"the min value is: {weeklySalesData.min()}")

weeklySalesData = weeklySalesData * 1.10

print(weeklySalesData)

randArray = np.array(np.random.randint(0, 100, 100))
print(randArray)