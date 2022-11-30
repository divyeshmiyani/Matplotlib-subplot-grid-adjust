def xy(graph_required):
    x, y = 1, 1
    while x * y < graph_required:
        x, y = [x, y] if x < y else [y, x]
        x += 1
    return x, y
