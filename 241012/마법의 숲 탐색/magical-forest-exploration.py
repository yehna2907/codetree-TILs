import heapq

R, C, K = map(int, input().split())

forest = [['.' for _ in range(C + 1)] for _ in range(R + 1)]


def in_forest(row, col):
    if 1 < row < R and 1 < col < C:
        return True
    else:
        return False


def rotate(exit):
    return (exit - 1) % 4


def check_down(row, col):
    if row >= R - 1:
        return False
    if forest[row+1][col-1] == '.' and forest[row+1][col+1] == '.' and forest[row+2][col] == '.':
        return True
    else:
        return False


def check_left(row, col):
    if row >= R - 1 or col <= 2:
        return False
    if forest[row-1][col-1] == '.' and forest[row][col-2] == '.' and forest[row+1][col-1] == '.'\
            and forest[row+1][col-2] == '.' and forest[row+2][col-1] == '.':
        return True
    else:
        return False


def check_right(row, col):
    if row >= R - 1 or col >= C - 1:
        return False
    if forest[row-1][col+1] == '.' and forest[row][col+2] == '.' and forest[row+1][col+1] == '.'\
            and forest[row+1][col+2] == '.' and forest[row+2][col+1] == '.':
        return True
    else:
        return False


total = 0
group_no = 1
groups = {}

# golam_r = [-1, 0, 0, 0, 1]
# golam_c = [0, -1, 0, 1, 0]

exit_r = [-1, 0, 1, 0]
exit_c = [0, 1, 0, -1]

for _ in range(K):
    c, d = map(int, input().split())
    current_r, current_c = -1, c

    while check_down(current_r, current_c):
        current_r = current_r + 1
    while check_left(current_r, current_c):
        current_r, current_c = current_r + 1, current_c - 1
        d = rotate(d)
    while check_right(current_r, current_c):
        current_r, current_c = current_r + 1, current_c + 1
        d = rotate(d)

    if not in_forest(current_r, current_c):
        forest = [['.' for _ in range(C + 1)] for _ in range(R + 1)]
        group_no = 1
        groups = {}
        continue

    d_r = current_r + exit_r[d]
    d_c = current_c + exit_c[d]
    connected = set()
    for i in range(4):
        n_r, n_c = d_r + exit_r[i], d_c + exit_c[i]
        if in_forest(n_r, n_c) and forest[n_r][n_c] != '.':
            connected.add(forest[n_r][n_c])

    current_group = group_no
    max_row = current_r + 1

    if len(connected) > 0:
        for i in connected:
            if not groups.get(i):
                continue
            if max_row <= -groups[i][0]:
                current_group = i
                max_row = -groups[i][0]
    else:
        group_no += 1

    if not groups.get(current_group):
        groups[current_group] = []

    total += max_row
    heapq.heappush(groups[current_group], -max_row)

    forest[current_r][current_c] = current_group

    for i in range(4):
        forest[current_r + exit_r[i]][current_c + exit_c[i]] = current_group

print(total)