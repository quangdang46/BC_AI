from fringes import Stack, Queue, PriorityQueue
from problems import SingleFoodSearchProblem,MultiFoodSearchProblem


def bfs(problem):
    fringe = Queue()
    fringe.push((problem.getStartState(), []))
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.pop()
        if node not in visited:
            visited.add(node)
            successors = reversed(problem.getSuccessors(node))
            for child, action, cost in successors:
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.delete_elements(fringe.size())
                fringe.push((node, []))
                if problem.getNumFood() == 0:
                    return temp
    return []


def dfs(problem):
    fringe = Stack()
    fringe.push((problem.getStartState(), []))
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.pop()
        if node not in visited:
            visited.add(node)
            successors = reversed(problem.getSuccessors(node))
            for child, action, cost in successors:
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.delete_elements(fringe.size())
                fringe.push((node, []))
                if problem.getNumFood() == 0:
                    return temp
    return []

def ucs(problem):
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.get()
        if node not in visited:
            visited.add(node)
            for child, action, cost in problem.getSuccessors(node):
                x,y=child
                if problem.isValidMove(x,y) and child not in visited:
                    fringe.push((child, actions + [action]), problem.getCostOfActions(actions + [action]))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.clear_priority_queue()
                fringe.push((node, []), 0)
                if problem.getNumFood() == 0:
                    return temp
    return []
# yc21
def manhattanHeuristic(state, problem):
    if isinstance(problem, MultiFoodSearchProblem):
        food = problem.goalState
        x_f, y_f = food[0]
    else:
        x_f, y_f = problem.goalState
    x, y = state
    return abs(x-x_f) + abs(y-y_f)

def euclideanHeuristic(state, problem):
    if isinstance(problem, MultiFoodSearchProblem):
        food = problem.goalState
        x_f, y_f = food[0]
    else:
        x_f, y_f = problem.goalState
    x, y = state
    return ((x-x_f)**2 + (y-y_f)**2)**0.5
# yc22

def foodHeristic(state, problem):
    def getDistance(x1, y1, x2, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
    x,y=state
    if isinstance(problem,SingleFoodSearchProblem):
        x_f,y_f=problem.goalState
        return getDistance(x,y,x_f,y_f)
    else:
        return min([getDistance(x,y,x_f,y_f) for x_f,y_f in problem.goalState])

def astar(problem, fn_heuristic):
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.get()
        if node not in visited:
            visited.add(node)
            for child, action, cost in problem.getSuccessors(node):
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]),
                    problem.getCostOfActions(actions + [action]) + fn_heuristic(child, problem))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.clear_priority_queue()
                fringe.push((node, []), 0)
                if problem.getNumFood() == 0:
                    return temp
    return []

def gbfs(problem, fn_heuristic):
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.get()
        if node not in visited:
            visited.add(node)
            for child, action, cost in problem.getSuccessors(node):
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]), fn_heuristic(child, problem))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.clear_priority_queue()
                fringe.push((node, []), 0)
                if problem.getNumFood() == 0:
                    return temp

    return []


# # Thực hiện chạy code

# # Đọc file
# pacman_single_01 = SingleFoodSearchProblem("./sample_inputs/pacman_single01.txt")
# pacman_single_02 = SingleFoodSearchProblem("./sample_inputs/pacman_single02.txt")
# pacman_single_03 = SingleFoodSearchProblem("./sample_inputs/pacman_single03.txt")

# pacman_multi_01 = MultiFoodSearchProblem("./sample_inputs/pacman_multi01.txt")
# pacman_multi_02 = MultiFoodSearchProblem("./sample_inputs/pacman_multi02.txt")
# pacman_multi_03 = MultiFoodSearchProblem("./sample_inputs/pacman_multi03.txt")

# # Kiểm tra BFS
# # Single
# print(bfs(pacman_single_01))
# print(bfs(pacman_single_02))
# print(bfs(pacman_single_03))
# # Multi
# print(bfs(pacman_multi_01))
# print(bfs(pacman_multi_02))
# print(bfs(pacman_multi_03))

# # Kiểm tra DFS
# # Single
# print(dfs(pacman_single_01))
# print(dfs(pacman_single_02))
# print(dfs(pacman_single_03))
# # Multi
# print(dfs(pacman_multi_01))
# print(dfs(pacman_multi_02))
# print(dfs(pacman_multi_03))

# # Kiểm tra UCS
# # Single
# print(ucs(pacman_single_01))
# print(ucs(pacman_single_02))
# print(ucs(pacman_single_03))
# # Multi
# print(ucs(pacman_multi_01))
# print(ucs(pacman_multi_02))
# print(ucs(pacman_multi_03))

# # Kiểm tra animate BFS
# # Single
# pacman_single_01.animate(bfs(pacman_single_01))
# pacman_single_02.animate(bfs(pacman_single_02))
# pacman_single_03.animate(bfs(pacman_single_03))
# # Multi
# pacman_multi_01.animate(bfs(pacman_multi_01))
# pacman_multi_02.animate(bfs(pacman_multi_02))
# pacman_multi_03.animate(bfs(pacman_multi_03))

# # Kiểm tra animate DFS
# # Single
# pacman_single_01.animate(dfs(pacman_single_01))
# pacman_single_02.animate(dfs(pacman_single_02))
# pacman_single_03.animate(dfs(pacman_single_03))
# # Multi
# pacman_multi_01.animate(dfs(pacman_multi_01))
# pacman_multi_02.animate(dfs(pacman_multi_02))
# pacman_multi_03.animate(dfs(pacman_multi_03))

