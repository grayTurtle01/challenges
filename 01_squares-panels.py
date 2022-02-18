def solution(area):
    squares = []

    while( area >= 1):
            
        lenght = 1
        square = 1
        
        for i in range(area):
            if  i * i > area:
                lenght = i - 1
                break

        area = area - (lenght*lenght)
                
        squares.append( lenght* lenght)

    return squares         

print( solution(15324) )

