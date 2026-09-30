# pip install numpy

import numpy as np 

# print("=== creeat array ===")
# arr = np.array([10,20,30,40, 50, 60 ])
# print(arr)
# print(arr[0:1])
# print(arr+10)


# print("==data cleaning example ")
# data = np.array([20, 10, -30, -45 ])
# clean =data [data>=0]
# print ("cleaned : ", clean)


cities = np.array(["helhi", "Mumbi ", "rajstan", "lacknoW"])
cities =np.char.strip(cities)
cities = np.char.title(cities)
print(cities)