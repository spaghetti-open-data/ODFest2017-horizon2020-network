# testing the bargaining power proxy

def barPower(budget, totalBudget, N):
    '''
    (float, float, integer) => float
    computes bargaining power within  a project
    '''
    bP = ( N * budget - totalBudget) / (N * totalBudget)

    return bP

projects = []

project1 = [10, 10, 10, 10, 1000]
project2 = [50, 50, 50]
project3 = [70, 40, 57, 3, 190]

projects.append(project1)
projects.append(project2)
projects.append(project3)

for project in projects:
    bigN =len(project)
    tot = sum(budget for budget in project)
    barPowers = []
    for item in project:
        barP = ( bigN * item - tot) / (bigN * tot)
        barPowers.append(barP)
    print (str(project) + ': ' + str(barPowers) +' checksum: ' + str(sum (item for item in barPowers)))
