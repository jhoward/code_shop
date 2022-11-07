import os

def load_data(year, problem):
    """
    Load the data for a given year and problem
    """
    file_name = "aoc_" + str(year) + "_" + str(problem) + ".txt"
    file_name = os.path.join(".", "data", str(year), file_name)
    with open(file_name) as file:
        return_data = [str(line).strip() for line in file]

    return return_data

def peek(data):
    print(data[0:5])