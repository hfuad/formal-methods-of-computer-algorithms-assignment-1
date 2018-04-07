import math
import random
import time

print("# Formal Methods of Computer Algorithms - Assignment 1")
print("\tRiham Nour  182031")
print("\tHussam Fuad 161101")


# prepare random points
vlist = [(20, 20), (30, 50), (60, 70), (20, 30), (90, 5)]

print("## Sample points")
print(vlist)


# distance calc
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def display(vlist, minimum_index, minimum_Distance, minimize_max_distance_index, minimize_max_distance, iterations):
    print("### display for n=",len(vlist))
    print("#### 1) Using brute-force approach, design an algorithm to find the post-office location "
          "minimizing the average distance between the villages and the post office.")
    print("\tmin distance:", minimum_index, "\tvalue:", minimum_Distance)
    print("")
    print("#### 2) Using brute-force approach, design an algorithm to find the post-office location "
          "minimizing the maximum distance from a village to the post office.")
    print("\tminimize max:", minimize_max_distance_index, "\tvalue:", minimize_max_distance)
    print("")
    print("#### 4) Analyze your designed algorithms mathematically and empirically.")
    print("\tEmpirical Analysis : complexity O(log n**2)")
    print("\tnumerical Analysis : ")
    print("\t\tn=", len(vlist))
    print("\t\titerations=", iterations)
    print("\t\tcalculation n**2=", (len(vlist))**2)
    print("\t\tactual  n*(n-1)=", len(vlist)*(len(vlist)-1))
    print("")
    print("-------------------")


# brute force
def brute_force(vlist, enableLogging, minAverage, minimizeMax):
    minimum_Distance = 999
    minimum_index = -1
    iterations = 0
    minimize_max_distance = 999
    minimize_max_distance_index = 999

    for i in range(0, len(vlist)):
        summation = avg = count = 0
        local_maximum = -999
        for y in range(0, len(vlist)):
            if i != y:
                iterations += 1
                dist = euclidean_distance(vlist[i], vlist[y])
                if minAverage:
                    count += 1
                    summation += dist
                if minimizeMax:
                    if dist > local_maximum:
                        local_maximum = dist
                if enableLogging:
                    print("\t", i, ":", y, "\t", dist)
        if minAverage:
            avg = summation/count
            if avg < minimum_Distance:
                minimum_Distance = avg
                minimum_index = i
            if enableLogging:
                print("avg:", i, ":", avg)
        if minimizeMax:
            if local_maximum<minimize_max_distance:
                minimize_max_distance = local_maximum
                minimize_max_distance_index = i
    return minimum_index,  minimum_Distance, minimize_max_distance_index, minimize_max_distance, iterations

minimum_index,  minimum_Distance, minimize_max_distance_index, minimize_max_distance, iterations = brute_force(vlist, False, True, True)

display(vlist, minimum_index,  minimum_Distance, minimize_max_distance_index, minimize_max_distance, iterations)

# Generate 1000 random points
vlist = []
for i in range(1000):
    point = (random.randint(1, 50), random.randint(1, 50))
    vlist.append(point)

minimum_index,  minimum_Distance, minimize_max_distance_index, minimize_max_distance, iterations = brute_force(vlist, False, True, True)
display(vlist, minimum_index,  minimum_Distance, minimize_max_distance_index, minimize_max_distance, iterations)

print("#### 5)i)Which minimization is more suitable for this application, average or maximum distance and why? ")
print("maximum distance is more suitable since the best location for the post office is the one were it "
      "minimizes distance from the farthest village")
print("#### 5)ii)And which is faster to execute?")
print("since both have the same complexity maximum distance will be faster since it "
      "does not calculate and average before choosing the minimum distance")

# Generate 1000 random points
vlist = []
for i in range(1000):
    point = (random.randint(1, 50), random.randint(1, 50))
    vlist.append(point)
print("##### time for minAverage over 100000 ")
start = time.clock()
brute_force(vlist, False, True, False)
print(time.clock() - start)

print("##### time for minimizeMaximum over 100000 ")
start = time.clock()
brute_force(vlist, False, False, True)
print(time.clock() - start)

