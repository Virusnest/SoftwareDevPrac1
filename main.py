from operator import attrgetter
plans = []
totals = []

# Plan class to hold the plan details
class Plan:
    Name=""
    UpfrountCost=0
    MonthlyCost=0

# Enum for the result type
class ResultType:
    NONE=0
    BEST=1
    WORST=2

# Result class to hold the result of the calculation
class Result:
    Name=""
    TotalCost=0
    Status=ResultType.BEST

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

def calculate(t):
    # calculate the total cost for each plan
    for i in range(t):
        period =[]
        _totals = []
        for plan in plans:
            total = plan.UpfrountCost + plan.MonthlyCost * i
            _totals.append(total)
        best = min(_totals)
        worst = max(_totals)
        for i in range(len(plans)):
            if _totals[i] == best:
                result = Result()
                result.Name = plans[i].Name
                result.TotalCost = _totals[i]
                result.Status = ResultType.BEST
                period.append(result)
            elif _totals[i] == worst:
                result = Result()
                result.Name = plans[i].Name
                result.TotalCost = _totals[i]
                result.Status = ResultType.WORST
                period.append(result)
            else:
                result = Result()
                result.Name = plans[i].Name
                result.TotalCost = _totals[i]
                result.Status = ResultType.NONE
                period.append(result)
        totals.append(period)


def printTotals():
    # get the min and max total costs from the last period in the totals list
    best = [pln for pln in totals[len(totals)-1] if pln.Status == ResultType.BEST]
    worst = [pln for pln in totals[len(totals)-1] if pln.Status == ResultType.WORST]

    print("Name | Total")
    for pln in totals[len(totals)-1]:
        if pln.Status == ResultType.BEST:
            print(pln.Name, "$"+str(pln.TotalCost), "Best")
        elif pln.Status == ResultType.WORST:
            print(pln.Name, "$"+str(pln.TotalCost), "Worst")
        else:
            print(pln.Name, "$"+str(pln.TotalCost))

def printSummery():
    # loop through all periods and find out when each plan becomes the best
    oldstatus = []
    beststatus = []
    for i in range(len(totals)):
        for j in range(len(totals[i])):
            if i == 0:
                oldstatus = totals[i]
                break
            if totals[i][j].Status == 1 and (oldstatus[j].Status != 1):
                 beststatus.append((totals[i][j].Name,i))
            oldstatus = totals[i]

    if len(beststatus) == 0:
        best = [pln for pln in totals[len(totals) - 1] if pln.Status == ResultType.BEST]
        for pln in best:
                print(pln.Name+" stays the best plan over the period")
        return
    # print the results as a summery "X becomes the best after y months"
    for i in range(len(beststatus)):
        print(beststatus[i][0], "becomes the best after", beststatus[i][1], "months")

loadFile("plans.txt")
printList()

print("Enter time period in months")
time = int(input())

calculate(time)
printTotals()
# ask to print summery
print("Do you want to print the summery? (Y/n)")
if input().lower() != "n":
    printSummery()