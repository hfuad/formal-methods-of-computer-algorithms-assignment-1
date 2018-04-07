# Formal Methods of Computer Algorithms - Assignment 1
	Riham Nour  182031
	Hussam Fuad 161101
## Sample points
[(20, 20), (30, 50), (60, 70), (20, 30), (90, 5)]
### display for n= 5
#### 1)Using brute-force approach, design an algorithm to find the post-office location minimizing the average distance between the villages and the post office.
	min distance: 3 	value: 40.81489150162855

#### 2)Using brute-force approach, design an algorithm to find the post-office location minimizing the maximum distance from a village to the post office.
	minimize max: 0 	value: 71.58910531638176

#### 4)Analyze your designed algorithms mathematically and empirically.
	Empirical Analysis : complexity O(log n**2)
	numerical Analysis : 
		n= 5
		iterations= 20
		calculation n**2= 25
		actual  n*(n-1)= 20

-------------------
### display for n= 100
#### 1)Using brute-force approach, design an algorithm to find the post-office location minimizing the average distance between the villages and the post office.
	min distance: 71 	value: 18.180936886500835

#### 2)Using brute-force approach, design an algorithm to find the post-office location minimizing the maximum distance from a village to the post office.
	minimize max: 32 	value: 34.48187929913333

#### 4)Analyze your designed algorithms mathematically and empirically.
	Empirical Analysis : complexity O(log n**2)
	numerical Analysis : 
		n= 100
		iterations= 9900
		calculation n**2= 10000
		actual  n*(n-1)= 9900

-------------------
