import tkinter as tk
import random
#from search import Node
from collections import deque
import time
class Node:
    def __init__(self, state, move=None, parent=None):
        self.state = state
        self.move = move
        self.parent = parent

def generate_random_state():
    numbers = list(range(9))
    random.shuffle(numbers)
    random_state = [numbers[i:i+3] for i in range(0, 9, 3)]
    return random_state
def is_goal(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal_state

def get_neighbors(node):
    neighbors = []

    zero_position = [(i, j) for i, row in enumerate(node.state) for j, value in enumerate(row) if value == 0][0]
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for move in moves:
        new_position = (zero_position[0] + move[0], zero_position[1] + move[1])

        if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:
            new_state = [row.copy() for row in node.state]
            new_state[zero_position[0]][zero_position[1]] = node.state[new_position[0]][new_position[1]]
            new_state[new_position[0]][new_position[1]] = 0
            neighbors.append((new_state, move))

    return neighbors

def breadth_first_search_gui(start_node):
    root = tk.Tk()
    root.title("Hamza First Assignment")

    canvas = tk.Canvas(root, width=300, height=300, bg="lightgray")
    canvas.pack()

    cell_size = 100
    delay = 1000

    queue = deque([start_node])
    visited = set()
    solution_found = False

    def draw_state(state):
        canvas.delete("all")
        for i, row in enumerate(state):
            for j, value in enumerate(row):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = (j + 1) * cell_size, (i + 1) * cell_size
                canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="lightblue")
                if value != 0:
                    canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(value), fill="red", font=("Arial", 16, "bold"))

        root.update()
        root.after(delay)

    while queue:
        current_node = queue.popleft()
        draw_state(current_node.state)

        if is_goal(current_node.state):
            print("Goal State Reached!")
            solution_found = True
            break

        if tuple(map(tuple, current_node.state)) not in visited:
            visited.add(tuple(map(tuple, current_node.state)))
            neighbors = get_neighbors(current_node)

            for neighbor, move in neighbors:
                new_node = Node(state=neighbor, move=move, parent=current_node)
                queue.append(new_node)

    if not solution_found:
        print("No Solution Found!")

    root.mainloop()


initial_state = [[1,2,3],[4,5,6],[0,7,8]]
initial_node = Node(state=initial_state)
start_time = time.time()
breadth_first_search_gui(initial_node)
end_time = time.time()
print("Time taken", int(end_time - start_time), "second")
