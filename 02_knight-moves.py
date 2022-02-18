def index_2_coords(index):
    y = (index // 8) + 1
    x = (index % 8) + 1

    return (y, x)

def coords_2_index( coords ):
    y, x = coords 

    index = (y-1)*8 + (x-1)
    return index

moves = { 'ul' : (-2, -1),
          'ur' : (-2, 1),
          'ru' : (-1, 2),
          'rd' : (1, 2),
          'dr' : (2, 1),

          'dl' : (2, -1),
          'ld' : (1, -2),
          
          'lu' : (-1, -2)
        }

def make_move(src, move):
    coords = index_2_coords(src)
    y, x = coords

    #print(coords)

    delta = moves[move]
    delta_y, delta_x = delta

    #print(delta)

    new_y = y + delta_y
    new_x = x + delta_x

    if new_y <= 0 or new_x <= 0 or new_y > 8 or new_x > 8:
        return -1

    dest = coords_2_index( (new_y, new_x) )

    if dest < 0 or dest > 63:
        return -1

    else:
        return dest


import random

def search_random_path(src, dest):

    keys = list(moves.keys())
    path = [src]
    
    while dest not in path:
        # select random move
        random_index = random.randint(0,7) 
        move = keys[random_index] 

        new_index = make_move(src, move)

        if new_index >= 0:

            #if new_index not in path:
            path.append(new_index)
            src = new_index
            #print(path)
                
            if new_index == dest:
                break
            
    
    return path

def search_short_path(src, dest):
    short_path = list(range(100))

    for i in range(100):
       new_path = search_random_path(src, dest)
       if len(new_path) < len(short_path):
           short_path = new_path 

    return short_path

def sandbox(src):
    for move in moves.keys():
        index = make_move(src, move)
        print(index)

src = 22
dest = 63

sandbox(src)
#print( make_move(src, 'dl') )

#print(search_random_path(src, dest))

#print(search_short_path(src, dest))


