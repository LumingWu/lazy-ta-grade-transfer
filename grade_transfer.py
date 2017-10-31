import csv

class csv_object:

    def __init__(self, path):
        file = open(path, "rt")
        try:
            reader = csv.reader(file, delimiter=",")
            self.rows = []
            for row in reader:
                self.rows.append(row)
                """
                if blackboard:
                    self.rows.append(row[0].split("\t"))
                else:
                    self.rows.append(row)
                """
        finally:
            file.close()

    def row_len(self):
        return len(self.rows)

    def col_len(self, row):
        return len(self.rows[row])
    
    def edit(self, row, col, val):
        self.rows[row][col] = val

    def get(self, row, col):
        return self.rows[row][col]

    def save(self, path="output.csv"):
        file = open(path, "wt", newline="")
        try:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            for row in self.rows:
                writer.writerow(row)
        finally:
            file.close()

class grade_transfer:
    
    """
    Modify csv file at path1 depending on the value of csv file at path2
    """
    def __init__(self, path1, path2):
        """
        self.csv1 = csv_object(path1, True)
        self.csv2 = csv_object(path2, False)
        """
        self.csv1 = csv_object(path1)
        self.csv2 = csv_object(path2)

    """
    Return the column index of a label
    """
    def get_column_index(self, column_name, first_csv=True):
        if first_csv:
            for i in range(0, self.csv1.col_len(0)):
                if self.csv1.get(0, i) == column_name:
                    return i
            return None
        for i in range(0, self.csv2.col_len(0)):
            if self.csv2.get(0, i) == column_name:
                return i
        return None
        
    """
    For each row i in the column match_col1 of csv1
        If its value matches a row j in column match_col2 of csv2
            tranfer / overwrite the value of row i in column transfer1 of csv1
                by the value of row j in column transfer2 of csv2
    If there exists a value in csv1 for row i in column transfer1, do nothing.
    If the value in csv2 is an empty string, fill 0 into csv1.
    """
    def transfer_by_column(self, match_col1, match_col2, transfer1, transfer2):
        for i in range(1, self.csv1.row_len()):
            val1 = self.csv1.get(i, transfer1)
            # Transfer grade only if the grade absent. This is safety measurement.
            if val1 == "" or "Needs Grading" or "In Progress":
                key1 = self.csv1.get(i, match_col1)
                for j in range(1, self.csv2.row_len()):
                    key2 = self.csv2.get(j, match_col2)
                    if key1 == key2:
                        val2 = self.csv2.get(j, transfer2)
                        # If no TA attendance, that is an 0.
                        if val2 == "":
                            self.csv1.edit(i, transfer1, 0)
                        else:
                            self.csv1.edit(i, transfer1, val2)
        self.csv1.save()
        
"""
A simple method that serves the purpose of this program.
"""
def transfer_grade(path1, path2, transfer1, transfer2):
    transfer = grade_transfer(path1, path2)
    match_col1 = transfer.get_column_index("Student ID", True)
    match_col2 = transfer.get_column_index("Student ID", False)
    transfer_col1 = transfer.get_column_index(transfer1, True)
    transfer_col2 = transfer.get_column_index(transfer2, False)
    transfer.transfer_by_column(match_col1, match_col2, transfer_col1, transfer_col2)
    
    
    
    
    
        
        
