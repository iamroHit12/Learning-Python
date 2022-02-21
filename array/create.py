from array import array
import random

valuelist = array("d",[100])

for i in range(len(valuelist)):
    valuelist[i] = random.random()

for value in valuelist:
    print(value)