
graph =[[0,1,0,0,0,0,0,0],
        [1,0,1,0,0,0,0,0],
        [0,1,0,1,0,0,0,0],
        [0,0,1,0,1,1,0,0],
        [0,0,0,1,0,1,1,0],
        [0,0,0,1,1,0,1,1],
        [0,0,0,0,1,1,0,1],
        [0,0,0,0,0,1,1,0]]

start = 2

def dfs(graph, start, visited = []):

  visited.append(start)

  for index in range(len(graph[start])):
    if graph[start][index] and not index in visited:
      dfs(graph, index, visited)
  
  return visited



a = dfs(graph, start)

for b in range(len(a)):
  a[b] += 1

print(a)
  