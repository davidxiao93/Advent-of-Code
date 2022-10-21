input = """Before: [2, 3, 2, 2]
0 3 3 0
After:  [0, 3, 2, 2]

Before: [1, 1, 2, 3]
6 0 2 0
After:  [0, 1, 2, 3]

Before: [1, 0, 2, 2]
6 0 2 0
After:  [0, 0, 2, 2]

Before: [1, 1, 1, 1]
11 2 1 0
After:  [2, 1, 1, 1]

Before: [3, 0, 0, 2]
0 3 3 2
After:  [3, 0, 0, 2]

Before: [1, 1, 2, 2]
9 1 0 2
After:  [1, 1, 1, 2]

Before: [3, 2, 1, 1]
5 2 1 1
After:  [3, 2, 1, 1]

Before: [1, 1, 0, 3]
7 1 3 0
After:  [0, 1, 0, 3]

Before: [1, 2, 1, 3]
5 2 1 0
After:  [2, 2, 1, 3]

Before: [0, 2, 2, 0]
8 0 0 0
After:  [0, 2, 2, 0]

Before: [2, 0, 0, 1]
3 0 3 0
After:  [1, 0, 0, 1]

Before: [3, 1, 2, 2]
4 1 3 1
After:  [3, 0, 2, 2]

Before: [2, 2, 1, 1]
5 2 1 1
After:  [2, 2, 1, 1]

Before: [1, 1, 2, 2]
6 0 2 2
After:  [1, 1, 0, 2]

Before: [1, 1, 1, 2]
4 1 3 0
After:  [0, 1, 1, 2]

Before: [2, 1, 3, 1]
13 1 3 0
After:  [1, 1, 3, 1]

Before: [0, 1, 2, 1]
13 1 3 1
After:  [0, 1, 2, 1]

Before: [2, 1, 0, 2]
4 1 3 1
After:  [2, 0, 0, 2]

Before: [2, 1, 0, 1]
2 0 1 3
After:  [2, 1, 0, 1]

Before: [3, 1, 2, 1]
12 1 2 2
After:  [3, 1, 0, 1]

Before: [1, 1, 3, 2]
4 1 3 3
After:  [1, 1, 3, 0]

Before: [2, 2, 1, 3]
7 1 3 0
After:  [0, 2, 1, 3]

Before: [1, 3, 2, 1]
6 0 2 1
After:  [1, 0, 2, 1]

Before: [2, 1, 2, 1]
13 1 3 1
After:  [2, 1, 2, 1]

Before: [2, 1, 3, 0]
14 2 0 3
After:  [2, 1, 3, 1]

Before: [1, 1, 2, 3]
6 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 1, 3]
11 2 1 2
After:  [1, 1, 2, 3]

Before: [2, 2, 3, 2]
0 3 3 0
After:  [0, 2, 3, 2]

Before: [1, 2, 0, 2]
1 0 2 3
After:  [1, 2, 0, 0]

Before: [2, 1, 0, 0]
2 0 1 3
After:  [2, 1, 0, 1]

Before: [0, 2, 1, 1]
5 2 1 3
After:  [0, 2, 1, 2]

Before: [0, 3, 2, 1]
10 3 2 3
After:  [0, 3, 2, 1]

Before: [3, 3, 2, 2]
0 3 3 0
After:  [0, 3, 2, 2]

Before: [1, 1, 2, 0]
12 1 2 0
After:  [0, 1, 2, 0]

Before: [0, 2, 1, 3]
5 2 1 0
After:  [2, 2, 1, 3]

Before: [0, 3, 2, 1]
8 0 0 0
After:  [0, 3, 2, 1]

Before: [1, 1, 1, 3]
11 2 1 1
After:  [1, 2, 1, 3]

Before: [0, 1, 1, 2]
11 2 1 2
After:  [0, 1, 2, 2]

Before: [1, 1, 1, 1]
13 1 3 1
After:  [1, 1, 1, 1]

Before: [1, 3, 0, 0]
1 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 2, 3, 1]
14 2 0 1
After:  [2, 1, 3, 1]

Before: [0, 3, 0, 3]
8 0 0 3
After:  [0, 3, 0, 0]

Before: [0, 0, 1, 1]
8 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 3, 2, 1]
8 0 0 2
After:  [0, 3, 0, 1]

Before: [2, 1, 2, 3]
12 1 2 1
After:  [2, 0, 2, 3]

Before: [3, 2, 2, 3]
14 2 1 2
After:  [3, 2, 1, 3]

Before: [2, 2, 3, 0]
15 2 2 2
After:  [2, 2, 1, 0]

Before: [2, 3, 3, 2]
15 2 2 0
After:  [1, 3, 3, 2]

Before: [1, 1, 0, 0]
1 0 2 3
After:  [1, 1, 0, 0]

Before: [3, 2, 2, 2]
0 3 3 3
After:  [3, 2, 2, 0]

Before: [1, 3, 2, 2]
6 0 2 3
After:  [1, 3, 2, 0]

Before: [2, 1, 0, 1]
3 0 3 1
After:  [2, 1, 0, 1]

Before: [3, 3, 1, 3]
7 2 3 0
After:  [0, 3, 1, 3]

Before: [0, 2, 1, 0]
5 2 1 3
After:  [0, 2, 1, 2]

Before: [1, 1, 1, 2]
4 1 3 2
After:  [1, 1, 0, 2]

Before: [0, 3, 1, 2]
8 0 0 1
After:  [0, 0, 1, 2]

Before: [2, 1, 3, 3]
7 1 3 0
After:  [0, 1, 3, 3]

Before: [3, 2, 2, 1]
10 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 1, 0, 1]
3 0 3 3
After:  [2, 1, 0, 1]

Before: [2, 1, 1, 1]
13 1 3 2
After:  [2, 1, 1, 1]

Before: [2, 2, 0, 3]
7 1 3 1
After:  [2, 0, 0, 3]

Before: [2, 2, 0, 1]
3 0 3 0
After:  [1, 2, 0, 1]

Before: [2, 2, 3, 1]
3 0 3 3
After:  [2, 2, 3, 1]

Before: [1, 2, 0, 0]
1 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 2, 2, 2]
14 3 2 1
After:  [2, 0, 2, 2]

Before: [3, 1, 1, 2]
4 1 3 1
After:  [3, 0, 1, 2]

Before: [2, 1, 1, 1]
2 0 1 3
After:  [2, 1, 1, 1]

Before: [1, 1, 0, 0]
1 0 2 1
After:  [1, 0, 0, 0]

Before: [1, 3, 0, 2]
1 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 1, 1, 3]
9 1 0 2
After:  [1, 1, 1, 3]

Before: [3, 1, 2, 2]
12 1 2 2
After:  [3, 1, 0, 2]

Before: [0, 1, 2, 1]
12 1 2 2
After:  [0, 1, 0, 1]

Before: [3, 2, 0, 3]
7 1 3 3
After:  [3, 2, 0, 0]

Before: [2, 1, 2, 3]
7 2 3 2
After:  [2, 1, 0, 3]

Before: [3, 1, 3, 1]
13 1 3 0
After:  [1, 1, 3, 1]

Before: [2, 1, 1, 1]
11 2 1 0
After:  [2, 1, 1, 1]

Before: [0, 1, 1, 0]
11 2 1 3
After:  [0, 1, 1, 2]

Before: [2, 1, 3, 3]
7 1 3 2
After:  [2, 1, 0, 3]

Before: [2, 3, 2, 1]
10 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 2, 2]
4 1 3 1
After:  [1, 0, 2, 2]

Before: [1, 3, 0, 1]
1 0 2 0
After:  [0, 3, 0, 1]

Before: [1, 3, 0, 3]
1 0 2 3
After:  [1, 3, 0, 0]

Before: [2, 3, 3, 1]
3 0 3 1
After:  [2, 1, 3, 1]

Before: [2, 1, 1, 2]
11 2 1 3
After:  [2, 1, 1, 2]

Before: [2, 1, 1, 1]
2 0 1 1
After:  [2, 1, 1, 1]

Before: [3, 1, 2, 2]
4 1 3 0
After:  [0, 1, 2, 2]

Before: [2, 0, 2, 1]
10 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 3, 0, 1]
1 0 2 1
After:  [1, 0, 0, 1]

Before: [1, 1, 0, 2]
9 1 0 0
After:  [1, 1, 0, 2]

Before: [2, 3, 2, 1]
3 0 3 2
After:  [2, 3, 1, 1]

Before: [1, 2, 2, 1]
0 3 3 3
After:  [1, 2, 2, 0]

Before: [3, 1, 2, 2]
12 1 2 1
After:  [3, 0, 2, 2]

Before: [0, 2, 3, 1]
8 0 0 1
After:  [0, 0, 3, 1]

Before: [0, 0, 2, 1]
10 3 2 2
After:  [0, 0, 1, 1]

Before: [3, 2, 1, 3]
15 0 0 3
After:  [3, 2, 1, 1]

Before: [1, 3, 2, 2]
6 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 2, 2, 3]
6 0 2 3
After:  [1, 2, 2, 0]

Before: [1, 1, 3, 2]
4 1 3 2
After:  [1, 1, 0, 2]

Before: [1, 2, 2, 1]
10 3 2 3
After:  [1, 2, 2, 1]

Before: [1, 2, 2, 1]
6 0 2 2
After:  [1, 2, 0, 1]

Before: [1, 2, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [1, 2, 2, 1]
10 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 3, 3, 1]
3 0 3 3
After:  [2, 3, 3, 1]

Before: [2, 3, 2, 3]
14 2 0 2
After:  [2, 3, 1, 3]

Before: [2, 1, 3, 1]
2 0 1 3
After:  [2, 1, 3, 1]

Before: [0, 3, 3, 0]
8 0 0 1
After:  [0, 0, 3, 0]

Before: [2, 1, 1, 3]
7 2 3 2
After:  [2, 1, 0, 3]

Before: [0, 2, 2, 1]
10 3 2 3
After:  [0, 2, 2, 1]

Before: [3, 2, 1, 3]
5 2 1 3
After:  [3, 2, 1, 2]

Before: [3, 1, 1, 2]
0 3 3 2
After:  [3, 1, 0, 2]

Before: [0, 3, 1, 3]
7 2 3 3
After:  [0, 3, 1, 0]

Before: [2, 0, 2, 1]
10 3 2 3
After:  [2, 0, 2, 1]

Before: [2, 2, 1, 0]
5 2 1 2
After:  [2, 2, 2, 0]

Before: [2, 1, 2, 2]
4 1 3 3
After:  [2, 1, 2, 0]

Before: [1, 3, 1, 1]
0 2 3 2
After:  [1, 3, 0, 1]

Before: [1, 1, 0, 3]
1 0 2 3
After:  [1, 1, 0, 0]

Before: [1, 0, 0, 3]
1 0 2 2
After:  [1, 0, 0, 3]

Before: [2, 1, 1, 0]
11 2 1 0
After:  [2, 1, 1, 0]

Before: [2, 0, 0, 1]
3 0 3 3
After:  [2, 0, 0, 1]

Before: [3, 3, 0, 1]
14 0 2 2
After:  [3, 3, 1, 1]

Before: [0, 1, 2, 0]
8 0 0 1
After:  [0, 0, 2, 0]

Before: [2, 0, 1, 1]
3 0 3 2
After:  [2, 0, 1, 1]

Before: [1, 3, 2, 0]
6 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 3, 2, 0]
2 0 2 3
After:  [3, 3, 2, 1]

Before: [2, 1, 0, 1]
13 1 3 2
After:  [2, 1, 1, 1]

Before: [1, 1, 2, 1]
13 1 3 2
After:  [1, 1, 1, 1]

Before: [1, 3, 2, 0]
6 0 2 2
After:  [1, 3, 0, 0]

Before: [3, 1, 3, 2]
4 1 3 1
After:  [3, 0, 3, 2]

Before: [2, 3, 2, 2]
15 0 0 3
After:  [2, 3, 2, 1]

Before: [2, 3, 2, 1]
3 0 3 3
After:  [2, 3, 2, 1]

Before: [2, 1, 1, 2]
4 1 3 0
After:  [0, 1, 1, 2]

Before: [1, 1, 1, 1]
13 1 3 0
After:  [1, 1, 1, 1]

Before: [3, 1, 1, 0]
11 2 1 2
After:  [3, 1, 2, 0]

Before: [3, 1, 1, 1]
11 2 1 0
After:  [2, 1, 1, 1]

Before: [3, 1, 0, 2]
4 1 3 0
After:  [0, 1, 0, 2]

Before: [3, 3, 1, 3]
15 0 0 3
After:  [3, 3, 1, 1]

Before: [1, 2, 2, 1]
10 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 1, 1, 0]
11 2 1 3
After:  [1, 1, 1, 2]

Before: [1, 1, 1, 2]
11 2 1 0
After:  [2, 1, 1, 2]

Before: [3, 2, 2, 2]
14 2 1 2
After:  [3, 2, 1, 2]

Before: [0, 0, 3, 3]
15 2 2 3
After:  [0, 0, 3, 1]

Before: [0, 3, 2, 2]
0 3 3 0
After:  [0, 3, 2, 2]

Before: [1, 0, 2, 1]
10 3 2 1
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 2]
14 3 2 1
After:  [2, 0, 2, 2]

Before: [1, 0, 0, 3]
1 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 2, 1, 3]
7 2 3 1
After:  [3, 0, 1, 3]

Before: [3, 1, 1, 2]
11 2 1 0
After:  [2, 1, 1, 2]

Before: [1, 3, 2, 1]
6 0 2 0
After:  [0, 3, 2, 1]

Before: [2, 0, 3, 1]
3 0 3 0
After:  [1, 0, 3, 1]

Before: [3, 1, 2, 2]
12 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 1, 2, 0]
12 1 2 3
After:  [3, 1, 2, 0]

Before: [2, 1, 2, 0]
2 0 1 3
After:  [2, 1, 2, 1]

Before: [1, 1, 3, 1]
14 2 3 2
After:  [1, 1, 0, 1]

Before: [1, 3, 2, 3]
6 0 2 0
After:  [0, 3, 2, 3]

Before: [1, 1, 2, 3]
12 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 0, 2, 1]
10 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 0, 2, 0]
6 0 2 1
After:  [1, 0, 2, 0]

Before: [2, 3, 1, 3]
7 2 3 2
After:  [2, 3, 0, 3]

Before: [1, 1, 1, 1]
11 2 1 3
After:  [1, 1, 1, 2]

Before: [2, 1, 2, 2]
2 0 1 0
After:  [1, 1, 2, 2]

Before: [1, 2, 1, 3]
7 2 3 3
After:  [1, 2, 1, 0]

Before: [1, 1, 2, 2]
12 1 2 0
After:  [0, 1, 2, 2]

Before: [2, 0, 2, 1]
10 3 2 2
After:  [2, 0, 1, 1]

Before: [0, 1, 2, 3]
12 1 2 2
After:  [0, 1, 0, 3]

Before: [2, 1, 1, 3]
11 2 1 0
After:  [2, 1, 1, 3]

Before: [2, 1, 3, 1]
13 1 3 3
After:  [2, 1, 3, 1]

Before: [0, 2, 1, 1]
8 0 0 1
After:  [0, 0, 1, 1]

Before: [1, 0, 0, 2]
1 0 2 1
After:  [1, 0, 0, 2]

Before: [2, 1, 3, 3]
2 0 1 1
After:  [2, 1, 3, 3]

Before: [0, 1, 2, 2]
4 1 3 2
After:  [0, 1, 0, 2]

Before: [1, 1, 2, 1]
13 1 3 0
After:  [1, 1, 2, 1]

Before: [1, 1, 3, 0]
9 1 0 1
After:  [1, 1, 3, 0]

Before: [1, 1, 0, 1]
1 0 2 1
After:  [1, 0, 0, 1]

Before: [2, 2, 3, 1]
3 0 3 1
After:  [2, 1, 3, 1]

Before: [3, 2, 1, 2]
5 2 1 0
After:  [2, 2, 1, 2]

Before: [1, 1, 2, 0]
12 1 2 1
After:  [1, 0, 2, 0]

Before: [3, 0, 2, 3]
2 0 2 3
After:  [3, 0, 2, 1]

Before: [2, 1, 3, 3]
2 0 1 2
After:  [2, 1, 1, 3]

Before: [3, 1, 3, 1]
15 0 0 0
After:  [1, 1, 3, 1]

Before: [0, 1, 3, 2]
4 1 3 1
After:  [0, 0, 3, 2]

Before: [3, 2, 3, 3]
15 2 0 0
After:  [1, 2, 3, 3]

Before: [1, 3, 3, 1]
0 3 3 0
After:  [0, 3, 3, 1]

Before: [0, 0, 2, 3]
7 2 3 0
After:  [0, 0, 2, 3]

Before: [0, 2, 1, 3]
7 2 3 2
After:  [0, 2, 0, 3]

Before: [3, 0, 2, 1]
2 0 2 0
After:  [1, 0, 2, 1]

Before: [2, 2, 2, 1]
10 3 2 2
After:  [2, 2, 1, 1]

Before: [1, 2, 0, 1]
1 0 2 0
After:  [0, 2, 0, 1]

Before: [1, 2, 0, 0]
1 0 2 2
After:  [1, 2, 0, 0]

Before: [3, 1, 2, 1]
2 0 2 1
After:  [3, 1, 2, 1]

Before: [0, 0, 3, 1]
8 0 0 1
After:  [0, 0, 3, 1]

Before: [0, 1, 1, 2]
11 2 1 3
After:  [0, 1, 1, 2]

Before: [0, 1, 3, 1]
13 1 3 2
After:  [0, 1, 1, 1]

Before: [1, 1, 1, 2]
11 2 1 2
After:  [1, 1, 2, 2]

Before: [2, 0, 3, 1]
3 0 3 3
After:  [2, 0, 3, 1]

Before: [0, 2, 1, 2]
8 0 0 0
After:  [0, 2, 1, 2]

Before: [1, 0, 2, 1]
6 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 1, 0, 2]
4 1 3 3
After:  [1, 1, 0, 0]

Before: [2, 2, 1, 1]
3 0 3 2
After:  [2, 2, 1, 1]

Before: [1, 2, 1, 2]
5 2 1 2
After:  [1, 2, 2, 2]

Before: [2, 0, 2, 1]
3 0 3 3
After:  [2, 0, 2, 1]

Before: [2, 1, 0, 1]
3 0 3 2
After:  [2, 1, 1, 1]

Before: [2, 2, 1, 2]
5 2 1 1
After:  [2, 2, 1, 2]

Before: [1, 1, 2, 2]
9 1 0 3
After:  [1, 1, 2, 1]

Before: [2, 2, 1, 3]
15 0 0 3
After:  [2, 2, 1, 1]

Before: [3, 1, 0, 1]
13 1 3 3
After:  [3, 1, 0, 1]

Before: [3, 3, 2, 1]
10 3 2 2
After:  [3, 3, 1, 1]

Before: [0, 1, 3, 2]
4 1 3 3
After:  [0, 1, 3, 0]

Before: [0, 1, 1, 0]
11 2 1 2
After:  [0, 1, 2, 0]

Before: [3, 1, 3, 1]
14 3 1 0
After:  [0, 1, 3, 1]

Before: [0, 1, 3, 3]
8 0 0 3
After:  [0, 1, 3, 0]

Before: [0, 1, 2, 1]
10 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
3 0 3 2
After:  [2, 1, 1, 1]

Before: [0, 2, 1, 3]
5 2 1 3
After:  [0, 2, 1, 2]

Before: [1, 0, 0, 3]
1 0 2 0
After:  [0, 0, 0, 3]

Before: [2, 3, 0, 1]
3 0 3 0
After:  [1, 3, 0, 1]

Before: [2, 1, 2, 1]
12 1 2 1
After:  [2, 0, 2, 1]

Before: [2, 1, 3, 2]
4 1 3 0
After:  [0, 1, 3, 2]

Before: [1, 2, 1, 0]
5 2 1 3
After:  [1, 2, 1, 2]

Before: [3, 1, 3, 1]
13 1 3 1
After:  [3, 1, 3, 1]

Before: [1, 2, 1, 0]
5 2 1 1
After:  [1, 2, 1, 0]

Before: [3, 1, 2, 1]
10 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 1, 1]
13 1 3 2
After:  [1, 1, 1, 1]

Before: [2, 1, 2, 1]
13 1 3 2
After:  [2, 1, 1, 1]

Before: [1, 2, 1, 3]
7 1 3 1
After:  [1, 0, 1, 3]

Before: [0, 0, 2, 2]
14 3 2 3
After:  [0, 0, 2, 0]

Before: [2, 2, 1, 3]
15 0 0 1
After:  [2, 1, 1, 3]

Before: [2, 1, 3, 2]
4 1 3 1
After:  [2, 0, 3, 2]

Before: [1, 2, 1, 3]
5 2 1 2
After:  [1, 2, 2, 3]

Before: [2, 2, 1, 0]
5 2 1 3
After:  [2, 2, 1, 2]

Before: [2, 0, 2, 1]
3 0 3 2
After:  [2, 0, 1, 1]

Before: [1, 0, 0, 1]
1 0 2 0
After:  [0, 0, 0, 1]

Before: [2, 1, 1, 0]
15 0 0 0
After:  [1, 1, 1, 0]

Before: [0, 0, 3, 3]
8 0 0 0
After:  [0, 0, 3, 3]

Before: [1, 1, 1, 2]
4 1 3 3
After:  [1, 1, 1, 0]

Before: [1, 2, 0, 3]
1 0 2 1
After:  [1, 0, 0, 3]

Before: [1, 1, 0, 2]
9 1 0 1
After:  [1, 1, 0, 2]

Before: [3, 1, 1, 1]
11 2 1 3
After:  [3, 1, 1, 2]

Before: [1, 1, 0, 3]
7 1 3 1
After:  [1, 0, 0, 3]

Before: [1, 1, 1, 3]
7 1 3 2
After:  [1, 1, 0, 3]

Before: [1, 1, 2, 3]
6 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 1, 2]
4 1 3 3
After:  [2, 1, 1, 0]

Before: [2, 2, 2, 3]
7 1 3 2
After:  [2, 2, 0, 3]

Before: [1, 3, 2, 1]
0 3 3 3
After:  [1, 3, 2, 0]

Before: [0, 0, 3, 3]
8 0 0 3
After:  [0, 0, 3, 0]

Before: [3, 1, 3, 1]
15 0 0 1
After:  [3, 1, 3, 1]

Before: [1, 0, 0, 2]
1 0 2 2
After:  [1, 0, 0, 2]

Before: [0, 0, 0, 1]
0 3 3 1
After:  [0, 0, 0, 1]

Before: [1, 1, 1, 2]
9 1 0 0
After:  [1, 1, 1, 2]

Before: [1, 3, 0, 1]
1 0 2 2
After:  [1, 3, 0, 1]

Before: [1, 1, 3, 3]
9 1 0 0
After:  [1, 1, 3, 3]

Before: [2, 1, 3, 1]
13 1 3 2
After:  [2, 1, 1, 1]

Before: [2, 1, 3, 2]
4 1 3 3
After:  [2, 1, 3, 0]

Before: [2, 1, 2, 1]
13 1 3 3
After:  [2, 1, 2, 1]

Before: [1, 0, 2, 2]
6 0 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 1]
10 3 2 2
After:  [1, 1, 1, 1]

Before: [3, 2, 1, 3]
5 2 1 2
After:  [3, 2, 2, 3]

Before: [0, 1, 2, 0]
12 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 1, 1, 3]
2 0 1 0
After:  [1, 1, 1, 3]

Before: [1, 2, 2, 3]
14 2 1 2
After:  [1, 2, 1, 3]

Before: [1, 2, 0, 3]
1 0 2 0
After:  [0, 2, 0, 3]

Before: [0, 1, 2, 2]
8 0 0 2
After:  [0, 1, 0, 2]

Before: [0, 2, 1, 0]
5 2 1 1
After:  [0, 2, 1, 0]

Before: [2, 0, 0, 1]
15 0 0 2
After:  [2, 0, 1, 1]

Before: [2, 2, 1, 3]
5 2 1 0
After:  [2, 2, 1, 3]

Before: [3, 2, 2, 1]
10 3 2 2
After:  [3, 2, 1, 1]

Before: [0, 3, 2, 2]
14 3 2 2
After:  [0, 3, 0, 2]

Before: [1, 2, 0, 1]
1 0 2 2
After:  [1, 2, 0, 1]

Before: [0, 1, 1, 0]
11 2 1 0
After:  [2, 1, 1, 0]

Before: [1, 2, 2, 3]
14 2 1 3
After:  [1, 2, 2, 1]

Before: [2, 1, 3, 1]
3 0 3 3
After:  [2, 1, 3, 1]

Before: [0, 1, 2, 3]
7 1 3 3
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 2]
2 0 1 1
After:  [2, 1, 2, 2]

Before: [2, 2, 1, 0]
5 2 1 1
After:  [2, 2, 1, 0]

Before: [3, 2, 1, 3]
5 2 1 0
After:  [2, 2, 1, 3]

Before: [1, 1, 2, 1]
0 3 3 1
After:  [1, 0, 2, 1]

Before: [1, 0, 2, 1]
6 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 3, 0, 2]
1 0 2 0
After:  [0, 3, 0, 2]

Before: [0, 1, 1, 3]
11 2 1 2
After:  [0, 1, 2, 3]

Before: [1, 1, 3, 3]
9 1 0 1
After:  [1, 1, 3, 3]

Before: [3, 1, 2, 3]
12 1 2 1
After:  [3, 0, 2, 3]

Before: [0, 1, 1, 1]
13 1 3 0
After:  [1, 1, 1, 1]

Before: [1, 1, 2, 3]
9 1 0 1
After:  [1, 1, 2, 3]

Before: [0, 3, 1, 3]
7 2 3 0
After:  [0, 3, 1, 3]

Before: [3, 1, 2, 1]
13 1 3 2
After:  [3, 1, 1, 1]

Before: [1, 0, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [1, 1, 0, 3]
1 0 2 0
After:  [0, 1, 0, 3]

Before: [2, 1, 2, 2]
12 1 2 2
After:  [2, 1, 0, 2]

Before: [3, 0, 1, 3]
14 3 0 0
After:  [1, 0, 1, 3]

Before: [3, 1, 3, 3]
7 1 3 3
After:  [3, 1, 3, 0]

Before: [1, 1, 0, 0]
1 0 2 0
After:  [0, 1, 0, 0]

Before: [1, 1, 1, 1]
0 2 3 2
After:  [1, 1, 0, 1]

Before: [2, 1, 0, 1]
2 0 1 2
After:  [2, 1, 1, 1]

Before: [1, 1, 2, 1]
14 3 1 1
After:  [1, 0, 2, 1]

Before: [0, 0, 2, 3]
7 2 3 3
After:  [0, 0, 2, 0]

Before: [3, 2, 0, 0]
14 0 2 1
After:  [3, 1, 0, 0]

Before: [0, 0, 2, 3]
8 0 0 0
After:  [0, 0, 2, 3]

Before: [3, 1, 1, 0]
11 2 1 1
After:  [3, 2, 1, 0]

Before: [1, 2, 1, 1]
5 2 1 2
After:  [1, 2, 2, 1]

Before: [0, 2, 1, 3]
7 2 3 3
After:  [0, 2, 1, 0]

Before: [3, 1, 2, 2]
15 0 0 3
After:  [3, 1, 2, 1]

Before: [0, 0, 0, 2]
8 0 0 2
After:  [0, 0, 0, 2]

Before: [3, 1, 3, 1]
13 1 3 2
After:  [3, 1, 1, 1]

Before: [1, 1, 2, 3]
9 1 0 2
After:  [1, 1, 1, 3]

Before: [1, 2, 0, 2]
1 0 2 2
After:  [1, 2, 0, 2]

Before: [2, 1, 2, 3]
2 0 1 3
After:  [2, 1, 2, 1]

Before: [1, 2, 0, 3]
1 0 2 2
After:  [1, 2, 0, 3]

Before: [1, 0, 2, 0]
6 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 0, 3, 1]
0 3 3 2
After:  [1, 0, 0, 1]

Before: [1, 3, 2, 1]
6 0 2 3
After:  [1, 3, 2, 0]

Before: [1, 1, 1, 1]
9 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 3, 2, 1]
0 3 3 1
After:  [0, 0, 2, 1]

Before: [1, 1, 3, 1]
13 1 3 3
After:  [1, 1, 3, 1]

Before: [2, 2, 0, 3]
7 1 3 0
After:  [0, 2, 0, 3]

Before: [0, 3, 2, 1]
0 3 3 0
After:  [0, 3, 2, 1]

Before: [1, 0, 0, 1]
1 0 2 2
After:  [1, 0, 0, 1]

Before: [2, 1, 2, 1]
2 0 1 2
After:  [2, 1, 1, 1]

Before: [1, 2, 2, 2]
6 0 2 2
After:  [1, 2, 0, 2]

Before: [0, 1, 1, 1]
13 1 3 3
After:  [0, 1, 1, 1]

Before: [2, 1, 1, 0]
11 2 1 2
After:  [2, 1, 2, 0]

Before: [0, 1, 3, 1]
13 1 3 1
After:  [0, 1, 3, 1]

Before: [3, 2, 0, 2]
0 3 3 1
After:  [3, 0, 0, 2]

Before: [1, 1, 2, 1]
10 3 2 3
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
13 1 3 0
After:  [1, 1, 2, 1]

Before: [2, 1, 0, 1]
13 1 3 1
After:  [2, 1, 0, 1]

Before: [2, 1, 2, 2]
12 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 1, 2, 0]
12 1 2 1
After:  [0, 0, 2, 0]

Before: [3, 1, 2, 2]
4 1 3 2
After:  [3, 1, 0, 2]

Before: [1, 1, 0, 2]
1 0 2 1
After:  [1, 0, 0, 2]

Before: [0, 2, 1, 1]
0 2 3 2
After:  [0, 2, 0, 1]

Before: [1, 1, 2, 0]
6 0 2 0
After:  [0, 1, 2, 0]

Before: [0, 3, 1, 2]
8 0 0 3
After:  [0, 3, 1, 0]

Before: [1, 3, 0, 0]
1 0 2 2
After:  [1, 3, 0, 0]

Before: [1, 1, 2, 0]
12 1 2 2
After:  [1, 1, 0, 0]

Before: [2, 1, 0, 2]
0 3 3 1
After:  [2, 0, 0, 2]

Before: [0, 3, 3, 3]
8 0 0 1
After:  [0, 0, 3, 3]

Before: [3, 3, 0, 1]
0 3 3 0
After:  [0, 3, 0, 1]

Before: [3, 1, 1, 2]
4 1 3 3
After:  [3, 1, 1, 0]

Before: [2, 1, 2, 3]
12 1 2 3
After:  [2, 1, 2, 0]

Before: [3, 1, 2, 1]
12 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 0, 2, 2]
6 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 1, 0, 1]
0 3 3 1
After:  [1, 0, 0, 1]

Before: [1, 1, 0, 3]
9 1 0 2
After:  [1, 1, 1, 3]

Before: [3, 0, 2, 1]
10 3 2 3
After:  [3, 0, 2, 1]

Before: [2, 2, 3, 3]
14 3 2 3
After:  [2, 2, 3, 1]

Before: [3, 1, 2, 2]
12 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 1, 2, 1]
10 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 1, 3, 0]
8 0 0 2
After:  [0, 1, 0, 0]

Before: [3, 1, 2, 0]
12 1 2 1
After:  [3, 0, 2, 0]

Before: [1, 3, 2, 0]
6 0 2 3
After:  [1, 3, 2, 0]

Before: [2, 0, 1, 3]
7 2 3 3
After:  [2, 0, 1, 0]

Before: [3, 2, 2, 1]
10 3 2 3
After:  [3, 2, 2, 1]

Before: [1, 2, 0, 0]
1 0 2 3
After:  [1, 2, 0, 0]

Before: [2, 1, 1, 1]
0 2 3 0
After:  [0, 1, 1, 1]

Before: [3, 2, 1, 1]
5 2 1 3
After:  [3, 2, 1, 2]

Before: [3, 1, 3, 1]
14 2 3 0
After:  [0, 1, 3, 1]

Before: [2, 1, 1, 3]
14 2 1 1
After:  [2, 0, 1, 3]

Before: [0, 1, 1, 2]
8 0 0 0
After:  [0, 1, 1, 2]

Before: [2, 3, 3, 2]
15 2 2 2
After:  [2, 3, 1, 2]

Before: [0, 1, 2, 3]
7 2 3 1
After:  [0, 0, 2, 3]

Before: [1, 1, 0, 2]
4 1 3 2
After:  [1, 1, 0, 2]

Before: [0, 2, 3, 0]
8 0 0 2
After:  [0, 2, 0, 0]

Before: [0, 1, 1, 1]
11 2 1 1
After:  [0, 2, 1, 1]

Before: [2, 1, 1, 1]
13 1 3 0
After:  [1, 1, 1, 1]

Before: [2, 3, 1, 3]
7 2 3 0
After:  [0, 3, 1, 3]

Before: [2, 1, 2, 3]
12 1 2 2
After:  [2, 1, 0, 3]

Before: [2, 2, 1, 3]
5 2 1 3
After:  [2, 2, 1, 2]

Before: [3, 1, 1, 3]
11 2 1 0
After:  [2, 1, 1, 3]

Before: [0, 0, 1, 3]
7 2 3 1
After:  [0, 0, 1, 3]

Before: [1, 3, 2, 1]
10 3 2 2
After:  [1, 3, 1, 1]

Before: [3, 2, 1, 2]
15 0 0 2
After:  [3, 2, 1, 2]

Before: [1, 2, 1, 1]
0 2 3 1
After:  [1, 0, 1, 1]

Before: [1, 1, 1, 3]
9 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 1, 0, 3]
9 1 0 3
After:  [1, 1, 0, 1]

Before: [0, 1, 1, 1]
11 2 1 2
After:  [0, 1, 2, 1]

Before: [0, 1, 2, 1]
13 1 3 2
After:  [0, 1, 1, 1]

Before: [1, 1, 2, 2]
4 1 3 2
After:  [1, 1, 0, 2]

Before: [3, 1, 1, 2]
11 2 1 3
After:  [3, 1, 1, 2]

Before: [2, 2, 3, 2]
0 3 3 3
After:  [2, 2, 3, 0]

Before: [0, 0, 1, 1]
0 2 3 1
After:  [0, 0, 1, 1]

Before: [0, 1, 2, 2]
12 1 2 1
After:  [0, 0, 2, 2]

Before: [2, 0, 3, 1]
3 0 3 2
After:  [2, 0, 1, 1]

Before: [1, 0, 2, 0]
6 0 2 0
After:  [0, 0, 2, 0]

Before: [0, 2, 1, 1]
5 2 1 0
After:  [2, 2, 1, 1]

Before: [1, 3, 3, 0]
15 2 2 0
After:  [1, 3, 3, 0]

Before: [0, 3, 2, 0]
8 0 0 2
After:  [0, 3, 0, 0]

Before: [2, 2, 2, 1]
0 3 3 1
After:  [2, 0, 2, 1]

Before: [3, 1, 1, 2]
4 1 3 0
After:  [0, 1, 1, 2]

Before: [1, 2, 1, 0]
5 2 1 0
After:  [2, 2, 1, 0]

Before: [2, 2, 3, 3]
15 0 0 0
After:  [1, 2, 3, 3]

Before: [2, 1, 0, 0]
2 0 1 1
After:  [2, 1, 0, 0]

Before: [1, 2, 2, 3]
6 0 2 2
After:  [1, 2, 0, 3]

Before: [1, 0, 0, 1]
1 0 2 1
After:  [1, 0, 0, 1]

Before: [2, 2, 0, 1]
3 0 3 1
After:  [2, 1, 0, 1]

Before: [3, 2, 1, 2]
5 2 1 1
After:  [3, 2, 1, 2]

Before: [2, 1, 3, 2]
14 2 0 1
After:  [2, 1, 3, 2]

Before: [1, 1, 0, 0]
9 1 0 2
After:  [1, 1, 1, 0]

Before: [2, 2, 3, 3]
15 2 2 2
After:  [2, 2, 1, 3]

Before: [0, 2, 1, 0]
8 0 0 2
After:  [0, 2, 0, 0]

Before: [1, 1, 0, 1]
9 1 0 0
After:  [1, 1, 0, 1]

Before: [0, 1, 2, 2]
4 1 3 0
After:  [0, 1, 2, 2]

Before: [1, 1, 0, 0]
9 1 0 0
After:  [1, 1, 0, 0]

Before: [2, 3, 2, 1]
3 0 3 1
After:  [2, 1, 2, 1]

Before: [1, 2, 1, 3]
5 2 1 3
After:  [1, 2, 1, 2]

Before: [2, 1, 1, 3]
11 2 1 2
After:  [2, 1, 2, 3]

Before: [1, 1, 3, 0]
9 1 0 2
After:  [1, 1, 1, 0]

Before: [2, 1, 1, 3]
11 2 1 1
After:  [2, 2, 1, 3]

Before: [2, 1, 3, 2]
2 0 1 2
After:  [2, 1, 1, 2]

Before: [0, 2, 1, 3]
5 2 1 2
After:  [0, 2, 2, 3]

Before: [1, 0, 0, 2]
1 0 2 3
After:  [1, 0, 0, 0]

Before: [1, 1, 1, 2]
9 1 0 3
After:  [1, 1, 1, 1]

Before: [2, 1, 3, 2]
4 1 3 2
After:  [2, 1, 0, 2]

Before: [1, 0, 2, 2]
6 0 2 2
After:  [1, 0, 0, 2]

Before: [3, 1, 1, 3]
11 2 1 1
After:  [3, 2, 1, 3]

Before: [3, 1, 2, 3]
2 0 2 0
After:  [1, 1, 2, 3]

Before: [1, 2, 0, 2]
1 0 2 0
After:  [0, 2, 0, 2]

Before: [3, 1, 2, 1]
10 3 2 2
After:  [3, 1, 1, 1]

Before: [1, 0, 2, 3]
7 2 3 0
After:  [0, 0, 2, 3]

Before: [3, 1, 2, 3]
12 1 2 0
After:  [0, 1, 2, 3]

Before: [2, 1, 1, 3]
7 2 3 1
After:  [2, 0, 1, 3]

Before: [0, 2, 1, 2]
5 2 1 3
After:  [0, 2, 1, 2]

Before: [3, 1, 1, 0]
11 2 1 0
After:  [2, 1, 1, 0]

Before: [1, 1, 3, 1]
9 1 0 0
After:  [1, 1, 3, 1]

Before: [1, 1, 2, 2]
9 1 0 1
After:  [1, 1, 2, 2]

Before: [2, 1, 1, 3]
11 2 1 3
After:  [2, 1, 1, 2]

Before: [1, 1, 1, 2]
4 1 3 1
After:  [1, 0, 1, 2]

Before: [3, 1, 0, 1]
13 1 3 0
After:  [1, 1, 0, 1]

Before: [1, 2, 2, 3]
6 0 2 0
After:  [0, 2, 2, 3]

Before: [1, 3, 0, 3]
1 0 2 0
After:  [0, 3, 0, 3]

Before: [2, 1, 1, 0]
2 0 1 2
After:  [2, 1, 1, 0]

Before: [0, 1, 2, 1]
12 1 2 3
After:  [0, 1, 2, 0]

Before: [2, 3, 1, 1]
3 0 3 3
After:  [2, 3, 1, 1]

Before: [2, 1, 3, 3]
2 0 1 3
After:  [2, 1, 3, 1]

Before: [1, 3, 2, 1]
10 3 2 3
After:  [1, 3, 2, 1]

Before: [1, 1, 3, 3]
9 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 1, 3, 2]
9 1 0 1
After:  [1, 1, 3, 2]

Before: [1, 1, 0, 1]
13 1 3 2
After:  [1, 1, 1, 1]

Before: [3, 0, 2, 0]
2 0 2 1
After:  [3, 1, 2, 0]

Before: [2, 0, 0, 0]
14 0 1 2
After:  [2, 0, 1, 0]

Before: [0, 1, 2, 1]
13 1 3 3
After:  [0, 1, 2, 1]

Before: [2, 1, 3, 0]
14 2 0 1
After:  [2, 1, 3, 0]

Before: [2, 1, 0, 1]
13 1 3 0
After:  [1, 1, 0, 1]

Before: [2, 1, 0, 1]
2 0 1 1
After:  [2, 1, 0, 1]

Before: [0, 3, 2, 1]
10 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 1, 3, 1]
0 3 3 2
After:  [0, 1, 0, 1]

Before: [0, 2, 1, 1]
5 2 1 1
After:  [0, 2, 1, 1]

Before: [2, 1, 1, 2]
15 0 0 3
After:  [2, 1, 1, 1]

Before: [1, 1, 2, 0]
6 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 1]
6 0 2 0
After:  [0, 1, 2, 1]

Before: [0, 2, 1, 3]
7 1 3 1
After:  [0, 0, 1, 3]

Before: [1, 0, 0, 0]
1 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 1, 2, 3]
2 0 1 2
After:  [2, 1, 1, 3]

Before: [0, 2, 0, 2]
0 3 3 1
After:  [0, 0, 0, 2]

Before: [0, 2, 3, 0]
15 2 2 2
After:  [0, 2, 1, 0]

Before: [1, 2, 2, 2]
14 2 1 3
After:  [1, 2, 2, 1]

Before: [0, 1, 3, 1]
8 0 0 2
After:  [0, 1, 0, 1]

Before: [3, 3, 3, 2]
15 0 0 3
After:  [3, 3, 3, 1]

Before: [3, 3, 0, 2]
14 0 2 1
After:  [3, 1, 0, 2]

Before: [0, 1, 1, 3]
11 2 1 0
After:  [2, 1, 1, 3]

Before: [1, 1, 0, 1]
9 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 1, 2, 1]
10 3 2 3
After:  [0, 1, 2, 1]

Before: [2, 2, 2, 1]
10 3 2 1
After:  [2, 1, 2, 1]

Before: [0, 1, 2, 2]
4 1 3 3
After:  [0, 1, 2, 0]

Before: [1, 2, 2, 1]
10 3 2 2
After:  [1, 2, 1, 1]

Before: [2, 1, 1, 2]
11 2 1 1
After:  [2, 2, 1, 2]

Before: [1, 1, 2, 1]
12 1 2 3
After:  [1, 1, 2, 0]

Before: [3, 3, 1, 1]
0 2 3 1
After:  [3, 0, 1, 1]

Before: [0, 1, 2, 2]
4 1 3 1
After:  [0, 0, 2, 2]

Before: [0, 3, 2, 2]
8 0 0 3
After:  [0, 3, 2, 0]

Before: [2, 1, 2, 1]
2 0 1 0
After:  [1, 1, 2, 1]

Before: [1, 1, 0, 3]
1 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 3, 3, 2]
15 0 0 0
After:  [1, 3, 3, 2]

Before: [0, 1, 1, 2]
4 1 3 2
After:  [0, 1, 0, 2]

Before: [1, 3, 0, 3]
1 0 2 1
After:  [1, 0, 0, 3]

Before: [1, 1, 0, 1]
1 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 1, 0, 2]
4 1 3 0
After:  [0, 1, 0, 2]

Before: [3, 2, 2, 2]
2 0 2 2
After:  [3, 2, 1, 2]

Before: [0, 2, 2, 1]
10 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 1, 0, 2]
4 1 3 2
After:  [0, 1, 0, 2]

Before: [0, 1, 0, 2]
4 1 3 3
After:  [0, 1, 0, 0]

Before: [1, 1, 2, 1]
10 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 1, 0, 1]
13 1 3 0
After:  [1, 1, 0, 1]

Before: [1, 3, 2, 2]
6 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 1, 2, 1]
13 1 3 0
After:  [1, 1, 2, 1]

Before: [0, 1, 1, 3]
11 2 1 1
After:  [0, 2, 1, 3]

Before: [3, 2, 1, 0]
5 2 1 3
After:  [3, 2, 1, 2]

Before: [2, 1, 2, 3]
7 2 3 3
After:  [2, 1, 2, 0]

Before: [1, 1, 1, 1]
11 2 1 2
After:  [1, 1, 2, 1]

Before: [2, 1, 1, 1]
3 0 3 2
After:  [2, 1, 1, 1]

Before: [0, 1, 1, 3]
8 0 0 1
After:  [0, 0, 1, 3]

Before: [3, 2, 3, 3]
7 1 3 3
After:  [3, 2, 3, 0]

Before: [0, 3, 0, 0]
8 0 0 2
After:  [0, 3, 0, 0]

Before: [1, 1, 2, 1]
6 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 1, 1, 2]
4 1 3 0
After:  [0, 1, 1, 2]

Before: [1, 1, 2, 1]
9 1 0 1
After:  [1, 1, 2, 1]

Before: [3, 1, 2, 0]
12 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 3, 0, 3]
1 0 2 2
After:  [1, 3, 0, 3]

Before: [1, 1, 0, 3]
9 1 0 1
After:  [1, 1, 0, 3]

Before: [0, 2, 2, 2]
8 0 0 1
After:  [0, 0, 2, 2]

Before: [0, 1, 1, 1]
13 1 3 1
After:  [0, 1, 1, 1]

Before: [1, 1, 3, 1]
13 1 3 0
After:  [1, 1, 3, 1]

Before: [0, 1, 2, 1]
8 0 0 0
After:  [0, 1, 2, 1]

Before: [2, 1, 2, 1]
12 1 2 2
After:  [2, 1, 0, 1]

Before: [1, 0, 2, 3]
6 0 2 1
After:  [1, 0, 2, 3]

Before: [3, 0, 3, 1]
15 2 0 2
After:  [3, 0, 1, 1]

Before: [0, 1, 1, 1]
0 2 3 0
After:  [0, 1, 1, 1]

Before: [3, 0, 0, 3]
14 0 2 1
After:  [3, 1, 0, 3]

Before: [3, 1, 1, 1]
0 2 3 1
After:  [3, 0, 1, 1]

Before: [0, 1, 2, 3]
7 2 3 3
After:  [0, 1, 2, 0]

Before: [3, 1, 0, 1]
13 1 3 1
After:  [3, 1, 0, 1]

Before: [0, 0, 3, 0]
8 0 0 1
After:  [0, 0, 3, 0]

Before: [1, 1, 0, 2]
1 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 1, 1, 2]
4 1 3 1
After:  [2, 0, 1, 2]

Before: [3, 2, 3, 0]
15 2 2 3
After:  [3, 2, 3, 1]

Before: [0, 2, 0, 3]
7 1 3 0
After:  [0, 2, 0, 3]

Before: [1, 1, 3, 2]
9 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 3, 1, 3]
8 0 0 1
After:  [0, 0, 1, 3]

Before: [3, 1, 2, 1]
2 0 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 3, 1]
9 1 0 2
After:  [1, 1, 1, 1]

Before: [2, 1, 3, 0]
2 0 1 3
After:  [2, 1, 3, 1]

Before: [2, 1, 1, 0]
11 2 1 1
After:  [2, 2, 1, 0]

Before: [3, 1, 1, 1]
13 1 3 0
After:  [1, 1, 1, 1]

Before: [2, 2, 1, 3]
5 2 1 1
After:  [2, 2, 1, 3]

Before: [0, 0, 2, 1]
10 3 2 3
After:  [0, 0, 2, 1]

Before: [3, 3, 0, 2]
0 3 3 1
After:  [3, 0, 0, 2]

Before: [0, 2, 1, 0]
8 0 0 0
After:  [0, 2, 1, 0]

Before: [3, 3, 0, 2]
15 0 0 3
After:  [3, 3, 0, 1]

Before: [1, 0, 2, 3]
6 0 2 0
After:  [0, 0, 2, 3]

Before: [0, 0, 1, 1]
8 0 0 1
After:  [0, 0, 1, 1]

Before: [1, 0, 2, 1]
10 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 2, 1, 2]
5 2 1 1
After:  [1, 2, 1, 2]

Before: [2, 1, 3, 1]
14 2 0 1
After:  [2, 1, 3, 1]

Before: [2, 1, 2, 0]
2 0 1 0
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 2]
6 0 2 3
After:  [1, 1, 2, 0]

Before: [2, 1, 1, 3]
2 0 1 2
After:  [2, 1, 1, 3]

Before: [2, 3, 3, 2]
14 2 0 2
After:  [2, 3, 1, 2]

Before: [1, 0, 0, 2]
1 0 2 0
After:  [0, 0, 0, 2]

Before: [3, 3, 2, 2]
15 0 0 0
After:  [1, 3, 2, 2]

Before: [0, 1, 1, 2]
4 1 3 3
After:  [0, 1, 1, 0]

Before: [2, 2, 1, 2]
5 2 1 3
After:  [2, 2, 1, 2]

Before: [2, 1, 2, 0]
12 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 1, 0, 1]
13 1 3 2
After:  [3, 1, 1, 1]

Before: [1, 2, 1, 1]
5 2 1 1
After:  [1, 2, 1, 1]

Before: [2, 1, 2, 2]
4 1 3 2
After:  [2, 1, 0, 2]

Before: [0, 1, 0, 2]
4 1 3 0
After:  [0, 1, 0, 2]

Before: [3, 1, 0, 2]
4 1 3 2
After:  [3, 1, 0, 2]

Before: [1, 1, 3, 2]
4 1 3 1
After:  [1, 0, 3, 2]

Before: [3, 1, 1, 1]
13 1 3 2
After:  [3, 1, 1, 1]

Before: [0, 0, 2, 0]
8 0 0 3
After:  [0, 0, 2, 0]

Before: [1, 1, 3, 2]
9 1 0 0
After:  [1, 1, 3, 2]

Before: [3, 2, 1, 0]
5 2 1 1
After:  [3, 2, 1, 0]

Before: [1, 1, 0, 2]
1 0 2 0
After:  [0, 1, 0, 2]

Before: [2, 1, 0, 1]
13 1 3 3
After:  [2, 1, 0, 1]

Before: [3, 1, 2, 0]
12 1 2 2
After:  [3, 1, 0, 0]

Before: [3, 2, 2, 3]
2 0 2 0
After:  [1, 2, 2, 3]

Before: [1, 1, 1, 0]
11 2 1 1
After:  [1, 2, 1, 0]

Before: [0, 0, 1, 2]
8 0 0 3
After:  [0, 0, 1, 0]

Before: [1, 1, 0, 0]
9 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 1, 3, 0]
9 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 1, 1, 1]
11 2 1 1
After:  [1, 2, 1, 1]

Before: [3, 0, 0, 0]
14 0 2 3
After:  [3, 0, 0, 1]

Before: [2, 1, 1, 3]
7 1 3 3
After:  [2, 1, 1, 0]

Before: [0, 3, 3, 2]
8 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 1, 2, 1]
12 1 2 1
After:  [3, 0, 2, 1]

Before: [3, 0, 2, 3]
7 2 3 0
After:  [0, 0, 2, 3]

Before: [3, 1, 1, 1]
14 3 1 1
After:  [3, 0, 1, 1]

Before: [1, 1, 1, 3]
9 1 0 0
After:  [1, 1, 1, 3]

Before: [0, 0, 3, 3]
8 0 0 2
After:  [0, 0, 0, 3]

Before: [3, 1, 3, 3]
7 1 3 1
After:  [3, 0, 3, 3]

Before: [1, 1, 2, 2]
12 1 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 0, 1]
1 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 2, 2, 1]
3 0 3 2
After:  [2, 2, 1, 1]

Before: [2, 0, 3, 0]
14 0 1 1
After:  [2, 1, 3, 0]

Before: [1, 1, 2, 2]
4 1 3 3
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 3]
12 1 2 2
After:  [1, 1, 0, 3]

Before: [1, 2, 1, 3]
7 2 3 2
After:  [1, 2, 0, 3]

Before: [3, 0, 0, 1]
14 0 2 2
After:  [3, 0, 1, 1]

Before: [3, 2, 1, 0]
5 2 1 0
After:  [2, 2, 1, 0]

Before: [2, 3, 2, 1]
3 0 3 0
After:  [1, 3, 2, 1]

Before: [0, 1, 3, 2]
8 0 0 3
After:  [0, 1, 3, 0]

Before: [2, 2, 1, 1]
3 0 3 3
After:  [2, 2, 1, 1]

Before: [3, 2, 3, 1]
0 3 3 3
After:  [3, 2, 3, 0]

Before: [2, 1, 1, 0]
14 2 1 3
After:  [2, 1, 1, 0]

Before: [2, 2, 1, 3]
7 2 3 1
After:  [2, 0, 1, 3]

Before: [2, 3, 3, 1]
3 0 3 2
After:  [2, 3, 1, 1]

Before: [1, 1, 2, 1]
9 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 3, 2, 1]
10 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 1, 0, 1]
13 1 3 3
After:  [0, 1, 0, 1]

Before: [1, 1, 1, 3]
11 2 1 3
After:  [1, 1, 1, 2]

Before: [3, 1, 1, 2]
11 2 1 2
After:  [3, 1, 2, 2]

Before: [1, 3, 2, 3]
6 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 1, 2, 3]
8 0 0 2
After:  [0, 1, 0, 3]

Before: [3, 0, 1, 3]
14 3 0 2
After:  [3, 0, 1, 3]

Before: [2, 1, 2, 0]
12 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 1, 1, 1]
11 2 1 0
After:  [2, 1, 1, 1]

Before: [2, 3, 2, 1]
0 3 3 2
After:  [2, 3, 0, 1]

Before: [1, 1, 0, 2]
0 3 3 3
After:  [1, 1, 0, 0]

Before: [1, 0, 0, 1]
1 0 2 3
After:  [1, 0, 0, 0]

Before: [3, 2, 1, 3]
7 2 3 3
After:  [3, 2, 1, 0]

Before: [3, 1, 1, 3]
11 2 1 2
After:  [3, 1, 2, 3]

Before: [0, 1, 2, 2]
12 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 3, 2, 1]
10 3 2 0
After:  [1, 3, 2, 1]

Before: [1, 1, 3, 1]
13 1 3 1
After:  [1, 1, 3, 1]

Before: [2, 2, 1, 1]
3 0 3 1
After:  [2, 1, 1, 1]

Before: [2, 1, 2, 2]
4 1 3 0
After:  [0, 1, 2, 2]

Before: [1, 1, 1, 1]
9 1 0 2
After:  [1, 1, 1, 1]

Before: [1, 3, 2, 1]
10 3 2 0
After:  [1, 3, 2, 1]

Before: [2, 0, 2, 1]
10 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 0, 3]
1 0 2 2
After:  [1, 1, 0, 3]

Before: [1, 2, 0, 1]
1 0 2 3
After:  [1, 2, 0, 0]

Before: [1, 3, 0, 0]
1 0 2 0
After:  [0, 3, 0, 0]

Before: [2, 1, 1, 3]
14 2 1 0
After:  [0, 1, 1, 3]

Before: [1, 1, 1, 2]
9 1 0 1
After:  [1, 1, 1, 2]

Before: [1, 1, 0, 1]
13 1 3 1
After:  [1, 1, 0, 1]

Before: [2, 0, 0, 2]
15 0 0 0
After:  [1, 0, 0, 2]

Before: [2, 3, 1, 1]
3 0 3 0
After:  [1, 3, 1, 1]

Before: [0, 1, 2, 0]
12 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 2, 1, 2]
5 2 1 0
After:  [2, 2, 1, 2]

Before: [2, 0, 2, 2]
14 3 2 2
After:  [2, 0, 0, 2]

Before: [0, 2, 2, 1]
10 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 1, 0, 2]
4 1 3 3
After:  [2, 1, 0, 0]

Before: [1, 3, 0, 2]
1 0 2 2
After:  [1, 3, 0, 2]

Before: [0, 0, 2, 3]
8 0 0 1
After:  [0, 0, 2, 3]

Before: [2, 1, 1, 3]
7 1 3 0
After:  [0, 1, 1, 3]

Before: [3, 1, 2, 1]
13 1 3 0
After:  [1, 1, 2, 1]

Before: [2, 0, 1, 1]
3 0 3 1
After:  [2, 1, 1, 1]

Before: [1, 1, 2, 1]
13 1 3 1
After:  [1, 1, 2, 1]

Before: [0, 1, 2, 1]
12 1 2 1
After:  [0, 0, 2, 1]

Before: [2, 2, 3, 3]
14 3 2 2
After:  [2, 2, 1, 3]

Before: [3, 1, 1, 1]
13 1 3 3
After:  [3, 1, 1, 1]

Before: [3, 3, 3, 2]
15 2 0 1
After:  [3, 1, 3, 2]

Before: [2, 1, 2, 1]
3 0 3 1
After:  [2, 1, 2, 1]

Before: [3, 1, 2, 0]
2 0 2 3
After:  [3, 1, 2, 1]

Before: [1, 2, 1, 2]
5 2 1 3
After:  [1, 2, 1, 2]

Before: [3, 2, 1, 1]
5 2 1 0
After:  [2, 2, 1, 1]

Before: [0, 1, 2, 1]
12 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 1, 1, 1]
3 0 3 0
After:  [1, 1, 1, 1]

Before: [3, 1, 1, 2]
11 2 1 1
After:  [3, 2, 1, 2]

Before: [1, 1, 1, 3]
11 2 1 0
After:  [2, 1, 1, 3]

Before: [1, 1, 2, 0]
9 1 0 3
After:  [1, 1, 2, 1]

Before: [0, 2, 2, 3]
8 0 0 3
After:  [0, 2, 2, 0]

Before: [0, 0, 2, 1]
10 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 2, 3, 3]
14 3 2 0
After:  [1, 2, 3, 3]

Before: [2, 1, 0, 3]
2 0 1 2
After:  [2, 1, 1, 3]

Before: [3, 1, 2, 0]
2 0 2 0
After:  [1, 1, 2, 0]

Before: [3, 1, 0, 2]
14 0 2 0
After:  [1, 1, 0, 2]

Before: [2, 1, 3, 0]
2 0 1 1
After:  [2, 1, 3, 0]

Before: [1, 1, 1, 0]
9 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 0, 0, 0]
1 0 2 1
After:  [1, 0, 0, 0]

Before: [0, 3, 2, 2]
8 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 3, 2, 2]
2 0 2 0
After:  [1, 3, 2, 2]

Before: [0, 2, 1, 2]
5 2 1 1
After:  [0, 2, 1, 2]

Before: [3, 3, 2, 2]
2 0 2 3
After:  [3, 3, 2, 1]

Before: [0, 2, 1, 2]
5 2 1 0
After:  [2, 2, 1, 2]

Before: [1, 0, 2, 1]
10 3 2 2
After:  [1, 0, 1, 1]

Before: [0, 1, 0, 1]
13 1 3 2
After:  [0, 1, 1, 1]

Before: [3, 1, 1, 1]
14 2 1 1
After:  [3, 0, 1, 1]

Before: [0, 1, 0, 1]
13 1 3 1
After:  [0, 1, 0, 1]

Before: [2, 2, 0, 1]
3 0 3 2
After:  [2, 2, 1, 1]

Before: [3, 2, 1, 3]
14 3 0 0
After:  [1, 2, 1, 3]

Before: [1, 1, 2, 2]
4 1 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 2, 3]
7 1 3 1
After:  [3, 0, 2, 3]

Before: [3, 0, 3, 0]
15 2 2 1
After:  [3, 1, 3, 0]

Before: [0, 2, 2, 2]
14 2 1 3
After:  [0, 2, 2, 1]

Before: [1, 1, 2, 3]
12 1 2 1
After:  [1, 0, 2, 3]

Before: [3, 1, 1, 1]
13 1 3 1
After:  [3, 1, 1, 1]

Before: [2, 1, 1, 1]
13 1 3 3
After:  [2, 1, 1, 1]

Before: [2, 2, 2, 3]
7 2 3 3
After:  [2, 2, 2, 0]

Before: [2, 3, 3, 3]
15 0 0 2
After:  [2, 3, 1, 3]

Before: [3, 1, 2, 1]
13 1 3 3
After:  [3, 1, 2, 1]

Before: [3, 3, 3, 2]
15 0 2 0
After:  [1, 3, 3, 2]

Before: [3, 1, 0, 2]
0 3 3 0
After:  [0, 1, 0, 2]

Before: [2, 0, 3, 2]
14 0 1 1
After:  [2, 1, 3, 2]

Before: [1, 0, 2, 1]
10 3 2 3
After:  [1, 0, 2, 1]

Before: [1, 3, 3, 1]
0 3 3 2
After:  [1, 3, 0, 1]

Before: [0, 2, 2, 1]
10 3 2 2
After:  [0, 2, 1, 1]

Before: [2, 2, 1, 0]
5 2 1 0
After:  [2, 2, 1, 0]

Before: [2, 3, 0, 1]
3 0 3 2
After:  [2, 3, 1, 1]

Before: [1, 2, 2, 2]
6 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 1, 2, 2]
12 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 1, 0, 2]
9 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 1, 2, 2]
12 1 2 2
After:  [0, 1, 0, 2]

Before: [2, 1, 2, 0]
12 1 2 2
After:  [2, 1, 0, 0]

Before: [2, 3, 3, 0]
15 0 0 3
After:  [2, 3, 3, 1]

Before: [2, 2, 0, 1]
15 0 0 0
After:  [1, 2, 0, 1]

Before: [2, 0, 3, 2]
0 3 3 2
After:  [2, 0, 0, 2]

Before: [3, 0, 3, 2]
15 2 2 3
After:  [3, 0, 3, 1]

Before: [2, 3, 2, 1]
10 3 2 3
After:  [2, 3, 2, 1]

Before: [2, 1, 2, 1]
3 0 3 3
After:  [2, 1, 2, 1]

Before: [1, 3, 0, 0]
1 0 2 3
After:  [1, 3, 0, 0]

Before: [3, 1, 2, 3]
2 0 2 3
After:  [3, 1, 2, 1]

Before: [2, 1, 1, 2]
11 2 1 2
After:  [2, 1, 2, 2]

Before: [1, 3, 2, 3]
7 2 3 1
After:  [1, 0, 2, 3]

Before: [0, 0, 0, 0]
8 0 0 3
After:  [0, 0, 0, 0]

Before: [1, 0, 3, 1]
14 2 3 2
After:  [1, 0, 0, 1]

Before: [3, 2, 0, 3]
14 0 2 3
After:  [3, 2, 0, 1]

Before: [3, 2, 2, 1]
2 0 2 1
After:  [3, 1, 2, 1]

Before: [2, 1, 2, 1]
3 0 3 0
After:  [1, 1, 2, 1]

Before: [2, 2, 0, 1]
3 0 3 3
After:  [2, 2, 0, 1]

Before: [0, 3, 3, 2]
8 0 0 0
After:  [0, 3, 3, 2]

Before: [3, 2, 0, 1]
14 0 2 1
After:  [3, 1, 0, 1]

Before: [1, 1, 1, 3]
9 1 0 1
After:  [1, 1, 1, 3]

Before: [0, 1, 0, 1]
13 1 3 0
After:  [1, 1, 0, 1]

Before: [1, 1, 1, 0]
9 1 0 1
After:  [1, 1, 1, 0]

Before: [1, 3, 2, 2]
6 0 2 0
After:  [0, 3, 2, 2]

Before: [2, 1, 1, 1]
14 3 1 0
After:  [0, 1, 1, 1]

Before: [1, 1, 3, 0]
9 1 0 0
After:  [1, 1, 3, 0]

Before: [2, 1, 3, 1]
3 0 3 2
After:  [2, 1, 1, 1]

Before: [2, 1, 1, 1]
3 0 3 1
After:  [2, 1, 1, 1]

Before: [3, 2, 1, 3]
7 1 3 3
After:  [3, 2, 1, 0]

Before: [2, 0, 3, 3]
15 0 0 2
After:  [2, 0, 1, 3]

Before: [3, 0, 2, 1]
10 3 2 2
After:  [3, 0, 1, 1]

Before: [1, 1, 2, 3]
9 1 0 0
After:  [1, 1, 2, 3]

Before: [1, 2, 1, 1]
5 2 1 0
After:  [2, 2, 1, 1]

Before: [0, 1, 2, 3]
12 1 2 1
After:  [0, 0, 2, 3]

Before: [1, 3, 0, 1]
1 0 2 3
After:  [1, 3, 0, 0]

Before: [2, 1, 0, 1]
2 0 1 0
After:  [1, 1, 0, 1]

Before: [3, 2, 2, 3]
2 0 2 1
After:  [3, 1, 2, 3]

Before: [1, 2, 0, 1]
1 0 2 1
After:  [1, 0, 0, 1]

Before: [1, 2, 2, 0]
6 0 2 0
After:  [0, 2, 2, 0]

Before: [2, 1, 1, 2]
11 2 1 0
After:  [2, 1, 1, 2]

Before: [3, 1, 1, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [2, 2, 1, 3]
5 2 1 2
After:  [2, 2, 2, 3]

Before: [3, 1, 1, 1]
11 2 1 1
After:  [3, 2, 1, 1]

Before: [2, 1, 2, 2]
4 1 3 1
After:  [2, 0, 2, 2]

Before: [1, 1, 2, 1]
12 1 2 0
After:  [0, 1, 2, 1]

Before: [1, 1, 0, 2]
9 1 0 3
After:  [1, 1, 0, 1]

Before: [3, 3, 2, 3]
2 0 2 0
After:  [1, 3, 2, 3]

Before: [1, 1, 2, 3]
9 1 0 3
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
12 1 2 0
After:  [0, 1, 2, 1]

Before: [1, 1, 0, 2]
4 1 3 1
After:  [1, 0, 0, 2]

Before: [1, 2, 2, 0]
6 0 2 3
After:  [1, 2, 2, 0]

Before: [2, 1, 1, 0]
11 2 1 3
After:  [2, 1, 1, 2]

Before: [1, 1, 0, 1]
13 1 3 3
After:  [1, 1, 0, 1]

Before: [3, 1, 2, 3]
7 1 3 3
After:  [3, 1, 2, 0]

Before: [0, 2, 1, 3]
8 0 0 0
After:  [0, 2, 1, 3]

Before: [3, 2, 1, 3]
7 1 3 0
After:  [0, 2, 1, 3]

Before: [1, 2, 2, 2]
6 0 2 3
After:  [1, 2, 2, 0]

Before: [1, 1, 1, 1]
13 1 3 3
After:  [1, 1, 1, 1]

Before: [2, 1, 3, 2]
15 2 2 1
After:  [2, 1, 3, 2]

Before: [2, 1, 0, 3]
2 0 1 0
After:  [1, 1, 0, 3]

Before: [1, 1, 2, 1]
12 1 2 2
After:  [1, 1, 0, 1]

Before: [1, 1, 3, 2]
4 1 3 0
After:  [0, 1, 3, 2]

Before: [2, 3, 2, 3]
7 2 3 2
After:  [2, 3, 0, 3]

Before: [2, 2, 1, 1]
5 2 1 3
After:  [2, 2, 1, 2]

Before: [0, 0, 2, 1]
10 3 2 0
After:  [1, 0, 2, 1]

Before: [3, 1, 0, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [2, 1, 3, 2]
2 0 1 1
After:  [2, 1, 3, 2]

Before: [2, 3, 1, 1]
3 0 3 1
After:  [2, 1, 1, 1]

Before: [2, 2, 1, 3]
7 1 3 3
After:  [2, 2, 1, 0]

Before: [3, 3, 3, 1]
15 0 2 1
After:  [3, 1, 3, 1]

Before: [0, 1, 1, 0]
11 2 1 1
After:  [0, 2, 1, 0]

Before: [1, 1, 1, 0]
11 2 1 0
After:  [2, 1, 1, 0]

Before: [3, 1, 3, 1]
13 1 3 3
After:  [3, 1, 3, 1]

Before: [0, 1, 3, 2]
8 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 2, 0, 3]
7 1 3 3
After:  [2, 2, 0, 0]

Before: [1, 0, 2, 1]
6 0 2 2
After:  [1, 0, 0, 1]

Before: [1, 3, 0, 2]
0 3 3 3
After:  [1, 3, 0, 0]

Before: [1, 1, 0, 1]
9 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 2, 2, 3]
7 1 3 1
After:  [1, 0, 2, 3]

Before: [1, 1, 2, 2]
12 1 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 0]
12 1 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 0, 2]
4 1 3 1
After:  [0, 0, 0, 2]

Before: [1, 1, 1, 0]
9 1 0 0
After:  [1, 1, 1, 0]

Before: [1, 1, 2, 0]
9 1 0 0
After:  [1, 1, 2, 0]

Before: [1, 2, 1, 1]
5 2 1 3
After:  [1, 2, 1, 2]

Before: [3, 0, 3, 2]
15 2 2 0
After:  [1, 0, 3, 2]

Before: [2, 2, 1, 3]
7 2 3 3
After:  [2, 2, 1, 0]

Before: [3, 1, 2, 2]
4 1 3 3
After:  [3, 1, 2, 0]

Before: [3, 1, 2, 1]
15 0 0 1
After:  [3, 1, 2, 1]

Before: [2, 3, 2, 1]
10 3 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 2, 2]
0 3 3 1
After:  [2, 0, 2, 2]

Before: [1, 2, 0, 2]
1 0 2 1
After:  [1, 0, 0, 2]

Before: [3, 3, 2, 0]
2 0 2 0
After:  [1, 3, 2, 0]

Before: [0, 1, 1, 2]
11 2 1 1
After:  [0, 2, 1, 2]

Before: [3, 1, 2, 1]
13 1 3 1
After:  [3, 1, 2, 1]

Before: [3, 1, 3, 3]
15 2 0 3
After:  [3, 1, 3, 1]

Before: [0, 1, 0, 1]
8 0 0 3
After:  [0, 1, 0, 0]

Before: [2, 3, 2, 1]
0 3 3 3
After:  [2, 3, 2, 0]

Before: [2, 1, 1, 2]
4 1 3 2
After:  [2, 1, 0, 2]

Before: [0, 1, 3, 1]
13 1 3 0
After:  [1, 1, 3, 1]

Before: [2, 2, 1, 1]
5 2 1 0
After:  [2, 2, 1, 1]

Before: [3, 1, 2, 0]
15 0 0 0
After:  [1, 1, 2, 0]

Before: [1, 1, 1, 1]
9 1 0 0
After:  [1, 1, 1, 1]

Before: [1, 1, 2, 2]
12 1 2 2
After:  [1, 1, 0, 2]

Before: [1, 1, 2, 1]
10 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 0, 1, 1]
3 0 3 3
After:  [2, 0, 1, 1]



8 0 0 2
5 2 2 2
6 3 1 1
8 0 0 3
5 3 0 3
9 2 3 1
8 1 3 1
8 1 2 1
11 0 1 0
10 0 0 1
8 0 0 2
5 2 3 2
6 3 0 3
8 2 0 0
5 0 1 0
12 3 2 0
8 0 3 0
11 1 0 1
10 1 1 3
6 1 2 0
8 1 0 1
5 1 0 1
6 0 0 2
5 0 1 1
8 1 3 1
11 3 1 3
10 3 3 2
6 3 0 3
6 2 1 1
4 3 1 0
8 0 3 0
11 0 2 2
10 2 0 1
8 1 0 0
5 0 1 0
8 3 0 2
5 2 0 2
6 2 1 3
8 0 2 3
8 3 3 3
8 3 3 3
11 3 1 1
10 1 1 3
6 3 3 2
6 0 0 1
8 0 2 0
8 0 1 0
8 0 1 0
11 3 0 3
10 3 0 0
6 2 2 1
6 1 0 3
13 1 2 1
8 1 2 1
11 1 0 0
10 0 3 2
6 2 0 0
6 3 1 1
6 2 0 3
9 0 3 1
8 1 1 1
8 1 3 1
11 1 2 2
10 2 0 0
6 3 1 1
6 2 1 2
6 0 2 3
7 3 2 1
8 1 2 1
8 1 2 1
11 1 0 0
10 0 3 3
6 3 1 2
6 1 2 0
6 0 1 1
6 2 1 1
8 1 1 1
11 3 1 3
10 3 3 1
6 2 0 3
8 0 0 2
5 2 0 2
6 2 2 0
15 0 3 0
8 0 1 0
8 0 2 0
11 0 1 1
10 1 0 0
6 3 1 1
6 0 0 3
6 2 1 2
7 3 2 2
8 2 2 2
11 2 0 0
10 0 1 1
6 1 0 3
8 0 0 0
5 0 2 0
8 0 0 2
5 2 0 2
3 0 3 2
8 2 3 2
8 2 2 2
11 1 2 1
10 1 1 3
8 2 0 2
5 2 3 2
6 3 2 0
6 1 3 1
8 1 2 2
8 2 1 2
11 2 3 3
6 1 1 0
8 1 0 2
5 2 0 2
6 2 0 0
8 0 3 0
11 3 0 3
10 3 3 2
6 2 1 0
6 2 2 3
6 0 1 1
9 0 3 0
8 0 1 0
8 0 1 0
11 0 2 2
10 2 3 3
6 3 1 1
8 3 0 2
5 2 1 2
6 1 3 0
5 0 1 0
8 0 2 0
11 0 3 3
10 3 0 0
6 1 3 3
8 0 0 2
5 2 0 2
6 0 1 1
5 3 1 2
8 2 2 2
11 0 2 0
10 0 2 3
6 2 1 1
6 2 0 2
6 3 3 0
13 1 0 1
8 1 2 1
11 1 3 3
10 3 2 2
6 1 1 3
6 0 2 1
6 0 2 0
5 3 1 3
8 3 2 3
11 2 3 2
10 2 3 3
6 1 3 0
6 0 0 2
6 3 1 1
8 0 2 1
8 1 3 1
11 3 1 3
10 3 0 1
6 2 2 0
6 2 1 3
6 3 3 2
9 0 3 2
8 2 2 2
8 2 3 2
11 2 1 1
10 1 3 3
6 0 3 2
8 2 0 1
5 1 3 1
2 0 1 1
8 1 1 1
11 1 3 3
10 3 3 2
6 3 0 1
6 1 1 3
3 0 3 1
8 1 3 1
11 2 1 2
10 2 1 0
6 2 1 1
6 1 3 2
6 2 0 3
9 1 3 3
8 3 3 3
11 3 0 0
10 0 3 2
6 2 3 0
6 1 0 3
3 0 3 3
8 3 2 3
11 2 3 2
10 2 2 1
6 1 2 3
6 2 3 2
3 0 3 2
8 2 1 2
8 2 2 2
11 2 1 1
10 1 0 2
6 3 2 1
6 3 3 0
11 3 3 1
8 1 2 1
8 1 2 1
11 2 1 2
6 2 1 1
13 1 0 0
8 0 3 0
8 0 1 0
11 0 2 2
10 2 1 3
8 1 0 0
5 0 1 0
6 0 0 2
8 0 2 0
8 0 3 0
8 0 2 0
11 3 0 3
10 3 3 1
6 3 3 2
6 2 1 0
6 2 2 3
15 0 3 3
8 3 2 3
11 3 1 1
10 1 3 2
6 3 1 1
8 2 0 3
5 3 0 3
4 1 0 1
8 1 2 1
11 2 1 2
10 2 0 1
6 3 1 2
6 1 1 3
6 1 0 0
8 3 2 3
8 3 2 3
11 1 3 1
10 1 2 3
6 2 1 1
6 2 1 2
10 0 2 2
8 2 1 2
11 3 2 3
6 0 0 1
6 2 1 2
10 0 2 0
8 0 3 0
11 3 0 3
10 3 1 2
8 2 0 3
5 3 0 3
6 1 1 0
11 0 0 3
8 3 2 3
11 3 2 2
10 2 3 3
6 2 1 1
6 3 2 2
6 2 2 0
0 0 2 0
8 0 1 0
11 0 3 3
10 3 3 2
6 2 1 3
6 2 0 0
6 3 0 1
15 0 3 3
8 3 1 3
8 3 3 3
11 3 2 2
10 2 3 1
8 1 0 0
5 0 1 0
6 3 3 2
8 0 0 3
5 3 1 3
8 0 2 3
8 3 1 3
11 3 1 1
10 1 1 3
6 0 0 1
6 2 1 2
10 0 2 1
8 1 2 1
11 1 3 3
10 3 2 0
8 0 0 2
5 2 0 2
6 3 2 3
6 3 3 1
12 3 2 1
8 1 1 1
11 1 0 0
10 0 0 3
6 3 2 1
6 2 2 0
6 3 3 2
0 0 2 0
8 0 3 0
8 0 1 0
11 0 3 3
10 3 3 2
6 1 3 1
8 1 0 3
5 3 2 3
8 0 0 0
5 0 2 0
1 1 3 0
8 0 1 0
11 2 0 2
6 3 1 1
6 2 0 0
4 1 0 1
8 1 2 1
11 2 1 2
10 2 1 1
6 3 0 2
6 1 2 3
3 0 3 0
8 0 1 0
11 0 1 1
8 3 0 2
5 2 2 2
6 2 0 3
8 2 0 0
5 0 3 0
2 2 0 2
8 2 1 2
11 1 2 1
10 1 2 0
6 3 0 1
8 0 0 2
5 2 0 2
14 2 3 1
8 1 2 1
11 1 0 0
10 0 2 3
6 3 3 2
6 1 3 0
8 3 0 1
5 1 1 1
11 1 0 2
8 2 3 2
8 2 3 2
11 3 2 3
10 3 3 1
6 2 2 2
6 0 2 3
7 3 2 0
8 0 2 0
8 0 2 0
11 1 0 1
10 1 2 3
6 3 2 0
8 2 0 2
5 2 0 2
8 1 0 1
5 1 3 1
0 2 0 0
8 0 3 0
11 0 3 3
10 3 2 1
6 1 1 0
8 3 0 3
5 3 0 3
6 1 1 2
6 3 0 2
8 2 2 2
11 2 1 1
10 1 3 2
8 3 0 1
5 1 1 1
6 3 1 3
11 0 0 1
8 1 1 1
11 1 2 2
10 2 1 1
6 1 2 2
6 3 2 0
6 2 1 3
12 0 2 0
8 0 3 0
11 1 0 1
10 1 1 2
6 2 3 0
8 2 0 3
5 3 1 3
6 3 1 1
5 3 1 3
8 3 2 3
11 2 3 2
6 0 3 3
6 3 0 0
8 2 0 1
5 1 2 1
13 1 0 0
8 0 1 0
11 0 2 2
10 2 3 1
6 2 1 2
6 1 2 3
6 3 0 0
2 2 0 3
8 3 3 3
11 1 3 1
10 1 2 3
6 1 3 0
6 3 0 1
5 0 1 1
8 1 2 1
11 1 3 3
10 3 3 2
6 1 3 3
8 0 0 1
5 1 0 1
8 1 0 0
5 0 2 0
3 0 3 1
8 1 2 1
11 2 1 2
6 1 1 0
6 0 2 1
8 3 0 3
5 3 2 3
5 0 1 0
8 0 3 0
8 0 2 0
11 0 2 2
6 1 0 1
6 2 1 0
15 0 3 3
8 3 3 3
11 3 2 2
6 0 2 1
6 2 3 3
6 3 3 0
4 0 3 1
8 1 2 1
11 2 1 2
6 0 1 3
8 0 0 0
5 0 2 0
8 3 0 1
5 1 2 1
6 3 0 0
8 0 2 0
8 0 3 0
11 0 2 2
10 2 1 3
8 2 0 2
5 2 3 2
6 1 1 1
6 2 3 0
1 1 0 2
8 2 3 2
11 3 2 3
10 3 0 0
6 0 3 3
8 3 0 1
5 1 0 1
6 2 0 2
7 3 2 2
8 2 2 2
11 0 2 0
10 0 0 3
6 2 3 1
8 3 0 2
5 2 0 2
6 3 3 0
13 1 0 2
8 2 3 2
8 2 3 2
11 3 2 3
8 3 0 2
5 2 2 2
2 2 0 1
8 1 3 1
11 3 1 3
10 3 2 2
6 1 3 3
6 3 3 1
6 2 0 0
3 0 3 3
8 3 3 3
11 3 2 2
10 2 2 0
6 1 1 1
6 2 1 3
8 2 0 2
5 2 0 2
14 2 3 2
8 2 2 2
8 2 3 2
11 2 0 0
10 0 1 3
6 3 0 1
6 3 2 2
6 2 0 0
6 2 1 0
8 0 2 0
11 3 0 3
10 3 0 1
6 0 1 3
6 2 3 2
8 3 0 0
5 0 0 0
7 3 2 3
8 3 3 3
8 3 2 3
11 1 3 1
10 1 1 2
6 2 0 0
8 0 0 3
5 3 1 3
6 1 1 1
1 3 0 1
8 1 2 1
11 1 2 2
10 2 2 3
6 0 2 1
6 3 1 0
6 2 2 2
2 2 0 1
8 1 3 1
8 1 1 1
11 1 3 3
10 3 1 2
6 1 0 1
6 2 2 3
1 1 3 0
8 0 2 0
8 0 3 0
11 2 0 2
10 2 3 1
6 2 0 0
6 2 0 2
15 0 3 3
8 3 1 3
11 3 1 1
10 1 0 3
6 3 0 2
6 1 3 1
0 0 2 2
8 2 3 2
11 3 2 3
10 3 3 0
6 1 2 3
6 3 1 1
6 0 0 2
12 1 2 3
8 3 3 3
8 3 3 3
11 3 0 0
10 0 3 1
8 1 0 0
5 0 2 0
8 1 0 2
5 2 2 2
6 0 2 3
7 3 2 2
8 2 2 2
11 2 1 1
10 1 2 3
6 2 3 1
6 3 1 2
13 1 2 0
8 0 3 0
11 0 3 3
10 3 1 1
6 1 2 3
6 3 1 0
8 3 2 0
8 0 1 0
11 1 0 1
6 1 3 0
6 2 2 2
6 3 0 3
10 0 2 0
8 0 1 0
11 0 1 1
6 3 0 0
2 2 0 3
8 3 1 3
11 3 1 1
10 1 2 3
6 1 2 2
8 1 0 1
5 1 1 1
6 2 2 0
1 1 0 0
8 0 3 0
11 3 0 3
10 3 1 0
6 2 0 3
6 2 0 2
1 1 3 3
8 3 1 3
11 3 0 0
10 0 0 3
6 3 2 1
8 3 0 0
5 0 2 0
6 3 2 2
0 0 2 2
8 2 1 2
11 3 2 3
10 3 3 0
8 0 0 3
5 3 0 3
6 1 3 1
6 2 2 2
7 3 2 3
8 3 1 3
8 3 3 3
11 0 3 0
10 0 0 3
6 3 2 2
6 2 1 0
0 0 2 1
8 1 3 1
8 1 2 1
11 1 3 3
8 1 0 2
5 2 2 2
6 3 1 0
6 3 3 1
2 2 1 1
8 1 1 1
11 3 1 3
10 3 1 1
6 3 2 3
6 2 0 0
6 3 0 2
13 0 2 3
8 3 3 3
8 3 1 3
11 3 1 1
10 1 2 3
8 2 0 0
5 0 1 0
8 3 0 2
5 2 2 2
8 0 0 1
5 1 0 1
11 0 0 1
8 1 2 1
11 3 1 3
10 3 3 0
6 0 1 3
6 3 3 1
6 3 1 2
14 3 2 3
8 3 3 3
11 0 3 0
10 0 2 3
6 1 0 1
6 1 0 0
6 2 3 2
10 0 2 1
8 1 1 1
8 1 2 1
11 1 3 3
6 1 1 2
6 0 3 1
5 0 1 2
8 2 3 2
11 3 2 3
10 3 2 1
8 3 0 3
5 3 2 3
8 1 0 0
5 0 2 0
6 3 3 2
0 0 2 3
8 3 2 3
8 3 1 3
11 3 1 1
10 1 2 0
6 1 3 3
8 3 0 2
5 2 1 2
6 0 1 1
5 3 1 3
8 3 1 3
11 0 3 0
10 0 3 1
6 1 3 0
6 0 3 3
8 1 0 2
5 2 2 2
7 3 2 3
8 3 2 3
11 3 1 1
6 0 0 2
6 2 3 3
6 0 3 0
14 2 3 0
8 0 1 0
8 0 1 0
11 0 1 1
10 1 0 3
6 3 0 2
6 2 2 0
6 2 0 1
13 0 2 1
8 1 3 1
8 1 1 1
11 3 1 3
10 3 2 1
6 3 1 3
6 1 2 0
8 0 2 2
8 2 3 2
11 1 2 1
6 1 0 3
6 3 3 2
11 0 0 2
8 2 2 2
11 1 2 1
10 1 2 3
6 0 3 0
8 1 0 2
5 2 2 2
6 3 2 1
2 2 1 2
8 2 1 2
11 3 2 3
6 0 0 2
6 1 3 1
8 1 2 0
8 0 3 0
8 0 2 0
11 0 3 3
10 3 2 2
6 2 2 0
6 1 2 3
3 0 3 0
8 0 2 0
11 2 0 2
10 2 3 3
6 0 0 1
6 2 0 0
6 3 3 2
0 0 2 2
8 2 1 2
8 2 1 2
11 2 3 3
10 3 1 0
6 2 3 1
6 2 3 3
8 3 0 2
5 2 0 2
14 2 3 2
8 2 3 2
11 2 0 0
10 0 0 1
8 2 0 2
5 2 0 2
6 1 0 0
1 0 3 3
8 3 2 3
8 3 2 3
11 1 3 1
6 2 2 0
6 2 0 3
6 1 3 2
15 0 3 0
8 0 2 0
11 1 0 1
10 1 2 0
6 3 0 1
6 0 3 2
6 1 1 3
12 1 2 1
8 1 1 1
11 1 0 0
10 0 1 2
6 3 1 1
6 3 1 0
5 3 1 3
8 3 3 3
11 2 3 2
10 2 1 0
6 0 2 3
6 2 3 2
8 1 0 1
5 1 0 1
7 3 2 3
8 3 1 3
8 3 1 3
11 3 0 0
6 2 1 1
6 3 0 2
6 0 1 3
14 3 2 2
8 2 2 2
11 2 0 0
8 2 0 2
5 2 0 2
6 1 1 3
6 2 3 1
8 1 3 1
11 0 1 0
10 0 0 1
6 2 1 0
6 3 1 2
1 3 0 0
8 0 2 0
11 0 1 1
10 1 3 0
6 0 3 3
6 1 1 1
14 3 2 1
8 1 2 1
11 0 1 0
10 0 3 2
6 2 3 1
6 2 0 0
6 1 1 3
1 3 0 0
8 0 1 0
11 0 2 2
10 2 0 1
6 0 2 2
6 2 0 3
6 2 1 0
15 0 3 3
8 3 2 3
8 3 3 3
11 1 3 1
6 3 0 0
8 0 0 3
5 3 1 3
11 3 3 3
8 3 1 3
8 3 1 3
11 3 1 1
10 1 3 3
6 2 0 0
6 3 0 2
8 0 0 1
5 1 2 1
0 0 2 1
8 1 1 1
8 1 1 1
11 1 3 3
10 3 1 2
6 2 0 1
6 2 3 3
15 0 3 1
8 1 1 1
8 1 1 1
11 1 2 2
10 2 1 0
6 0 2 3
6 3 3 1
6 2 1 2
7 3 2 3
8 3 3 3
11 3 0 0
10 0 0 2
6 2 3 0
6 0 0 3
2 0 1 3
8 3 3 3
11 2 3 2
10 2 2 3
6 1 0 2
6 1 0 1
1 1 0 1
8 1 1 1
11 3 1 3
8 1 0 1
5 1 3 1
2 0 1 1
8 1 3 1
11 3 1 3
10 3 0 2
6 2 2 3
8 2 0 1
5 1 3 1
15 0 3 1
8 1 1 1
8 1 1 1
11 2 1 2
10 2 3 0
6 3 0 1
6 1 0 3
6 2 1 2
2 2 1 2
8 2 2 2
8 2 3 2
11 0 2 0
10 0 0 1
6 1 0 0
6 2 2 2
10 0 2 2
8 2 1 2
11 1 2 1
10 1 2 0
6 3 1 1
6 2 0 3
6 2 0 2
9 2 3 2
8 2 1 2
11 0 2 0
10 0 2 2
6 1 1 3
6 0 2 1
8 0 0 0
5 0 1 0
5 3 1 3
8 3 2 3
11 3 2 2
10 2 0 1
6 1 2 2
6 2 1 3
1 0 3 2
8 2 2 2
11 2 1 1
6 3 3 2
6 2 3 0
15 0 3 2
8 2 2 2
11 2 1 1
10 1 2 0
6 2 1 1
6 3 3 2
9 1 3 3
8 3 3 3
11 0 3 0
10 0 2 1
6 0 0 2
6 2 0 0
6 1 1 3
1 3 0 2
8 2 1 2
8 2 1 2
11 2 1 1
10 1 0 0
6 2 2 1
6 0 0 3
6 3 2 2
13 1 2 2
8 2 3 2
11 0 2 0
10 0 0 2
6 2 2 3
8 2 0 0
5 0 0 0
6 3 1 1
6 3 0 0
8 0 3 0
11 0 2 2
10 2 0 1
6 0 1 2
6 3 2 0
6 0 1 3
12 0 2 3
8 3 1 3
8 3 2 3
11 3 1 1
10 1 3 2
6 2 2 1
6 2 3 0
6 3 2 3
4 3 1 1
8 1 2 1
11 2 1 2
10 2 0 0
8 3 0 3
5 3 1 3
6 1 1 1
6 3 3 2
8 3 2 3
8 3 2 3
11 0 3 0
6 2 3 2
6 2 0 1
6 2 0 3
9 1 3 3
8 3 1 3
11 0 3 0
10 0 1 2
6 1 3 3
6 2 2 0
11 3 3 3
8 3 2 3
11 2 3 2
6 2 0 3
6 3 1 1
15 0 3 0
8 0 2 0
8 0 2 0
11 2 0 2
10 2 2 3
8 2 0 0
5 0 1 0
8 3 0 1
5 1 1 1
6 0 0 2
8 1 2 2
8 2 2 2
8 2 1 2
11 3 2 3
10 3 2 0"""



