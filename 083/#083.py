import heapq
#Dijkstra's Algorithm Some Taken Off The Internet
def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
    # Set Distance as Infinity
    distances = {(r, c): float('inf') for r in range(rows) for c in range(cols)}
    distances[(0, 0)] = grid[0][0]  # Start Node to Start Node is its own value
    # Priority queue using (distance, node)
    priority_queue = [(grid[0][0], (0, 0))]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == (len(grid)-1, len(grid[0])-1):
            return distances[(len(grid)-1, len(grid[0])-1)]
        for dr, dc in directions:
            new_row, new_col = current_node[0] + dr, current_node[1] + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                neighbor = (new_row, new_col)
                distance = current_distance + grid[new_row][new_col]
                # If a shorter path to neighbor update its distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
# Create a grid
with open("083/#083.txt","r") as f:
    grid = f.read().split("\n")
    for row in range(len(grid)):
        grid[row] = grid[row].split(",")
        for cell in range(len(grid[row])):
            grid[row][cell] = int(grid[row][cell])
print(dijkstra(grid))
