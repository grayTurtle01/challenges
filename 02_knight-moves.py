def index_2_coords(index):
    x = (index % 8) + 1
    y = (index // 8) + 1

    return (y, x)

