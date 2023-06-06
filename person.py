import rand

class Person:
    def __init__(self, id, age, alive):
        self.id = id
        self.age = age
        self.alive = alive
        self.ageLevel = Person.checkAge(age)
        self.package = Person.setPackage(self)

    # Sprawdzenie rangi wieku do 0 do 2
    def checkAge(age):
        if(age<=35): return 0
        elif(age>35 and age<=65): return 1
        else: return 2
    
    # Przydzielanie pakietu według rangi wieku od 1 do 3
    def setPackage(self):
        num = rand.getRandomNumber(0,100)

        if(self.ageLevel==0):
            if(num<70): return 1
            elif(num>=70 and num<95): return 2
            return 3

        elif(self.ageLevel==1):
            if(num<50): return 1
            elif(num>=50 and num<80): return 2
            return 3

        else:
            if(num<30): return 1
            elif(num>=30 and num<70): return 2
            return 3
        
    def setAge(self, age):
        self.age = age

    def setAgeLevel(self, ageLevel):
        self.ageLevel = ageLevel

    def setAlive(self, alive):
        self.alive = alive
    
