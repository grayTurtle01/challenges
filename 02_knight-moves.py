def index_2_coords(index):
    y = (index // 8) + 1
    x = (index % 8) + 1

    return (y, x)

def coords_2_index( coords ):
    y, x = coords 

    index = (y-1)*8 + (x-1)
    return index

    


