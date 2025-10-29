from random import choice                       
def wins(b, p):
    s = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i]==p for i in line) for line in s)
def terminal(b):
    if wins(b,'X'): return 1
    if wins(b,'O'): return -1
    if all(c!=' ' for c in b): return 0
    return None
def moves(b):  return [i for i,c in enumerate(b) if c==' ']
def minimax(b, player):
    t = terminal(b)
    if t is not None: return t, None
    if player=='X':
        best = (-2, None)
        for m in moves(b):
            b[m]='X'
            score,_ = minimax(b,'O')
            b[m]=' '
            if score>best[0]: best=(score,m)
        return best
    else:
        best = (2, None)
        for m in moves(b):
            b[m]='O'
            score,_ = minimax(b,'X')
            b[m]=' '
            if score<best[0]: best=(score,m)
        return best
def print_board(b):
    for r in range(3): print(' | '.join(b[r*3:r*3+3]))
    print()
def play():
    board=[' ']*9
    cur = 'X' if input('Play first? (y/n) ').lower().startswith('y') else 'O'
    while True:
        print_board(board)
        t = terminal(board)
        if t is not None:
            print('Result:', 'X wins' if t==1 else 'O wins' if t==-1 else 'Draw')
            return
        if cur=='X':
            try: m = int(input('Move (0-8): '))       if board[m]!=' ': raise Exception
            except:  print('Invalid move')              continue
        else:
            _,m = minimax(board,'O')
            if m is None: m = choice(moves(board))     print('AI plays', m)
        board[m]=cur
        cur = 'O' if cur=='X' else 'X'
if __name__=='__main__':                              play()
