# graph = {'A': ['B', 'C', 'D'],
#          'B': ['C', 'A'],
#          'C': ['B', 'E', 'D', 'A'],
#          'D': ['A', 'C', 'E', 'F'],
#          'E': ['D', 'C', 'F'],
#          'F': ['D', 'E']}
graph = {'A': ['B', 'D', 'C'],
         'B': ['E', 'A'],
         'C': ['D', 'G', 'A'],
         'D': ['G', 'C', 'A'],
         'E': ['F', 'B'],
         'F': ['I', 'E'],
         'G': ['D', 'H', 'C'],
         'H': ['I', 'G'],
         'I': ['J', 'H', 'F'],
         'J': ['I']}
graph2 = {'A': ['B', 'C', 'D'],
          'B': ['C', 'A'],
          'C': ['B', 'F', 'D', 'A'],
          'D': ['A', 'C', 'F', 'E'],
          'E': ['D', 'F', 'G'],
          'F': ['C', 'G', 'E', 'D'],
          'G': ['E', 'F']}


def graphSearch(start, goal, openlist, closelist, graph, path):
    openlist.append(start)
    # print(openlist)
    print(f'OPENLIST \t CURR \t CLOSELIST \t GoalTest')
    while (len(openlist)):
        curr = (openlist[0])
        openlist.pop(0)

        # print(curr)
        if curr not in closelist:
            closelist.append(curr)
        if curr == goal:
            GoalTest = True
            print(f" {openlist} | {curr:5}  |  {closelist} | {GoalTest}")
            break
        else:
            GoalTest = False
            childrens = graph[curr]
            # **** BFS
            # for child in childrens:
            #     if child not in openlist and child not in closelist:
            #         openlist.append(child)
            # **** BFS

            # **** DFS
            # a = childrens[::-1]
            # for child in a:
            #     if child not in openlist and child not in closelist:
            #         openlist.insert(0, child)
            # **** DFS
            print(f" {openlist} | {curr:5}  |  {closelist} | {GoalTest}")

            # print(f'{curr} \t {closelist} \t {openlist}')
            # print("Curr", curr)
            # print("Closelist: ",closelist)
            # print("Openlist: ", openlist)


    # print(openlist)
    # print(closelist)


start = 'A'
goal = 'J'
openlist = []
closelist = []
path = []
graphSearch(start, goal, openlist, closelist, graph, path)
# print(closelist)
# print(openlist)
# print(path)
