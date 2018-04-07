# Formal Methods of Computer Algorithms - Assignment 1
	Riham Nour  182031
	Hussam Fuad 161101
	 0 : 1 	 31.622776601683793
	 0 : 2 	 64.03124237432849
	 0 : 3 	 10.0
	 0 : 4 	 71.58910531638176
avg: 0 : 44.31078107309851

	 1 : 0 	 31.622776601683793
	 1 : 2 	 36.05551275463989
	 1 : 3 	 22.360679774997898
	 1 : 4 	 75.0
avg: 1 : 41.259742282830395

	 2 : 0 	 64.03124237432849
	 2 : 1 	 36.05551275463989
	 2 : 3 	 56.568542494923804
	 2 : 4 	 71.58910531638176
avg: 2 : 57.061100735068486

	 3 : 0 	 10.0
	 3 : 1 	 22.360679774997898
	 3 : 2 	 56.568542494923804
	 3 : 4 	 74.33034373659252
avg: 3 : 40.81489150162855

	 4 : 0 	 71.58910531638176
	 4 : 1 	 75.0
	 4 : 2 	 71.58910531638176
	 4 : 3 	 74.33034373659252
avg: 4 : 73.12713859233901

## display for n= 5
### 1)Using brute-force approach, design an algorithm to find the post-office location minimizing the average distance between the villages and the post office.
	min distance: 3 	value: 40.81489150162855

### 2)Using brute-force approach, design an algorithm to find the post-office location minimizing the maximum distance from a village to the post office.
	minimize max: 0 	value: 71.58910531638176

### 4)Analyze your designed algorithms mathematically and empirically.
	Empirical Analysis : complexity O(log n**2)
	numerical Analysis : 
		n= 5
		iterations= 20
		calculation n**2= 25
		actual  n*(n-1)= 20

-------------------
# rerun for 100 random points
## display for n= 100
### 1)Using brute-force approach, design an algorithm to find the post-office location minimizing the average distance between the villages and the post office.
	min distance: 18 	value: 20.0722846167212

### 2)Using brute-force approach, design an algorithm to find the post-office location minimizing the maximum distance from a village to the post office.
	minimize max: 18 	value: 32.449961479175904

### 4)Analyze your designed algorithms mathematically and empirically.
	Empirical Analysis : complexity O(log n**2)
	numerical Analysis : 
		n= 100
		iterations= 9900
		calculation n**2= 10000
		actual  n*(n-1)= 9900

-------------------

