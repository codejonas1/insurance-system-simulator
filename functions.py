from person import Person
import rand

def createPeople(amount):
    id=0
    allPeople = []

    while(id<amount):
        age = rand.getRandomNumber(18, 92)

        p = Person(id, age, True)
    
        allPeople.append(p)
    
        print("#id", allPeople[id].id, "Wiek:", allPeople[id].age,"| Poziom wieku:", allPeople[id].ageLevel,"| Żyje:", allPeople[id].alive, "| Pakiet:", allPeople[id].package)

        id+=1

    return allPeople

def showChart(dict, title, pos, axs):

    names = list(dict.keys())
    values = list(dict.values())

    axs[pos].clear()
    axs[pos].barh(names, values)
    axs[pos].set_title(title)
