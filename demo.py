# Easy calculation of the move
def calcMoveEasy(xi):
    a = 22695477
    b = 1
    m = 2**32
    xi_plus1 = (a*xi + b) % m
    if(xi_plus1 <= 2**31):
        comp_move = 0
    else:
        comp_move = 1
    return xi_plus1, comp_move