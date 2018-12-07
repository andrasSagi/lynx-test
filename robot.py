def robot_walk(matrix):
    collected = matrix[0][0]
    x = 0
    y = 0
    while x < len(matrix) or y < len(matrix[0]):
        if x == len(matrix) - 1:
            for i in range(y + 1, len(matrix[0])):
                collected += matrix[x][i]
            break
        if y == len(matrix[0]) - 1:
            for j in range(x + 1, len(matrix)):
                collected += matrix[j][y]
            break
        right = matrix[x][y+1]
        down = matrix[x+1][y]
        if right < down:
            collected += down
            x += 1
        else:
            collected += right
            y += 1
    return collected

