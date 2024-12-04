from operator import attrgetter
# Runtime Data
plans = []
results = []
totals = []

# Plan class to hold the plan details
class Plan:
    Name=""
    UpfrountCost=0
    MonthlyCost=0

# Result class to hold the result of the calculation
class Result:
    Name=""
    IntersectionX=0

def loadFile(filename):
    with open(filename) as file:
        for line in file:
            # ignore comments
            if line[0] == "#":
                continue
            # split the line into a list of strings
            parts = line.split(" ")

            # create a new plan object
            plan = Plan()
            plan.Name = parts[0]
            plan.UpfrountCost = int(parts[1])
            plan.MonthlyCost = int(parts[2])

            # add the plan object to the list
            plans.append(plan)

def printList():
    print("Name | Upfront | Monthly")
    for plan in plans:
        print(plan.Name,"$"+str(plan.UpfrountCost), "$"+str(plan.MonthlyCost))

def intersection(p1, p2):
    # calculate the intersection of two lines
    x = (p2.UpfrountCost - p1.UpfrountCost) / (p1.MonthlyCost - p2.MonthlyCost)
    y = p1.MonthlyCost * x + p1.UpfrountCost
    # return none if no intersection is found
    if x < 0 or y < 0:
        return None
    return x, p2

def calculateTotals(t):
    # calculate the total cost of each plan over the time period
    for plan in plans:
        total = plan.UpfrountCost + (plan.MonthlyCost * t)
        totals.append(total)

def findClosestIntersection(p1, list):
    # find the closest intersection in a list of plans
    closest = None
    for plan in list:
        inter = intersection(p1, plan)
        if closest is None:
            closest = inter
        if inter is None:
            break
        if inter[0] < closest[0]:
            closest = inter
    return closest

def calculateSummery(t):
    # sort the plans by upfront cost
    plans.sort(key=attrgetter('UpfrountCost'))
    # ad the best initial cost first
    currentBest = plans.pop(0)
    result = Result()
    result.Name = currentBest.Name
    result.IntersectionX = 0
    results.append(result)
    finish = False
    # loop through intersection path
    while (len(plans)!=0):
        # Find the closest intersection
        closest = findClosestIntersection(currentBest, plans)
        if closest is None:
            finish = True
            break
        # if an intersection is found add the plan to the results
        if len(plans)!=0:
            currentBest = plans.pop(plans.index(closest[1]))
            result = Result()
            result.Name = closest[1].Name
            result.IntersectionX = closest[0]
            results.append(result)

    results.sort(key=attrgetter('IntersectionX'))

def printtotals():
    best = min(totals)
    worst = max(totals)
    # print the best and worst plans
    print("Name | Total")
    for i in range(len(plans)):
        if totals[i] == best:
            print("Best Plan: ", end='')
        elif totals[i] == worst:
            print("Worst Plan: ",end='')
        print(plans[i].Name,"$"+ str(totals[i]))

def printSummery():
    for i in range(len(results)):
        # print how long the plan is the best for and the point it becomes the best\
        age = 0
        if i == len(results)-1:
            age = time - results[i].IntersectionX
        else:
            age = results[i+1].IntersectionX - results[i].IntersectionX

        print(results[i].Name, "is the best plan for", age, "months")
        print(results[i].Name, "becomes the best plan at", results[i].IntersectionX, "months")

def printTotals():
    # Print the total cost of all the plans over the time period
    total = 0
    for result in results:
        total += result.UpfrountCost
    print("Total upfront cost: $"+str(total))

### MAIN PROGRAM ###
loadFile("plans.txt")
printList()

### MAIN UI AND INTERFACE ###
print("Would You like a summery of the plans or the total cost of the plans? (S/T)")

if input().lower() == "t":
    print("Enter time period in months")
    time = int(input())
    calculateTotals(time)
    printtotals()
else:
    print("Enter time period in months")
    time = int(input())
    calculateSummery(time)
    printSummery()