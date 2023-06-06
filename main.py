import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from person import Person
import packages
import events
import rand
import functions

matplotlib.rcParams.update({'font.size': 6})

fig, axs = plt.subplots(3)
years = 0
allMoney = 0
amount = 100000
customers = functions.createPeople(amount)

def simulation(n):
    global years, allMoney

    # 1 iteracja symulacji to pol roku
    years+=0.5

    for i in range(amount):
        # Jezeli klient nie zyje przjdz do nastepnego
        if(customers[i].alive == False): continue

        # Platnosc skladek za pol roku
        allMoney += (6 * packages.priceOfpackages[customers[i].package-1])

        # Postarzanie
        newAge = customers[i].age+0.5
        customers[i].setAge(newAge)
        newAgeLevel = Person.checkAge(customers[i].age)

        # Sprawdzenie rangi wieku po postarzeniu, przydzielenie nowej rangi i pakietu
        if(customers[i].ageLevel != newAgeLevel):
            customers[i].setAgeLevel(newAgeLevel)
            customers[i].setPackage()

        # (20%) prawdopodobieństwo na zajscie zdarzenia 
        isHappend = rand.isProbability(18)

        # Sprawdzenie czy zdarzenie zaszlo
        if(isHappend):
            eventNumber = rand.getRandomNumber(0, 5)
            eventProbabilty = rand.getRandomNumber(1, 100)

            # ustawione (40%) prawdopodobieństwo na wypłacenie odszkodowania
            if(rand.isProbability(40) == False): continue

            if(customers[i].ageLevel == 0):
                event = list(events.probabilityYoungPerson)[eventNumber]

                # Jezeli zdarzenie zaszlo dla mlodego
                if(eventProbabilty <= events.probabilityYoungPerson[event]):

                    events.amountYoungPerson[event]+=1
                    events.youngPackages[customers[i].package-1][event]+=1

                    if(eventNumber > 2): customers[i].setAlive(False)

                    allMoney -= events.priceOfEvents[customers[i].package-1][event]
                
            
            if(customers[i].ageLevel == 1):
                event = list(events.probabilityMediumPerson)[eventNumber]
                
                # Jezeli zdarzenie zaszlo dla sredniego
                if(eventProbabilty <= events.probabilityMediumPerson[event]):

                    events.amountMediumPerson[event]+=1
                    events.mediumPackages[customers[i].package-1][event]+=1

                    if(eventNumber > 2): customers[i].setAlive(False)

                    allMoney -= events.priceOfEvents[customers[i].package-1][event]
            

            if(customers[i].ageLevel == 2):
                eventNumber = rand.getRandomNumber(0, 2)
                event = list(events.probabilityOldPerson)[eventNumber]

                # Jezeli zdarzenie zaszlo dla starego
                if(eventProbabilty <= events.probabilityOldPerson[event]):

                    events.amountOldPerson[event]+=1
                    events.oldPackages[customers[i].package-1][event]+=1

                    if(eventNumber > 0): customers[i].setAlive(False)

                    allMoney -= events.priceOfEvents[customers[i].package-1][event]
    
    s="Lata: " + str(years) + " Zysk: " + str(allMoney) + "zł"
    fig.suptitle(s)

    functions.showChart(events.amountYoungPerson, "Młode osoby", 0, axs)    
    functions.showChart(events.amountMediumPerson, "Średnie osoby", 1, axs) 
    functions.showChart(events.amountOldPerson, "Stare osoby", 2, axs) 

    if(years%5==0):
        print("Lata:", years)
        print("Zysk:", allMoney)

        print("Młoda osoba:", events.amountYoungPerson)
        print()

        print("Średnia osoba:", events.amountMediumPerson)
        print()

        print("Stara osoba:", events.amountOldPerson)
        print()


ani = animation.FuncAnimation(fig, simulation, interval=100)
#ani.save("TLI.gif", writer='imagemagick',fps=60)
plt.show()
