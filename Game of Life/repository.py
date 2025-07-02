class Repo:
    def __init__(self, file_name=""):
        self._file_name = file_name

    def read_from_file(self):
        matrix = []
        with open(self._file_name, 'r') as file:
            for line in file:
                row = line.strip().split(",")
                matrix.append(row)
        return matrix

    def set_file_name(self, pattern):
        self._file_name = pattern

    def save_to_file(self, table):
        """
        saves the current table to a file
        :param table: the table to save
        """
        with open("simulation.txt", 'w') as file:
            for row in table:
                file.write(",".join(row) + "\n")

    def load_from_file(self):
        """
        loads the table from a file
        :return: the table
        """
        table = []
        with open("simulation.txt", 'r') as file:
            for line in file:
                row = line.strip().split(",")
                table.append(row)
        return table
