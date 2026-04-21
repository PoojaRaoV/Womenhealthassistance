from user_profile import UserProfile
from health_tracker import HealthTracker
from report_analysis import ReportAnalysis

class HealthSystem:
    def __init__(self):
        self.user = UserProfile()
        self.tracker = HealthTracker()
        self.report = ReportAnalysis()

    def process_user_data(self, name, age, height, weight, condition):
        profile = self.user.create_profile(name, age, height, weight, condition)

        bmi = self.tracker.calculate_bmi(weight, height)
        category = self.tracker.bmi_category(bmi)

        return {
            "profile": profile,
            "bmi": bmi,
            "category": category
        }

    def get_period_prediction(self, last_period):
        return self.tracker.next_period_date(last_period)

    def analyze_reports(self, tsh, hb):
        return {
            "thyroid": self.report.analyze_thyroid(tsh),
            "hemoglobin": self.report.analyze_hemoglobin(hb)
        }