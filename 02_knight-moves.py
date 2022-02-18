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

    delta = moves[move]
    delta_y, delta_x = delta

    new_y = y + delta_y
    new_x = x + delta_x

    dest = coords_2_index( (new_y, new_x) )

    if dest < 0 or dest > 63:
        return -1

    else:
        return dest


src = 20
print(make_move(src, 'lu'))



