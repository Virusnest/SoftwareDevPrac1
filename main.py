from operator import attrgetter
list = []
totals = []

time=0
class Plan:
    Name=""
    UpfrountCost=0
    MonthlyCost=0

class ResultType:
    NONE=0
    BEST=1
    WORST=2

class Result:
    Name=""
    TotalCost=0
    Status=ResultType.BEST

def loadfile(filename):
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
            list.append(plan)

def printlist():
    print("Name | Upfront | Monthly")
    for plan in list:
        print(plan.Name,"$"+str(plan.UpfrountCost), "$"+str(plan.MonthlyCost))

def calculate(time):
    # calculate the total cost for each plan
    for i in range(time):
        period =[]
        totals = []
        for plan in list:
            total = plan.UpfrountCost + plan.MonthlyCost * time
            totals.append(total)
        best = min(totals)
        worst = max(totals)
        for i in range(len(list)):
            if totals[i] == best:
                period.append(Result(list[i].Name, totals[i], ResultType.BEST))
            elif totals[i] == worst:
                period.append(Result(list[i].Name, totals[i], ResultType.WORST))
            else:
                period.append(Result(list[i].Name, totals[i], ResultType.NONE))

        totals.append(period)

def printtotals():
    # get the min and max total costs from the last period in the totals list

def printsummery():
    best = (min(totals))
    worst = (max(totals),)
    print("Your best plan is: ", end='')


loadfile("plans.txt")
printlist()

print("Enter time period in months")
time = int(input())

calculate()
printtotals()