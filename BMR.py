from PersonMetrics import PersonMetrics
from Goal import Goal

# https://macrofactorapp.com/macrofactors-bmr/
class BMR:
    @staticmethod
    def adjust_energy_deficit(bmr, goal: Goal):
        if goal.rate < 0:
            return bmr * 0.95
        return bmr

    @staticmethod
    def adjust_low_than_peak(bmr, p: PersonMetrics):
        if p.weight/(p.peak_weight*1.0) < 0.9:
            return bmr * .93
        return bmr

    # Metabolic adaptation adjustment
    @staticmethod
    def metabolic_adjustment(bmr, p: PersonMetrics):
        return BMR.adjust_energy_deficit(bmr, p) * BMR.adjust_low_than_peak(bmr, p)

    @staticmethod
    def hwas_improved(p: PersonMetrics):
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
    def ffm_improved(p: PersonMetrics):
        if p.age < 60:
            age_factor = 1.1
        else:
            age_factor = 2.75

        return 50.2 * p.fatFreeMass()**0.7 \
               + 40.5 * (p.fatFreeMass()**0.7 * p.fatMass()**0.066) \
               - age_factor * p.age

    # Althete is spending at least 7 hr/wk of intense exercise
    @staticmethod
    def athlete_improved(p: PersonMetrics):
        return 40.4 * p.fatFreeMass()**0.932

    @staticmethod
    def cunningham_1991(p: PersonMetrics):
        return 21.6 * p.fatFreeMass() + 370

    @staticmethod
    def oxford_henry(p: PersonMetrics):
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
