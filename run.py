# Search methods


import search


print("--------------------------------------------------------------")
ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())

print("AQUI VEREMOS TODO A - B")
print(search.otra_first_graph_search(ab).path())
print(search.otra2_first_graph_search(ab).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

print("--------------------------------------------------------------")


print("--------------------------------------------------------------")
ab = search.GPSProblem('S', 'G'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())

print("\nAQUI VEREMOS TODO S - G\n")
print(search.otra_first_graph_search(ab).path())
print(search.otra2_first_graph_search(ab).path())
# Result:
# [<Node G>, <Node B>, <Node P>, <Node R>, <Node S>] : 90 + 101 + 97 + 80  = 368
# [<Node G>, <Node B>, <Node F>, <Node S>] : 90 + 211 + 99 = 400

print("--------------------------------------------------------------")

