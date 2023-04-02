def can_eat(c1,c2):
    x1 = c1[0]
    y1 = c1[1]
    y2 = c2[1]
    x2 = c2[0]
    if abs (x2-x1) + abs(y2-y1) == 3:
        return True
    else:
        return False
print('result =', can_eat((2,1),(4,2)))