class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))



my_matrix = Matrix([[1, 36, 59, 1],
                    [6, 85, 88, 36],
                    [9, 0, 9, 22]],
                   [[56, 18, 2, 66],
                    [6, 7, 99, 99],
                    [15, 5, 100, 99]])

print(my_matrix.__add__())