from typing import Tuple, List
Register = Tuple[int, int, int, int]
Instruction = Tuple[int, int, int, int]


def addr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] + r[b]
    return tuple(r)

def addi(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] + b
    return tuple(r)

def mulr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] * r[b]
    return tuple(r)

def muli(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] * b
    return tuple(r)

def banr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] & r[b]
    return tuple(r)

def bani(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] & b
    return tuple(r)

def borr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] | r[b]
    return tuple(r)

def bori(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] | b
    return tuple(r)

def setr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a]
    return tuple(r)

def seti(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = a
    return tuple(r)

def gtir(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if a > r[b] else 0
    return tuple(r)

def gtri(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] > b else 0
    return tuple(r)

def gtrr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] > r[b] else 0
    return tuple(r)

def eqir(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if a == r[b] else 0
    return tuple(r)

def eqri(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] == b else 0
    return tuple(r)

def eqrr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] == r[b] else 0
    return tuple(r)


instructions = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}


def get_matches(before: Register, after: Register, a: int, b: int, c: int) -> List[str]:
    ret: List[str] = []
    for name, instruction in instructions.items():
        e = instruction(before, a, b, c)
        if e == after:
            ret.append(name)
    return ret

count = 0
groupings = input.split("\n\n\n")[0].split("\n\n")
for grouping in groupings:
    lines = grouping.splitlines()
    before0, before1, before2, before3 = [int(x) for x in lines[0][9:-1].split(",", 3)]
    instruction0, instruction1, instruction2, instruction3 = [int(x) for x in lines[1].split(maxsplit=3)]
    after0, after1, after2, after3 = [int(x) for x in lines[2][9:-1].split(",", 3)]
    matches = get_matches(
        (before0, before1, before2, before3),
        (after0, after1, after2, after3),
        instruction1, instruction2, instruction3
    )
    if len(matches) >= 3:
        count += 1

print(count)