def set_zeroes(matrix):
    if not matrix:
        return
    rows, cols = len(matrix), len(matrix[0])
    row_flags, col_flags = [False]*rows, [False]*cols
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_flags[i] = True
                col_flags[j] = True
    for i in range(rows):
        for j in range(cols):
            if row_flags[i] or col_flags[j]:
                matrix[i][j] = 0
    return matrix
