import math
import random

# Formal Methods of Computer Algorithms - Assignment 1
# Riham Nour
# Hussam Fuad 161101


# prepare random points
vList = [
        (20, 20),
        (30, 50),
        (60, 70),
        (20, 30),
        (90, 5)
        ]
print(vList)


# distance calc
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


# brute force
def brute_force(vlist, enableLogging):
    minimum_Distance = 999
    minimum_index = maximum_index = -1
    iterations = 0
    maximum_Distance = -999
    for i in range(0, len(vList)):
        summation = avg = count = 0
        for y in range(0, len(vList)):
            if i != y:
                dist = euclidean_distance(vList[i], vList[y])
                count += 1
                summation += dist
                iterations += 1
                if enableLogging:
                    print("\t", i, ":", y, "\t", dist)
        avg = summation/count
        if enableLogging:
            print("avg:", i, ":", avg)
            print("")
        if avg < minimum_Distance:
            minimum_Distance = avg
            minimum_index = i
        if avg > maximum_Distance:
            maximum_Distance = avg
            maximum_index = i
    return minimum_index, maximum_index, minimum_Distance, maximum_Distance, iterations

minimum_index, maximum_index, minimum_Distance, maximum_Distance, iterations = brute_force(vList, True)

print("-------------------")
print("min distance:", minimum_index, "\tvalue:", minimum_Distance)
print("max distance:", maximum_index, "\tvalue:", maximum_Distance)
print("-------------------")
print("complexity O(log n**2)")
print("numerical complexity:")
print("n=", len(vList))
print("iterations=", iterations)
print("calculation n**2=", (len(vList))**2)
print("actual  n*(n-1)=", len(vList)*(len(vList)-1))

print("######################")
print("#rerun for 100 random points")
print("######################")

# Generate 1000 random points
vList = []
for i in range(100):
    point = (random.randint(1,50),random.randint(1,50))
    vList.append(point)

minimum_index, maximum_index, minimum_Distance, maximum_Distance, iterations = brute_force(vList, False)

print("-------------------")
print("min distance:", minimum_index, "\tvalue:", minimum_Distance)
print("max distance:", maximum_index, "\tvalue:", maximum_Distance)
print("-------------------")
print("complexity O(log n**2)")
print("numerical complexity:")
print("n=", len(vList))
print("iterations=", iterations)
print("calculation n**2=", (len(vList))**2)
print("actual  n*(n-1)=", len(vList)*(len(vList)-1))

