# def manual_incrementing_matrix(n):
#     matrix = [[None for y in range(n)] for x in range(n)]

#     counter = 0

#     for idx, el in enumerate(matrix):
#         for nested_idx, nested_el in enumerate(el):
#             matrix[idx][nested_idx] = counter + nested_idx

#         counter += 1

#     return matrix


# print(manual_incrementing_matrix(5))


# def manual_matrix(grid_area):
#     matrix = []
#     counter = 0 

#     while counter < grid_area:
#         matrix.append(( [ x for x in range(counter, grid_area + counter)]))
#         counter += 1 

#     return matrix

# print(manual_matrix(5))


def manual_matrix(grid_area):
    starting_num = 0 
    initial_matrix = grid_area
    matrix = []

    while starting_num != initial_matrix:
        matrix.append(list(range(starting_num, grid_area)))
        starting_num += 1
        grid_area += 1

    return matrix

print(manual_matrix(5))
