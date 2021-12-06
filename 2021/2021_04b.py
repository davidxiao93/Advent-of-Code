from typing import List

input = """83,69,34,46,30,23,19,75,22,37,89,78,32,39,11,44,95,43,26,48,84,53,94,88,18,40,62,35,27,42,15,2,91,20,4,64,99,71,54,97,52,36,28,7,74,45,70,86,98,1,61,50,68,6,77,8,57,47,51,72,65,3,49,24,79,13,17,92,41,80,63,67,82,90,55,0,10,93,38,21,59,73,33,31,9,76,5,66,16,58,85,87,12,29,25,14,96,56,60,81

68 73 98 51 49
82 56 87 64  8
46  7 21 38 30
66  5 86 97 74
60 63 76 55 39

92 20 87 77 52
72 29 81 24 64
26 16 19 79 68
 8 53 90 14 74
28 89 78 54 15

13 17 35  2 85
37 87 57 74 65
60 21 18 98 96
 4 51 46 84  0
90 75 80 41 64

83 98  4 78 45
90 62 71 68 39
47 81 96 73 43
 9 94 65 99 60
44  5 29 50  6

23 43 42 35  9
82 90 49 70 59
58 38 44 55 85
 3 99 88 65 61
71 53 17 37  4

58 38 47 84 89
60 87 80 92 75
57 83 40 62 25
11  7 33 76 70
82 31 53 56 90

96 40 50 21 38
58 77 64 98 86
 9 68 78 55 10
51 74 71 28 16
49 45 32  7 57

71 98 26  5 95
21 53 48 35 92
 4 90  9 45 82
67 28 33 34 58
85 41 80 64 19

98 36 33 34 55
15 81 97 56 96
91 73 32 63 83
31  3 85 80 38
71 93 87 86 27

19 15 97 31 26
56 58 54 87  1
 9 28 23  7 20
38 67 52 73 88
95 77 27 91 81

81 64 19 67 10
97 73 46 31  3
93 77  8  7 57
 0 28 87 42 66
17 79 58 14 18

43 17 63  7 49
28 27 31 23 41
65 34 51 70 77
73 56 74 96 72
94 86 48 71 40

97 43 56  0 30
60 71 34  1 96
10 72 28 82 84
36 22  9 20 67
 8 29 92  5 41

28 49  8 78 53
41 32  3  4 88
56 68 18 65 54
24  5 71 21 75
52 15 47 83 79

26 47  2 22  9
 6 81 53 17 88
58 25 55 31 19
42 27 85 97 14
64 52 66 63 51

80 43 88 42 51
17 18 84 60 24
34 48 89 33 10
 7 21 83  0 26
28 86 25 58 16

71 77  2 99 16
90 59 54 27 10
78 51 26 12 80
25 58 53 33 83
31  7 96 38 95

87 91  7 76  5
96  1 16 62 35
22 61 29 27 12
57 50 78  4 65
 3 97 73 82 94

93 63 43 22 71
12 74 41 64 62
81  2 37 99 27
26 39 66 30 20
77 78 18 53  5

72 61 21 59 41
18 49 95 51 30
63 75 10 47 27
83 11  8 39 68
 9 99 67 44 77

29 98 74 11 17
44 80  1 78  6
73 20 32  0 27
76 37 77 41 24
36 97 87 89 68

12 35 84 98 87
33 78 64 85  3
18 14 71 54 93
63 34 61 57 22
36 20 91 69 55

84 74 25 67 38
59 60 56 68 81
41 51 23 98 92
30 35 45 17 83
71 97 21  5 94

95 10 92 27 34
15 67 76 14 98
85 81 40 38 58
 8 17  6 59 48
78 73 84 11 46

25 50 40 69 27
89 59 17 86 20
 3 98 76 90  9
41 75 21 29 55
47 94 23  6 68

82 90 99 65 52
81 18 87 42  6
56 79 36 96 60
70 20 39 22 14
71 88 86 46 48

99 37 16 39 46
82 27 12 19 47
25 80 38 22 55
76  1  7 54 28
60 97 56 32 17

79  5 56 14 51
86 57 18 89 81
97 88 54 60 34
50 25 62 66 98
23 65 87 63 11

71 10  5 63 73
14 70  7 36 20
38 75 59 33 17
18  3 72 46 76
98 80 64 48 30

54 21 56 86 61
71 45 16  5 66
 0 12 94 70  1
37 98 26 93 18
87 90 24 44 91

18 10 72 81 48
67 80 42 25 33
92 34  0 27 26
77 99 57  9 46
82 15 54 21 52

73 18 80 27 50
58 97 84 81 21
94 68  8 57  9
56 98 67 36 92
86 53 35 41 89

86 65  2 74  5
 3 80 19 41 48
98 99 24 50 57
 8 59 53 67 91
62 83 72  9 14

56 69  7 38 87
39 71 84 41 88
23 94  1 97 33
73 14  2 79 72
26 91 45  9  6

17 40 97 51 57
92 25 38 26 23
32 44 83 87 49
54 74 33  7 12
14 36 30  8 98

56 26  3 73 32
90 80 23  0 27
59 19 33 78 52
21  1 20 86 34
85 48 37 97 67

23 13 90 35 44
30 96 18 14 92
80  5 97 11 58
12 50 33 65 78
48 26 86 15  7

70 32 62 92 13
23  1 21 50 59
79 26 11 65 76
90 54 64 63 31
 0 19 86 33  9

69 60  3 94 20
35 72 82 42 45
66  6 52 64 62
19 28 83  1 98
76 74 12  9 54

32 29 46 57 50
80 10 42 24 82
56 41 90  7 12
89 78 53 95  9
26 52 67 27 83

85 83  2 65 71
35 66 55 87 39
90 56 97 81  9
73 32 98 84 95
88 33 34 25 86

78  8 34 21 23
 2 86 10  4 58
31 62 35 91 63
81 90 69 15 47
41 12 61 72 36

10 95 68 87 25
59 45 54 92 82
34 81 12 61 83
89 69 98 72 44
84 20 51 36  1

59 94 26 76 54
39 21 86 13 48
58 61 75 80 62
 8 88 74 24 19
42 38 72 60 93

82 46 54 48 20
53 94 57 98 83
15 10 39 17 91
89 47  4 35 27
61 42 92 13  8

97 73  9 67 58
87 49 96 88 94
68 38 11 41 43
26 51  4 22  0
18  2 84 62 33

79 25 51 78 93
76 49 69 87 26
63 71 67 28 34
48 38 99 66 11
44 61 75 96 23

66 79 37 23 98
43 94 49 27 36
21 86 34 24 42
 4  8 85 63 32
74 82 68 92 72

12 77 87 53 76
71 66 10 68 36
74 49 27 16 34
98 21 54 93 18
95 61 97 65 32

60 91 68 11 76
66 62 65  3 41
 6 84 61 58 73
 7 28 63 75 55
35 45 98 47 81

85 75 46 45 58
95 92 73 99 47
25 97 76 15 23
19  5 37 36 65
96  8 24 49 61

53 60 16 94 59
10 47 82 17 89
86 91  1 40 45
34 76 38 97 63
25 85 57 27 93

77 95 20 24 93
37  4 23 39 35
81  2 56 18 87
46 75 52 51 50
88  8 83 80 27

20 47 27 52  2
97  0 17 64 11
53  9 69 88 77
13 89 28 21 36
71 33 31  6 68

45 25  6 18  7
51 84 82 83 81
13 65 34 93 71
87 92 49  8 24
76 29 53 96 58

15 41 65 85 29
78 30 93 98 67
36 58 12  1 25
 3 10 88  9 96
 8 53  7 14  6

78 37 50 99 51
42 19 40 62 54
89 38 64 70 56
96 72 41 43 95
90 91 17 28 59

23  5 45 80 93
14 75 78 25 86
21 24 73 30 34
39 74 22 19 49
72 31  1 77 57

59  8 57 68 32
71 19  9 29 63
 3 92 40 79 31
87 75 99 88  2
15 20 85 89 44

 7 41 16 15 46
76  5 51 11 38
28 70 68 91 66
56 94 59 34 86
72 80 42 75 65

92 95 48 65 89
27 64 69 15 33
93 47 30  7 63
91 35 29 42 72
90 23 11 50 54

97 17 66 92 91
81 23 12  6 93
48 25 27 16 54
21 32 50 94 98
15 55 40 11 84

66 56 95 44 33
26 11 41 22 86
 2  1 50 79 32
70 74 84  5 90
92  0  6 73 40

34 48 28 98 88
66 60 46 54 91
43 21 81 95 33
53 87 82 79 92
45 62 58 99 96

 6 16 70 86  9
19 95 37 96 62
 3 42 24 60 15
55 56 92 80 26
72 85 91 73 94

72 73 94 15  4
 3 40 67 21 84
45 33 60 82 10
48  6 29 79 70
27 66 13 38 47

31  0 56 89 61
62 49 37 73  1
63 68 38 83 44
70 17 69 14 81
72 58 52 50 79

46 18 61 11 14
51 58 94 98 69
 2  0 93  6 95
92 17  3 37 33
48 20 45 16 13

98 74 36 23  6
65 17 78 95 96
68 63 47 16 18
87 30 53 51 57
69 11 44 75 89

25 56  5 53  3
58  1 91  2 47
72 75 44 96 70
30 63 10 93 74
67 55 82 32 61

31 97 28 14 48
87 50 95 23 83
33 34  4 46 94
43 84 86 13 40
52 64 16 88 81

40 30 14 36 90
 2 25 12 10 33
18 27 78 73 60
11 92 52 69 93
19 22 35 17 61

42 45 49  8 14
21 18 69 12 27
25 76 63 28 64
52  7 77 58 39
87 89 88 38  4

40 57 53 48 46
13 59 23 55 61
 1 50 83 73 31
18 47 29 65 27
76 49 33 51 26

65 76 78 90 30
25 83  4 23  3
53 34 20 36 37
18 66 12 45 59
68 50 74 96 48

39 51 92  7 22
11 47 44 26 55
73 52 38 45 59
72 76 17 56 97
83 13 70 29 37

25 12 84 51 14
 2 22 85 13 10
73 93 67 72 80
56 90 60 42 61
36 16 50 70 97

 1 60 44 32 47
71 76 69 27 54
22 43 12 72  9
17 90 53 19 95
41 65 62 11 63

76 64 33  3 81
28 20 95 98 79
58 23 87 69 29
31 72 55 49 36
15 67 83 37 52

52 87 40 67 91
19  7 80 88 29
97 28 50 63 53
43 89 35 69 75
79 65 58 78 86

21 52 43 71 69
26 47 81 91 20
70 90  6 49 78
11 72 82 83  2
62 64 66 93 48

47 78 38 10 82
12 32 71 41 46
18 13 74 63 90
86 96 17 97  9
70  4 59 52  6

29 49 54 76  5
42 99 92 52 26
48 80 65  9 89
87 68 47 24 78
74  2 85 43 56

21  7 44 36  3
 0 72 66 28 74
99 68 83 53 30
96 81  4 69 23
15 20 31 41 42

87 78 21  6 62
68 95 30  5 20
81 54 42 50 70
18 39 93 35 72
22 97 73 74 75

25 24 62  5 54
85 31 88 40 76
48 44 15  3  4
61 47 56 72  9
11 49 50 78 39

54 30 52 70 16
63 49 91  3 51
71 36 46 79 67
80 66 31 57 43
45  9 84 17 35

68 41 32 23 24
95 62 87 97  5
16  2 48 17  1
59  9 35 96 22
50 70 44 89 31

21 35 47 36  2
33 49 77 39 60
70 91 97 18 66
25 95 22 87 20
69 27 76 52 11

42 40 26 61 98
33 88 79 72 73
 7 57 71  0 82
 2 21 74 63 41
58 96 50 13  4

80 84 96 31 38
58 75 19 91  6
10 54 52 66 81
55 35 47 23 69
95 40 21 17 79

58 68 27  0 81
49 51 93 83 23
 5 90  8 76 57
53 33 45 75 84
72 28 38 43 40

73 62 93 77 17
 4 89 82 85 18
33 57 58 55 49
48 11 94 14 72
 7 53 34 69 21

19 37 69 48 13
 5 14 46  2 86
40 87 95 79 36
81 62 70 23 82
51 43 91 29  9

70 16  3  5 38
62 85 19 15 41
36 42 13 31 87
58 66 27 49  6
82 54 91 23 10

67 63 60 80 66
16 30  2 85 97
45 52 62 21 49
83 75 76 10 82
47 90 72  5  9

 3 11 31 61 99
42 62 15 64 40
30 95  7 81 28
63 50 74 77 34
38 89 73  2 92

34 73 60 32 56
49 35 44 79 83
64 61 57  5 24
72 58  8 66 77
94 31 55 67 74

49 17 22 97 88
 0 16 14 93 31
28 73  6 82 90
80 45 92 55 78
 3 42 65 37 29

23 61 97  1 69
53 98 28 52 19
66 51 46 77 15
34 36 47 80 14
 7 89 62  9 49"""

