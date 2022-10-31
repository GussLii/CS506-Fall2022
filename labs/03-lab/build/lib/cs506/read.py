def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix=[]
    with open(csv_file_path) as file:
        for i in file:
            matrix.append(i)
    file.close()
    return matrix
            