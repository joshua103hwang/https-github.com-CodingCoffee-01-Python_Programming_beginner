cars = ["Ford", "Volvo", "BMW"]

#print(cars[0])
#print(cars[1])
#print(cars[2])
print(cars)
'''
for i in range(0,3):
    print(cars[i])

for i in cars:
    print(i)
'''
cars.append("Honda")
print(cars)
cars.pop(2)
print(cars)
cars.remove("Volvo")
print(cars)
