import numpy as np
class House():
    def __init__(self):
        self.house = np.array([["NAN", "", "", "", "NAN"],
                               ["", "", "", "", "NAN"],
                               ["NAN", "", "", "", "NAN"],
                               ["", "", "NAN", "", ""],
                               ["", "", "", "", ""],
                               ["", "", "", "", ""]])

    def __repr__(self):
        return f"""
                              7/3           
                         9/5   |   8/4      
                    6/4   |   6_{self.house[0][2]}_   |       
                     |   6_{self.house[0][1]}_   |   6_{self.house[0][3]}_      
                    5_{self.house[1][0]}_  |   5_{self.house[1][2]}_   |       
                     |   5_{self.house[1][1]}_   |   5_{self.house[1][3]}_      
                     |    |   4_{self.house[2][2]}_   |   3/2 
                     |   4_{self.house[2][1]}_   |   4_{self.house[2][3]}_   |  
                    3_{self.house[3][0]}_   |    |    |   3_{self.house[3][4]}_ 
                     |   3_{self.house[3][1]}_   |   3_{self.house[3][3]}_   |  
                    2_{self.house[4][0]}_   |   2_{self.house[4][2]}_   |   2_{self.house[4][4]}_ 
                     |   2_{self.house[4][1]}_   |   2_{self.house[4][3]}_   |  
                    1_{self.house[5][0]}_   |   1_{self.house[5][2]}_   |   1_{self.house[5][4]}_ 
                     |   1_{self.house[5][1]}_   |   1_{self.house[5][3]}_   |  
                     |    |    |    |    |  
                     =    =    =    =    =
"""

    def score(self):
        self.house1 = self.house.T
        for i in self.house1:
            if 1 in i:
                'выбираем большое число'
            else:
                'выбираем маленькое число'

    def put(self, number_tower, number_floor, number_item):
        self.house[6 - number_floor][number_tower - 1] = number_item

    def save(self):
        pass

    def load(self):
        pass
c = House()
print(c)
c.put(1, 5, 2)
print(c)