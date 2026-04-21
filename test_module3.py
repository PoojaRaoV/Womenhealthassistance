from user_profile import UserProfile
from health_tracker import HealthTracker
from report_analysis import ReportAnalysis

# Create objects
user = UserProfile()
tracker = HealthTracker()
report = ReportAnalysis()

# Input data
profile = user.create_profile(
    name="Puneetha",
    age=21,
    height=160,
    weight=55,
    condition="PCOS"
)

# BMI
bmi = tracker.calculate_bmi(profile["weight"], profile["height"])
category = tracker.bmi_category(bmi)

# Period prediction
next_period = tracker.next_period_date("2026-04-01")

# Report analysis
thyroid = report.analyze_thyroid(5.2)
hb = report.analyze_hemoglobin(10)

# Output
print("\n--- USER PROFILE ---")
print(profile)

print("\n--- HEALTH STATUS ---")
print("BMI:", bmi)
print("Category:", category)

print("\n--- MENSTRUAL TRACKING ---")
print("Next Period:", next_period)

print("\n--- REPORT ANALYSIS ---")
print("Thyroid:", thyroid)
print("Hemoglobin:", hb)