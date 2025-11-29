'''
Title:Ball Trajectory
Date:2025-11-29
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-29
Description:
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions

Examples:
1. get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) should return [2, 3].
Waiting:2. get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) should return [3, 0].
Waiting:3. get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) should return [1, 2].
Waiting:4. get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) should return [1, 1].
Waiting:5. get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) should return [2, 2].
'''
def get_next_location(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    # 找到 1 和 2 的位置
    pos1 = pos2 = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                pos1 = (r, c)
            elif grid[r][c] == 2:
                pos2 = (r, c)
            if pos1 and pos2:
                break
        if pos1 and pos2:
            break

    if pos1 is None or pos2 is None:
        raise ValueError("Grid must contain both a 1 (previous) and a 2 (current).")

    r1, c1 = pos1
    r2, c2 = pos2

    # 移动向量
    dr = r2 - r1
    dc = c2 - c1

    # 预测下一位置
    nr = r2 + dr
    nc = c2 + dc

    # 如果超出上下边界，竖直方向取反
    if nr < 0 or nr >= rows:
        dr = -dr
    # 如果超出左右边界，水平方向取反
    if nc < 0 or nc >= cols:
        dc = -dc

    # 用可能被反转后的方向计算最终下一位置
    next_r = r2 + dr
    next_c = c2 + dc

    return [next_r, next_c]

print(get_next_location([[0,0,0,0],
                         [0,0,0,0],
                         [0,1,2,0],
                         [0,0,0,0]]))   # [2, 3]

print(get_next_location([[0,0,0,0],
                         [0,0,1,0],
                         [0,2,0,0],
                         [0,0,0,0]]))   # [3, 0]

print(get_next_location([[0,2,0,0],
                         [1,0,0,0],
                         [0,0,0,0],
                         [0,0,0,0]]))   # [1, 2]

print(get_next_location([[0,0,0,0],
                         [0,0,0,0],
                         [2,0,0,0],
                         [0,1,0,0]]))   # [1, 1]

print(get_next_location([[0,0,0,0],
                         [0,0,0,0],
                         [0,0,1,0],
                         [0,0,0,2]]))   # [2, 2]
