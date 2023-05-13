# 10817
# A, B, C가 주어질때 두번째로 큰 정수 출력하기

def middle_num(a, b, c):
    if a >= b:
        if b >= c:
            return b
        
        else:
            if a >= c:
                return c
            else:
                return a
    
    elif b >= c:
        if c >= a:
            return c
        
        else:
            if b >= a:
                return a
            else:
                return b
        
    elif c >= a:
        if a >= b:
            return a
        
        else:
            if c >= b:
                return b
            else:
                return c

a, b, c = input().split(' ')
a, b, c = int(a), int(b), int(c)

print(middle_num(a, b, c))