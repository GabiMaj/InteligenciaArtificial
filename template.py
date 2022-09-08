from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar,
    greedy,
)
from simpleai.search.viewers import WebViewer, BaseViewer


# (problema)
INICIAL = (0, 0, 0)
GOAL = (0, 0, 0)
# cada accion es una tupla: 
ACCIONES = (
    
)


class NombreProblem(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return state == GOAL

    def actions(self, state):
        acciones_disponibles = []
        return 1

    def result(self, state, action):
        return 1

    def heuristic(self, state):
        return 1

# if __name__ == "__main__":
#     viewer = BaseViewer()
#     #result = depth_first(NombreProblem(INICIAL), graph_search=True, viewer=viewer)
#     #result = breadth_first(NombreProblem(INICIAL), graph_search=True, viewer=viewer)
#     result = astar(NombreProblem(INICIAL), viewer=viewer)

#     for action, state in result.path():
#         print("Haciendo", action, "llegué a:")
#         print(state)

#     print("Profundidad:", len(list(result.path())))
#     print("Stats:")
#     print(viewer.stats)