SCORES = [[6, 4], [9, 5], [7, 3], [8, 4], [3, 2]]
ITEMS = ["_домик_", "клубок_", "бабочка", "_миска_", "подушка", "_мышка_"]
class House():
    def __init__(self):
        self.house = [["NAN", "", "", "", "NAN"],
                      ["", "", "", "", "NAN"],
                      ["NAN", "", "", "", "NAN"],
                      ["", "", "NAN", "", ""],
                      ["", "", "", "", ""],
                      ["", "", "", "", ""]]

    def item(self, i, g):
        if type(self.house[i][g]) == int:
            return (ITEMS[self.house[i][g] - 1])
        else:
            return "_______"

    def __repr__(self):
        return f"""  
                             7/3
                 9/5          |           8/4
   6/4           |         6_{self.item(0, 2)}_      |
    |         6_{self.item(0, 1)}_      |         6_{self.item(0, 3)}_
 5_{self.item(1, 0)}_      |         5_{self.item(1, 2)}_      |
    |         5_{self.item(1, 1)}_      |         5_{self.item(1, 3)}_
    |            |         4_{self.item(2, 2)}_      |           3/2
    |         4_{self.item(2, 1)}_      |         4_{self.item(2, 3)}_      |
 3_{self.item(3, 0)}_      |            |            |         3_{self.item(3, 4)}_
    |         3_{self.item(3, 1)}_      |         3_{self.item(3, 3)}_      |
 2_{self.item(4, 0)}_      |         2_{self.item(4, 2)}_      |         2_{self.item(4, 4)}_
    |         2_{self.item(4, 1)}_      |         2_{self.item(4, 3)}_      |
 1_{self.item(5, 0)}_      |         1_{self.item(5, 2)}_      |         1_{self.item(5, 4)}_
    |         1_{self.item(5, 1)}_      |         1_{self.item(5, 3)}_      |
    |            |            |            |            |
    =            =            =            =            =
"""
#                     7/3
#            9/5       |       8/4
#   6/4       |     6_{self.item(0, 2)}_      |
#    |     6_{self.item(0, 1)}_      |     6_{self.item(0, 3)}_
# 5_{self.item(1, 0)}_      |     5_{self.item(1, 2)}_      |
#    |     5_{self.item(1, 1)}_      |     5_{self.item(1, 3)}_
#    |        |     4_{self.item(2, 2)}_      |       3/2
#    |     4_{self.item(2, 1)}_      |     4_{self.item(2, 3)}_      |
# 3_{self.item(3, 0)}_      |        |        |     3_{self.item(3, 4)}_
#    |     3_{self.item(3, 1)}_      |     3_{self.item(3, 3)}_      |
# 2_{self.item(4, 0)}_      |     2_{self.item(4, 2)}_      |     2_{self.item(4, 4)}_
#    |     2_{self.item(4, 1)}_      |     2_{self.item(4, 3)}_      |
# 1_{self.item(5, 0)}_      |     1_{self.item(5, 2)}_      |     1_{self.item(5, 4)}_
#    |     1_{self.item(5, 1)}_      |     1_{self.item(5, 3)}_      |
#    |        |        |        |        |
#    =        =        =        =        =


