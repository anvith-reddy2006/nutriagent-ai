# calculator.py
# This file calculates BMR, TDEE, and macros
# AI Technique: Rule-based reasoning

def calculate_bmr(weight_kg, height_cm, age, sex):
    """
    BMR = How many calories your body needs just to stay alive (at rest)
    We use the Harris-Benedict formula for this
    """
    if sex == "Male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    return round(bmr)


def calculate_tdee(bmr, activity_level):
    """
    TDEE = BMR multiplied by how active you are
    More active = more calories needed
    """
    activity_factors = {
        "Sedentary (little or no exercise)":   1.2,
        "Lightly Active (1-3 days/week)":      1.375,
        "Moderately Active (3-5 days/week)":   1.55,
        "Very Active (6-7 days/week)":         1.725,
        "Athlete (twice a day training)":      1.9,
    }
    factor = activity_factors.get(activity_level, 1.2)
    return round(bmr * factor)


def calculate_calorie_goal(tdee, goal):
    """
    Adjust calories based on the user's goal:
    - Lose weight = eat 500 less than TDEE
    - Gain muscle = eat 300 more than TDEE
    - Maintain = eat exactly TDEE
    """
    if goal == "Lose Weight":
        return max(1200, tdee - 500)
    elif goal == "Gain Muscle":
        return tdee + 300
    else:
        return tdee


def calculate_macros(calorie_goal, goal):
    """
    Split total calories into protein, carbs, and fat
    1g protein = 4 kcal
    1g carbs   = 4 kcal
    1g fat     = 9 kcal
    """
    if goal == "Lose Weight":
        protein_pct, carb_pct, fat_pct = 0.35, 0.40, 0.25
    elif goal == "Gain Muscle":
        protein_pct, carb_pct, fat_pct = 0.35, 0.45, 0.20
    else:
        protein_pct, carb_pct, fat_pct = 0.25, 0.50, 0.25

    protein_g = round((calorie_goal * protein_pct) / 4)
    carbs_g   = round((calorie_goal * carb_pct)    / 4)
    fat_g     = round((calorie_goal * fat_pct)     / 9)

    return {
        "protein_g": protein_g,
        "carbs_g":   carbs_g,
        "fat_g":     fat_g,
        "calories":  calorie_goal
    }


def get_bmi(weight_kg, height_cm):
    """
    BMI = weight divided by height squared
    Tells us if the person is underweight, normal, overweight or obese
    """
    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m ** 2), 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category