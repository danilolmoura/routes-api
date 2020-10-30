FILE_PATH = 'files/input-routes.csv'

def add_line(initial_position, final_position, weight):
    with open(FILE_PATH, 'a') as f:
        new_line = '\n{},{},{}'.format(initial_position, final_position, weight)
        f.write(new_line)



