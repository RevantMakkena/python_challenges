from typing import Counter


class Matrix:
    def __init__(self, matrix_string):
        self.raw_string = matrix_string
        self.total_rows = self.calculateTotalRows()
        self.total_columns = self.calculateTotalColumns()
        # print(f"rows are {self.total_rows}")
        # print(f"columns are {self.total_columns}")

    def row(self, index):
        print(self.raw_string[self.total_rows*index-1:self.total_rows+2])

    def column(self, index):
        pass

    def calculateTotalRows(self):
        return sum([1 if i == '\n' else 0 for i in self.raw_string])+1

    def calculateTotalColumns(self):
        count = 0
        for i in self.raw_string:
            if i == '\n':
                break

            if i != ' ':
                count += 1
        return(count)


x = Matrix("1 2 3\n4 5 6\n7 8 9")
x.row(2)
# 1 2 3
# 4 5 6
# 7 8 9
