import queue

graph =[[0,1,0,0,0,0,0,0],
        [1,0,1,0,0,0,0,0],
        [0,1,0,1,0,0,0,0],
        [0,0,1,0,1,1,0,0],
        [0,0,0,1,0,1,1,0],
        [0,0,0,1,1,0,1,1],
        [0,0,0,0,1,1,0,1],
        [0,0,0,0,0,1,1,0]]

start = 2

def bfs(grap, start, q = None, visited = None):
  width = len(graph[0])
  if visited is None:
    q = queue.Queue()
    visited = [start]

  if len(visited) is width:
    return visited

  for index in range(width):
    if graph[start][index] and not index in visited:
      q.put(index)
      visited.append(index)

  return bfs(grap, q.get(), q, visited)


print(bfs(graph, start))