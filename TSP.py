# Find the minimum element of a list
def min_row(arr):
    # TODO edge case: row only contains None
    return min(i for i in arr if i is not None)

# Find the minimum element of a column in a matrix
def min_column(graph, n):
    j = 0
    min = graph[j][n]
    while(min == None):
        j += 1
        min = graph[j][n]
    for i in range(1, len(graph)):
        if graph[i][n] != None: 
            if graph[i][n] < min:
                min = graph[i][n]

    return min        

# Perform and compute cost of row reduction
def row_reduce(graph):
    cost = 0
    for i in range(0, len(graph)):
        minRow = min_row(graph[i])
        for j in range(0, len(graph[i])):
            if(graph[i][j] != None):
                graph[i][j] -= minRow
        cost += minRow

    return cost


# Perform and compute cost of column reduction
def column_reduce(graph):
    cost = 0
    for i in range(0, len(graph)):
        minColumn = min_column(graph, i)
        for j in range(0 ,len(graph)):
            if(graph[j][i] != None):
                graph[j][i] -= minColumn
        cost += minColumn
    
    return cost
    

# Generate new matrix according to blocking
def generate_new_matrix(graph, n, m):
    new_matrix = graph.copy()

    for row in range(0, len(graph)):
        if(row == n):
            for j in range(0, len(graph[row])):
                new_matrix[row][j] = None
            
    for column in range(0, len(graph)):
        if (column == m):
            for j in range(0, len(graph)):
                new_matrix[j][column] = None


    new_matrix[m][0] = None

    return new_matrix


# Graph from handout example
graph = [[None, 10, 8, 9, 7], 
        [10, None, 10, 5, 6], 
        [8, 10, None, 8, 9], 
        [9, 5, 8, None, 6],
         [7, 6, 9, 6, None]]



rc = row_reduce(graph) + column_reduce(graph)
lb = rc


# Start walking from A
a_to_b = generate_new_matrix(graph, 0, 1)

print(row_reduce(a_to_b))
# First, compute minimum cost from A-B edge
# Then, add minimum cost from that to lb
# Repeat for every other edge
# Proceed with the edge that has the minimum combined cost


