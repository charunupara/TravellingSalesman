# Find the minimum element of a list
def min_row(arr):
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

#TODO Write row reduction function
def row_reduce(graph):
    cost = 0
    for i in range(0, len(graph)):
        minRow = min_row(graph[i])
        for j in range(0, len(graph[i])):
            if(graph[i][j] != None):
                graph[i][j] -= minRow
        cost += minRow

    return cost


#TODO Write column reduction function
def column_reduce(graph):
    cost = 0
    for i in range(0, len(graph)):
        minColumn = min_column(graph, i)
        for j in range(0 ,len(graph)):
            if(graph[j][i] != None):
                graph[j][i] -= minColumn
        cost += minColumn
    
    return cost
    

#TODO Write function to block out appropriate row, column, and cell for calculating bound
#       * This function could return a new 2D array

# Graph from handout example
graph = [[None, 10, 8, 9, 7], 
        [10, None, 10, 5, 6], 
        [8, 10, None, 8, 9], 
        [9, 5, 8, None, 6],
         [7, 6, 9, 6, None]]


rc1 = min_row(graph[0]) + min_row(graph[1]) + min_row(graph[2]) + min_row(graph[3]) + min_row(graph[4])


print(row_reduce(graph))
print(column_reduce(graph))









