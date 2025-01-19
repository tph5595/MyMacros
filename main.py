# import pandas as pd
# import numpy as np


class Person:
    def __init__(self, weight, bodyfat, height, age, sex):
        self.weight = weight
        self.bodyfat = bodyfat
        self.height = height
        if age < 18:
            raise Exception("Sorry, only ages 18+")
        self.age = age
        if sex not in ["M","F"]:
            raise Exception("Sorry, only male and female are accepted as sex")
        self.sex = sex

    def fatFreeMass(self):
        return self.weight * (1-self.bodyfat)
    def fatMass(self):
        return self.weight * (self.bodyfat)

# https://macrofactorapp.com/macrofactors-bmr/
class BMR:
    # Metabolic adaptation adjustment
    @staticmethod
    def adjust_energy_deficit(bmr):
        return bmr * 0.95

    # Metabolic adaptation adjustment
    @staticmethod
    def adjust_low_than_peak(bmr, p: Person, peak_weight):
        if p.weight/(peak_weight*1.0) < 0.9:
            return bmr * .93
        return bmr

    @staticmethod
    def hwas_improved(p: Person):
        if p.age < 60:
            age_factor = 1.96
        else:
            age_factor = 4.9

        if p.sex == "M":
            sex_factor = 0
        else: 
            sex_factor = 1

        return 129.6 * p.weight**0.55 \
               + 0.011 * p.height**2 \
               - age_factor * p.age \
               - 213.8 * sex_factor

    @staticmethod
    def ffm_improved(p: Person):
        if p.age < 60:
            age_factor = 1.1
        else:
            age_factor = 2.75

        return 50.2 * p.fatFreeMass()**0.7 \
               + 40.5 * (p.fatFreeMass()**0.7 * p.fatMass()**0.066) \
               - age_factor * p.age

    # Althete is spending at least 7 hr/wk of intense exercise
    @staticmethod
    def athlete_improved(p: Person):
        return 40.4 * p.fatFreeMass()**0.932

    @staticmethod
    def cunningham_1991(p: Person):
        return 21.6 * p.fatFreeMass() + 370

    @staticmethod
    def oxford_henry(p: Person):
        if p.sex == "M":
            if p.age < 30:
                return 14.4 * p.weight + 3.13 * p.height + 113
            elif p.age < 60:
                return 11.4 * p.weight + 5.41 * p.height - 137
            else:
                return 11.4 * p.weight + 5.41 * p.height - 256
        if p.sex == "F":
            if p.age < 30:
                return 10.4 * p.weight + 6.15 * p.height - 282
            elif p.age < 60:
                return 8.18 * p.weight + 5.02 * p.height - 11,6
            else:
                return 8.52 * p.weight + 4.21 * p.height + 10.7

        raise Exception("Sorry, only male and female are accepted as sex")
        
        
def pounds2kg(pounds):
    return pounds * 0.453592

def kg2pounds(kg):
    return kg / 0.453592

def inch2cm(inch):
    return inch * 2.54

def cm2inch(cm):
    return cm / 2.54

def main():
    return 0

if __name__ == "__main__":
    main()