# # Kiểm tra animate UCS
# # Single
# pacman_single_01.animate(ucs(pacman_single_01))
# pacman_single_02.animate(ucs(pacman_single_02))
# pacman_single_03.animate(ucs(pacman_single_03))
# # Multi
# pacman_multi_01.animate(ucs(pacman_multi_01))
# pacman_multi_02.animate(ucs(pacman_multi_02))
# pacman_multi_03.animate(ucs(pacman_multi_03))

# # Check hàm manhattanHeuristic
# # Single
# print(manhattanHeuristic(pacman_single_01.getStartState(),pacman_single_01))
# print(manhattanHeuristic(pacman_single_01.getStartState(),pacman_single_01))
# print(manhattanHeuristic(pacman_single_01.getStartState(),pacman_single_01))
# # Multi
# print(manhattanHeuristic(pacman_multi_01.getStartState(),pacman_multi_01))
# print(manhattanHeuristic(pacman_multi_02.getStartState(),pacman_multi_02))
# print(manhattanHeuristic(pacman_multi_03.getStartState(),pacman_multi_03))

# # Check hàm euclideanHeuristic
# # Single
# print(euclideanHeuristic(pacman_single_01.getStartState(),pacman_single_01))
# print(euclideanHeuristic(pacman_single_01.getStartState(),pacman_single_01))
# print(euclideanHeuristic(pacman_single_01.getStartState(),pacman_single_01))
# # Multi
# print(euclideanHeuristic(pacman_multi_01.getStartState(),pacman_multi_01))
# print(euclideanHeuristic(pacman_multi_02.getStartState(),pacman_multi_02))
# print(euclideanHeuristic(pacman_multi_03.getStartState(),pacman_multi_03))

# # Check hàm foodHeristic
# # Single
# print(foodHeristic(pacman_single_01.getStartState(),pacman_single_01))
# print(foodHeristic(pacman_single_01.getStartState(),pacman_single_01))
# print(foodHeristic(pacman_single_01.getStartState(),pacman_single_01))
# # Multi
# print(foodHeristic(pacman_multi_01.getStartState(),pacman_multi_01))
# print(foodHeristic(pacman_multi_02.getStartState(),pacman_multi_02))
# print(foodHeristic(pacman_multi_03.getStartState(),pacman_multi_03))

# Check hàm Astar
# Single
# Với manhattanHeuristic
# print(astar(pacman_single_01,manhattanHeuristic))
# print(astar(pacman_single_02,manhattanHeuristic))
# print(astar(pacman_single_03,manhattanHeuristic))
# # Với euclideanHeuristic
# print(astar(pacman_single_01,euclideanHeuristic))
# print(astar(pacman_single_02,euclideanHeuristic))
# print(astar(pacman_single_03,euclideanHeuristic))
# # Multi
# # Với manhattanHeuristic
# print(astar(pacman_multi_01,manhattanHeuristic))
# print(astar(pacman_multi_02,manhattanHeuristic))
# print(astar(pacman_multi_03,manhattanHeuristic))
# Với euclideanHeuristic
# print(astar(pacman_multi_01,euclideanHeuristic))
# print(astar(pacman_multi_02,euclideanHeuristic))
# print(astar(pacman_multi_03,euclideanHeuristic))

# # Check hàm animate Astar
# # Single
# # Với manhattanHeuristic
# pacman_single_01.animate(astar(pacman_single_01,manhattanHeuristic))
# pacman_single_02.animate(astar(pacman_single_02,manhattanHeuristic))
# pacman_single_03.animate(astar(pacman_single_03,manhattanHeuristic))
# # Với euclideanHeuristic
# pacman_single_01.animate(astar(pacman_single_01,euclideanHeuristic))
# pacman_single_02.animate(astar(pacman_single_02,euclideanHeuristic))
# pacman_single_03.animate(astar(pacman_single_03,euclideanHeuristic))
# # Multi
# # Với manhattanHeuristic
# pacman_multi_01.animate(astar(pacman_multi_01,manhattanHeuristic))
# pacman_multi_02.animate(astar(pacman_multi_02,manhattanHeuristic))
# pacman_multi_03.animate(astar(pacman_multi_03,manhattanHeuristic))
# # Với euclideanHeuristic
# pacman_multi_01.animate(astar(pacman_multi_01,euclideanHeuristic))
# pacman_multi_02.animate(astar(pacman_multi_02,euclideanHeuristic))
# pacman_multi_03.animate(astar(pacman_multi_03,euclideanHeuristic))

# # Check hàm gbfs
# # Single
# # Với foodHeristic
# print(gbfs(pacman_single_01,foodHeristic))
# print(gbfs(pacman_single_02,foodHeristic))
# print(gbfs(pacman_single_03,foodHeristic))
# # Multi
# # Với foodHeristic
# print(gbfs(pacman_multi_01,foodHeristic))
# print(gbfs(pacman_multi_02,foodHeristic))
# print(gbfs(pacman_multi_03,foodHeristic))

# # Check hàm animate gbfs
# # Single
# # Với foodHeristic
# pacman_single_01.animate(gbfs(pacman_single_01,foodHeristic))
# pacman_single_02.animate(gbfs(pacman_single_02,foodHeristic))
# pacman_single_03.animate(gbfs(pacman_single_03,foodHeristic))
# # Multi
# # Với foodHeristic
# pacman_multi_01.animate(gbfs(pacman_multi_01,foodHeristic))
# pacman_multi_02.animate(gbfs(pacman_multi_02,foodHeristic))
# pacman_multi_03.animate(gbfs(pacman_multi_03,foodHeristic))