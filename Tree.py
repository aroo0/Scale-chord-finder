from collections import deque

class TreeNode:
  # Classic implementation
  def __init__(self, value):
    self.value = value
    self.children = []

  
  def __repr__(self):
     return str(self.value)

  def add_child(self, child_node):
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children




def bfs(root_node, goal_value):
  # Classic Breadth-first search algorithm
  path_queue = deque()
  list_with_paths = []
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  while path_queue:
    current_path = path_queue.pop()
    current_node = current_path[-1]

    if goal_value in current_node.value:
      list_with_paths.append(current_path)

    for child in current_node.children:
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path)

  return list_with_paths


  