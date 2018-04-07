# Formal Methods of Computer Algorithms - Assignment 1
	Riham Nour  182031
	Hussam Fuad 161101
## Sample points
[(20, 20), (30, 50), (60, 70), (20, 30), (90, 5)]
### display for n= 5
#### 1) Using brute-force approach, design an algorithm to find the post-office location minimizing the average distance between the villages and the post office.
	min distance: 3 	value: 40.81489150162855

#### 2) Using brute-force approach, design an algorithm to find the post-office location minimizing the maximum distance from a village to the post office.
	minimize max: 0 	value: 71.58910531638176

#### 4) Analyze your designed algorithms mathematically and empirically.
	Empirical Analysis : complexity O(log n**2)
	numerical Analysis : 
		n= 5
		iterations= 20
		calculation n**2= 25
		actual  n*(n-1)= 20

-------------------
### display for n= 1000
#### 1) Using brute-force approach, design an algorithm to find the post-office location minimizing the average distance between the villages and the post office.
	min distance: 33 	value: 18.809185851542445

#### 2) Using brute-force approach, design an algorithm to find the post-office location minimizing the maximum distance from a village to the post office.
	minimize max: 33 	value: 33.97057550292606

#### 4) Analyze your designed algorithms mathematically and empirically.
	Empirical Analysis : complexity O(log n**2)
	numerical Analysis : 
		n= 1000
		iterations= 999000
		calculation n**2= 1000000
		actual  n*(n-1)= 999000

-------------------
#### 5)i)Which minimization is more suitable for this application, average or maximum distance and why? 
maximum distance is more suitable since the best location for the post office is the one were it minimizes distance from the farthest village
#### 5)ii)And which is faster to execute?
since both have the same complexity maximum distance will be faster since it does not calculate and average before choosing the minimum distance
time for minAverage over 100000 
1.3433499989999997
time for minimizeMaximum over 100000 
1.248110418