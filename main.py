list = []
time=0
class Plan:
    Name=""
    UpfrountCost=0
    MonthlyCost=0

def loadfile(filename):
    with open(filename) as file:
        for line in file:
            # split the line into a list of strings
            if line[0] == "#":
                continue
            parts = line.split(" ")
            # create a new plan object
            plan = Plan()
            # assign the values from the list to the object
            plan.Name = parts[0]
            plan.UpfrountCost = int(parts[1])
            plan.MonthlyCost = int(parts[2])
            # add the plan object to the list
            list.append(plan)

def printlist():
    for plan in list:
        print(plan.Name, plan.UpfrountCost, plan.MonthlyCost)


def calculate():
    totals = []
    for plan in list:
        total = plan.UpfrountCost + (plan.MonthlyCost * time)
        totals.append(total)
    # find largest and smallest totoal then print all plans hilighting the best and worst
    best = min(totals)
    worst = max(totals)
    for i in range(len(list)):
        if totals[i] == best:
            print("Best Plan: ", end='')
        elif totals[i] == worst:
            print("Worst Plan: ",end='')
        print(list[i].Name,"$"+ str(totals[i]))

loadfile("plans.txt")
printlist()

print("Enter time period in months")
time = int(input())

calculate()