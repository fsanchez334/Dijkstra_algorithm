class Node:
  def __init__(self, value, adjacent_nodes):
    self.value = value
    self.previous = None
    self.adjacent_nodes = adjacent_nodes 
    
node_b = Node("B", {})
node_a = Node("A", {})
node_c = Node("C", {})
node_d = Node("D", {})
node_e = Node("E", {})

node_a.adjacent_nodes = {node_b: 2, node_c:1}
node_b.adjacent_nodes = {node_a: 2, node_c:8, node_d: 3}
node_c.adjacent_nodes = {node_a: 2, node_b: 8, node_d: 6, node_e:2}
node_d.adjacent_nodes = {node_b: 3, node_c: 6, node_e: 7}
node_e.adjacent_nodes = {node_c: 2, node_d:7}

container = [node_b, node_c, node_d, node_e]

def dijkstras(beginning_node, list_of_nodes):
  #Declare visited and unvisited set
    #Visited will be empty
    #Unvisited will have the list of nodes
  
  #Declare your starting node

  #Declare your chart
    #When making your chart, set the values of the nodes equal to infinity
  
  visited = []
  unvisited = set(list_of_nodes)
  unvisited.add(beginning_node)
  current = beginning_node
  print("Unvisited", len(unvisited), unvisited)
  print("Visited", len(visited), visited)
  chart = {
    beginning_node: 0
  }
  
  for i in list_of_nodes:
    chart[i] = float('inf')

  #While loop continues until len of unvisited reaches 0
    #Look at the adjacent nodes of the current node
    #Look at the edge values of the adjacent nodes
      #If the edge values is less than the current value:
      #We set the current value to the edge value we calculated
    #Take current node and put it into the visited set
    #The current node will now become the node with the least value in the chart
  while len(unvisited) > 0:
    for nodes in current.adjacent_nodes.keys():      
      if chart[current] + current.adjacent_nodes[nodes] < chart[nodes]:
        chart[nodes] = chart[current] + current.adjacent_nodes[nodes]
    visited.append(current)
    print("Current: ", current.value)
    unvisited.remove(current)
    print("Unvisited", len(unvisited), unvisited)
    print("Visited", len(visited), visited)
    min = float('inf')
    for nodes in unvisited:
      if chart[nodes] < min and not nodes in visited:
        min = chart[nodes]
        current = nodes
        print(current.value)
  return chart

dijkstras(node_a, container)

