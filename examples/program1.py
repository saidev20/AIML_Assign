import random                                              
import os
import time
MAX_STEPS = 200
CLEAR_SCREEN = False
grid = [
    ['D', '.', '.'],
    ['.', '#', '.'],
    ['.', '.', 'D']
]
agent_pos = [0, 0]
rows, cols = len(grid), len(grid[0])
def neighbors(r, c):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            yield (nr, nc)
def find_path_to_nearest_dirt(start):
    from collections import deque
    q = deque([start])
    prev = {tuple(start): None}
    while q:
        cur = q.popleft()
        r, c = cur
        if grid[r][c] == 'D':
            # Reconstruct path
            path = []
            node = cur
            while node is not None:
                path.append(node)
                node = prev[tuple(node)]
            path.reverse()
            return path
        for nbr in neighbors(r, c):
            if tuple(nbr) not in prev:
                prev[tuple(nbr)] = cur
                q.append(nbr)
    return None
def show_grid(clear=CLEAR_SCREEN):
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(rows):
        for j in range(cols):
            cell = "A" if [i, j] == agent_pos else grid[i][j]
            print(cell, end=" ")
        print()
    print("_ _ _")
    time.sleep(0.2)
step = 0
while True:
    step += 1
    r, c = agent_pos
    if grid[r][c] == 'D':
        print(f"Step {step}: CLEAN")
        grid[r][c] = '.'
        show_grid(clear=False)
    else:
        path = find_path_to_nearest_dirt((r, c))
        valid_moves = []
        if r > 0 and grid[r-1][c] != '#':
            valid_moves.append('UP')
        if r < rows - 1 and grid[r+1][c] != '#':
            valid_moves.append('DOWN')
        if c > 0 and grid[r][c-1] != '#':
            valid_moves.append('LEFT')
        if c < cols - 1 and grid[r][c+1] != '#':
            valid_moves.append('RIGHT')
        if path and len(path) >= 2:
            nr, nc = path[1]
            if nr == r - 1 and nc == c:
                move = 'UP'
            elif nr == r + 1 and nc == c:
                move = 'DOWN'
            elif nr == r and nc == c - 1:
                move = 'LEFT'
            elif nr == r and nc == c + 1:
                move = 'RIGHT'
            else:
                move = random.choice(valid_moves) if valid_moves else None
        else:
            move = random.choice(valid_moves) if valid_moves else None
        if move is None:
            print(f"Step {step}: NO MOVE (stuck)")
            show_grid(clear=False)
            break
        print(f"Step {step}: MOVE {move}")
        if move == 'UP': agent_pos[0] -= 1
        elif move == 'DOWN': agent_pos[0] += 1
        elif move == 'LEFT': agent_pos[1] -= 1
        elif move == 'RIGHT': agent_pos[1] += 1
        show_grid(clear=False)
    if all(cell != 'D' for row in grid for cell in row):
        print("All dirt cleaned. Mission complete!")
        break
    if MAX_STEPS and step >= MAX_STEPS:
        print("Reached maximum steps")
        break