"""
board positions
0  1  2  3  4 
5  6  7  8  9 
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
"""

drawn_values = [int(x) for x in input.splitlines()[0].split(",")]
input = input.splitlines()[2:]



wins = []
for i in range(5):
    wins.append(set([5*s + i for s in range(5)]))
    wins.append(set([5*i + s for s in range(5)]))


class Board:
    def __init__(self, values: List[List[int]]):
        self.pos = dict() # maps board value to position
        self.sum_of_all_values_on_board = 0
        for y, line in enumerate(values):
            for x, v in enumerate(line):
                self.pos[v] = 5*y + x
                self.sum_of_all_values_on_board += v
        self.drawn_positions = set()
        self.sum_of_drawn_values_on_board = 0

    def call(self, drawn: int):
        self.last_drawn = drawn
        if drawn in self.pos:
            self.drawn_positions.add(self.pos[drawn])
            self.sum_of_drawn_values_on_board += drawn

    def is_win(self) -> int:
        """
        returns -1 if not win, otherwise the score
        """
        for w in wins:
            if w.issubset(self.drawn_positions):
                return (self.sum_of_all_values_on_board - self.sum_of_drawn_values_on_board) * self.last_drawn
        return -1

boards = []

for i in range(0, len(input), 6):
    boards.append(Board([[int(x) for x in input[i + j].split()] for j in range(5)]))

last_drawn_pos = -1
last_win = -1
for b in boards:
    for i, v in enumerate(drawn_values):
        b.call(v)
        score = b.is_win()
        if score != -1:
            if last_drawn_pos < i:
                last_drawn_pos = i
                last_win = score
            break

print(last_win)