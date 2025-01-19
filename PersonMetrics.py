from enum import Enum

class ActivityLevel(Enum):
    LOW = 1
    MODERATE = 2
    HIGH = 3

class PersonMetrics:
    def __init__(self, 
                 weight, 
                 bodyfat, 
                 height, 
                 age, 
                 sex, 
                 generalActivityLevel: ActivityLevel, 
                 trainingSessions,
                 peakWeight):
        self.weight = weight
        self.peakWeight = peakWeight
        self.bodyfat = bodyfat
        self.height = height
        if age < 18:
            raise Exception("Sorry, only ages 18+")
        self.age = age
        if sex not in ["M","F"]:
            raise Exception("Sorry, only male and female are accepted as sex")
        self.sex = sex
        self.generalActivityLevel = generalActivityLevel
        self.trainingSessions = trainingSessions

    def fatFreeMass(self):
        return self.weight * (1-self.bodyfat)
    def fatMass(self):
        return self.weight * (self.bodyfat)


