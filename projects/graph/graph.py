"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) 
        else:
            print('ERROR ADDING EDGE: Vertex not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # might want to raise an exception here instead

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a q and enqueue starting vertex 
        qq = Queue()
        qq.enqueue([starting_vertex])
        # create a set of traversed vertices 
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue the first vertex 
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # do the thing!!!
                print(path[-1])
                # add vertex to visited 
                visited.add(path[-1])
                # enqueue all neighbors 
                for neighbor in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(neighbor)
                    qq.enqueue(new_path)

        pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack 
        # initialize the stack with the starting_vertex wrapped in an array 
        # create visited set()

        # while stack is not empty 
            # pop head of the stack 
            # check if last value in the popped array is in visited:
                # add popped vertex to visited
                # if not loop through the vertexes neighbors
                    # add all neighbors to the stack

        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            path = stack.pop()

            if path[-1] not in visited:
                visited.add(path[-1])
                print(path[-1])

                for neighbor in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        # create a recursion helper function that will take a visited 
        # array argument and a vertex argument 
            # if node not in visited
                # add node to visited array 

                # loop through the neighbors of the vertex 
                    # recursively call the recursion helper function on 
                    # each neighbor 

        def dft_helper(node, visited=set()):
            if node not in visited:
                visited.add(node)
                print(node)

                for neighbor in self.get_neighbors(node):
                    dft_helper(neighbor, visited)

        dft_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue and initialize the queue with the starting_vertex 
        # create a visited set() data structure

        # create a while loop that will terminate once the queue is empty 
            # dequeue the head of the queue 

            # if the dequeued node is not in visited set:
                # check if the node is the destination_vertex:
                    # if so return the path 

                # if not:
                    # loop through the neighbors of the current_node 
                    # enqueue each of the neighbors with their corresponding 
                    # paths 

        q = Queue()
        q.enqueue([starting_vertex])

        visited = set() 

        while q.size() > 0:
            path = q.dequeue()

            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path 

                else:
                    for neighbor in self.get_neighbors(path[-1]):
                        new_path = list(path) 
                        new_path.append(neighbor) 
                        q.enqueue(new_path)
      

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # first create a stack and initialize the stack with the 
        # starting vertex 

        # create a visited set() 

        # create a while loop that will terminate once the stack is 
        # empty 
            # pop the head off the stack 
            # see if the popped node is in visited:
                # if not:
                    # add node to visited set
                    # check if the popped node is equal to destination_vertex 
                        # if so return path 
                        # if not loop through the node's neighbors and push
                        # the neighbors in the stack 

        stack = Stack() 
        stack.push([starting_vertex]) 

        visited = set() 

        while stack.size() > 0:
            path = stack.pop() 

            if path[-1] not in visited:
                visited.add(path[-1]) 

                if path[-1] == destination_vertex:
                    return path 
                else:
                    for neighbor in self.get_neighbors(path[-1]):
                        new_path = list(path) 
                        new_path.append(neighbor) 
                        stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
