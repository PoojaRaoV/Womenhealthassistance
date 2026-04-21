from datetime import datetime, timedelta

class HealthTracker:

    def calculate_bmi(self, weight, height):
        height_m = height / 100
        return round(weight / (height_m ** 2), 2)

    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def next_period_date(self, last_period, cycle_days=28):
        # FIXED FORMAT HERE ✅
        last_date = datetime.strptime(last_period, "%m/%d/%Y")
        next_date = last_date + timedelta(days=cycle_days)
        return next_date.strftime("%m/%d/%Y")