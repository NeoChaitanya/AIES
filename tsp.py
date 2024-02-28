import random

def randomSolution(tsp):
    cities =  list(range(len(tsp))) #0123 => [0, 1, 2, 3]
    solution =[]
    
    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) -1)]
        solution.append(randomCity)
        cities.remove(randomCity)
        
    return solution


def routeLength(tsp, solution):
    routeLength = 0
    
    for i in range(len(solution)):
        routeLength += tsp[solution[i-1]][solution[i]]
        
    return routeLength


def getNeighbours(solution):
    neighbours = [] #open list
    
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)  ####
            
    return neighbours


def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    
    for neighbour in neighbours:
        currnetRouteLength = routeLength(tsp, neighbour)
        if currnetRouteLength < bestRouteLength:
            bestRouteLength = currnetRouteLength
            bestNeighbour = neighbour
        
    return bestNeighbour, bestRouteLength


def hillClimbing(tsp):
    currnetSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currnetSolution)
    neighbours = getNeighbours(currnetSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)
    
    if bestNeighbourRouteLength < currentRouteLength:
        currnetSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currnetSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)
        
    return currnetSolution, currentRouteLength

def main():
    
    tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]
    
    print(hillClimbing(tsp))
     
if __name__ == "__main__":
    main()
        