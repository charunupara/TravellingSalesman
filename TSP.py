# Find the minimum element of a list
def min_list(arr):
    return min(i for i in arr if i is not None)

#TODO Write row reduction function
#TODO Write column reduction function
#TODO Write function to block out appropriate row, column, and cell for calculating bound
#       * This function could return a new 2D array

# Graph from handout example
graph = [[None, 10, 8, 9, 7], 
        [10, None, 10, 5, 6], 
        [8, 10, None, 8, 9], 
        [9, 5, 8, None, 6],
         [7, 6, 9, 6, None]]


rc1 = min_list(graph[0]) + min_list(graph[1]) + min_list(graph[2]) + min_list(graph[3]) + min_list(graph[4])

print(rc1)

for i in range(0, len(graph)):
    min_row = min_list(graph[i])
    for j in range(0, len(graph[i])):
        if(graph[i][j] != None):
            graph[i][j] -= min_row





