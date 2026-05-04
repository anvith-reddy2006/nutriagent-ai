# agent.py
# Main Dietician AI Agent
# Agent Type: Goal-based Agent
# Perceive → Reason → Act

from calculator import (calculate_bmr, calculate_tdee,
                        calculate_calorie_goal, calculate_macros, get_bmi)
from meal_planner import (load_food_data, filter_foods,
                          generate_weekly_plan, get_dietary_warnings)


class DieticianAgent:
    """
    Goal-Based AI Agent for personalised diet planning.
    Environment : User health profile
    Percepts    : Age, weight, height, goal, conditions
    Actions     : Meal plan, macros, warnings
    AI Logic    : Rule-based reasoning + Greedy Search
    """

    def __init__(self):
        self.food_db = load_food_data()

    def perceive(self, user_profile):
        """Step 1 — store user inputs."""
        self.profile = user_profile
        return self

    def reason(self):
        """Step 2 — calculate nutrition targets using rule-based AI."""
        p = self.profile
        self.bmr          = calculate_bmr(p["weight"], p["height"],
                                          p["age"], p["sex"])
        self.tdee         = calculate_tdee(self.bmr, p["activity_level"])
        self.calorie_goal = calculate_calorie_goal(self.tdee, p["goal"])
        self.macros       = calculate_macros(self.calorie_goal, p["goal"])
        self.bmi, self.bmi_category = get_bmi(p["weight"], p["height"])
        return self

    def act(self):
        """Step 3 — search food database and generate meal plan."""
        p = self.profile
        filtered_foods = filter_foods(
            self.food_db, p["diet_type"], p["conditions"]
        )
        # Pass macro targets so greedy search matches both
        # calories AND macros
        self.weekly_plan = generate_weekly_plan(
            filtered_foods,
            self.calorie_goal,
            self.macros
        )
        self.warnings = get_dietary_warnings(
            p["conditions"], p["diet_type"]
        )
        return self

    def run(self, user_profile):
        """Full agent loop: perceive → reason → act."""
        return self.perceive(user_profile).reason().act()

    def get_results(self):
        """Return all results as a dictionary for the UI."""
        return {
            "bmr":          self.bmr,
            "tdee":         self.tdee,
            "calorie_goal": self.calorie_goal,
            "macros":       self.macros,
            "bmi":          self.bmi,
            "bmi_category": self.bmi_category,
            "weekly_plan":  self.weekly_plan,
            "warnings":     self.warnings,
        }