#                              7/3
#                         9/5   |   8/4
#                    6/4   |   6_{self.item(0, 2)}_   |
#                     |   6_{self.item(0, 1)}_   |   6_{self.item(0, 3)}_
#                    5_{self.item(1, 0)}_  |   5_{self.item(1, 2)}_   |
#                     |   5_{self.house[1][1]}_   |   5_{self.house[1][3]}_
#                     |    |   4_{self.house[2][2]}_   |   3/2
#                     |   4_{self.house[2][1]}_   |   4_{self.house[2][3]}_   |
#                    3_{self.house[3][0]}_   |    |    |   3_{self.house[3][4]}_
#                     |   3_{self.house[3][1]}_   |   3_{self.house[3][3]}_   |
#                    2_{self.house[4][0]}_   |   2_{self.house[4][2]}_   |   2_{self.house[4][4]}_
#                     |   2_{self.house[4][1]}_   |   2_{self.house[4][3]}_   |
#                    1_{self.house[5][0]}_   |   1_{self.house[5][2]}_   |   1_{self.house[5][4]}_
#                     |   1_{self.house[5][1]}_   |   1_{self.house[5][3]}_   |
#                     |    |    |    |    |
#                     =    =    =    =    =


    def score(self):
        s = 0
        s += self.score_1()
        s += self.score_2()
        s += self.score_3()
        s += self.score_4()
        s += self.score_5()
        s += self.score_6()

    def score_1(self):
        s = 0
        for i in range(5):
            w = []
            for g in self.house:
                w.append(g[i])
            if "" in w:
                s += 0
            elif 1 in w:
                s += SCORES[i][0]
            else:
                s += SCORES[i][1]
        return s

    def score_2(self):
        pass

    def score_3(self):
        pass

    def score_4(self):
        s = 0
        for i in range(5):
            w = []
            for g in self.house:
                w.append(g[i])
            while 4 in w:
                a = [w.index(4), self.house.index(g)]
                if (self.house[a[1]-1][a[0]] == 1 and 0 <= a[1]-1 <= 5 and 0 <= a[0] <= 4) or (self.house[a[1]][a[0]-1] == 1 and 0 <= a[1] <= 5 and 0 <= a[0]-1 <= 4) or (self.house[a[1]][a[0]+1] == 1 and 0 <= a[1] <= 5 and 0 <= a[0]+1 <= 4) or (self.house[a[1]+1][a[0]-1] == 1 and 0 <= a[1]+1 <= 5 and 0 <= a[0]-1 <= 4) or (self.house [a[1]+1][a[0]+1] == 1 and 0 <= a[1]+1 <= 5 and 0 <= a[0]+1 <= 4):
                    s += 1
                if (self.house[a[1]-1][a[0]] == 2 and 0 <= a[1]-1 <= 5 and 0 <= a[0] <= 4) or (self.house[a[1]][a[0]-1] == 2 and 0 <= a[1] <= 5 and 0 <= a[0]-1 <= 4) or (self.house[a[1]][a[0]+1] == 2 and 0 <= a[1] <= 5 and 0 <= a[0]+1 <= 4) or (self.house[a[1]+1][a[0]-1] == 2 and 0 <= a[1]+1 <= 5 and 0 <= a[0]-1 <= 4) or (self.house [a[1]+1][a[0]+1] == 2 and 0 <= a[1]+1 <= 5 and 0 <= a[0]+1 <= 4):
                    s += 1
                if (self.house[a[1]-1][a[0]] == 3 and 0 <= a[1]-1 <= 5 and 0 <= a[0] <= 4) or (self.house[a[1]][a[0]-1] == 3 and 0 <= a[1] <= 5 and 0 <= a[0]-1 <= 4) or (self.house[a[1]][a[0]+1] == 3 and 0 <= a[1] <= 5 and 0 <= a[0]+1 <= 4) or (self.house[a[1]+1][a[0]-1] == 3 and 0 <= a[1]+1 <= 5 and 0 <= a[0]-1 <= 4) or (self.house [a[1]+1][a[0]+1] == 3 and 0 <= a[1]+1 <= 5 and 0 <= a[0]+1 <= 4):
                    s += 1
                if (self.house[a[1]-1][a[0]] == 4 and 0 <= a[1]-1 <= 5 and 0 <= a[0] <= 4) or (self.house[a[1]][a[0]-1] == 4 and 0 <= a[1] <= 5 and 0 <= a[0]-1 <= 4) or (self.house[a[1]][a[0]+1] == 4 and 0 <= a[1] <= 5 and 0 <= a[0]+1 <= 4) or (self.house[a[1]+1][a[0]-1] == 4 and 0 <= a[1]+1 <= 5 and 0 <= a[0]-1 <= 4) or (self.house [a[1]+1][a[0]+1] == 4 and 0 <= a[1]+1 <= 5 and 0 <= a[0]+1 <= 4):
                    s += 1
                if (self.house[a[1]-1][a[0]] == 5 and 0 <= a[1]-1 <= 5 and 0 <= a[0] <= 4) or (self.house[a[1]][a[0]-1] == 5 and 0 <= a[1] <= 5 and 0 <= a[0]-1 <= 4) or (self.house[a[1]][a[0]+1] == 5 and 0 <= a[1] <= 5 and 0 <= a[0]+1 <= 4) or (self.house[a[1]+1][a[0]-1] == 5 and 0 <= a[1]+1 <= 5 and 0 <= a[0]-1 <= 4) or (self.house [a[1]+1][a[0]+1] == 5 and 0 <= a[1]+1 <= 5 and 0 <= a[0]+1 <= 4):
                    s += 1
                if (self.house[a[1]-1][a[0]] == 6 and 0 <= a[1]-1 <= 5 and 0 <= a[0] <= 4) or (self.house[a[1]][a[0]-1] == 6 and 0 <= a[1] <= 5 and 0 <= a[0]-1 <= 4) or (self.house[a[1]][a[0]+1] == 6 and 0 <= a[1] <= 5 and 0 <= a[0]+1 <= 4) or (self.house[a[1]+1][a[0]-1] == 6 and 0 <= a[1]+1 <= 5 and 0 <= a[0]-1 <= 4) or (self.house [a[1]+1][a[0]+1] == 6 and 0 <= a[1]+1 <= 5 and 0 <= a[0]+1 <= 4):
                    s += 1
                w[w.index(4)] = ""
        return s


    def score_5(self):
        s = 0
        for i in range(5):
            w = []
            for g in self.house:
                w.append(g[i])
            while 5 in w:
                s += 6 - w.index(5)
                w[w.index(5)] = ""
        return s

    def score_6(self):
        pass

    def put(self, number_tower, number_floor, number_item):
        self.house[6 - number_floor][number_tower - 1] = number_item

    def save(self):
        pass

    def load(self):
        pass