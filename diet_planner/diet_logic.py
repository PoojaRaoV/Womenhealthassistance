import random

healthy_foods = {
    "breakfast": ["Oats", "Idli", "Upma", "Boiled Eggs", "Smoothie"],
    "lunch": ["Rice + Dal", "Chapati + Curry", "Veg pulao", "Quinoa salad"],
    "dinner": ["Soup", "Salad", "Grilled vegetables", "Khichdi"],
    "snacks": ["Fruits", "Nuts", "Yogurt", "Roasted chana"]
}

pcos_foods = {
    "breakfast": ["Oats with flaxseeds", "Egg whites", "Green smoothie"],
    "lunch": ["Millet roti + sabzi", "Brown rice + dal"],
    "dinner": ["Vegetable soup", "Paneer salad"],
    "snacks": ["Almonds", "Walnuts"]
}

iron_rich = ["Spinach", "Dates", "Beetroot", "Pomegranate"]

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def generate_day_plan(food_type, hb, bmi):
    plan = {
        "breakfast": random.choice(food_type["breakfast"]),
        "lunch": random.choice(food_type["lunch"]),
        "dinner": random.choice(food_type["dinner"]),
        "snacks": random.choice(food_type["snacks"])
    }

    if hb < 12:
        plan["extra"] = random.choice(iron_rich)

    if bmi > 25:
        plan["note"] = "Low calorie diet recommended"
    elif bmi < 18:
        plan["note"] = "High calorie diet recommended"

    return plan

def generate_weekly_plan(user):
    bmi = calculate_bmi(user["weight"], user["height"])
    food_type = pcos_foods if user["pcos"] == 1 else healthy_foods

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    return {
        day: generate_day_plan(food_type, user["hb"], bmi)
        for day in days
    }

def generate_monthly_plan(user):
    return {f"Week {i+1}": generate_weekly_plan(user) for i in range(4)}

def generate_yearly_plan(user):
    return {f"Month {i+1}": generate_monthly_plan(user) for i in range(12)}