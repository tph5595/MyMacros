# import pandas as pd
# import numpy as np
from PersonMetrics import PersonMetrics, ActivityLevel
from BMR import BMR

def activity_factor(p: PersonMetrics):
    if p.generalActivityLevel == ActivityLevel.LOW:
        correction_factor = 1.2
    elif p.generalActivityLevel == ActivityLevel.MODERATE:
        correction_factor = 1.4
    elif p.generalActivityLevel == ActivityLevel.HIGH:
        correction_factor = 1.6

    if p.trainingSessions == 0 :
        correction_factor += 0
    elif p.trainingSessions <= 3:
        correction_factor += 0.1
    elif p.trainingSessions <= 6:
        correction_factor += 0.2
    elif p.trainingSessions > 6:
        correction_factor += 0.3

    return correction_factor

def estimate_energy_expenditure(p: PersonMetrics):
    if p.isAthlete:
        bmr = BMR.athlete_improved(p)
    else:
        hwas_bmr = BMR.hwas_improved(p)
        ffm_bmr = BMR.ffm_improved(p)
        bmr = (hwas_bmr + ffm_bmr)/2.0

    bmr = bmr * BMR.metabolic_adjustment(bmr, p) 

    return bmr * activity_factor(p)

def main():
    return 0

if __name__ == "__main__":
    main()
