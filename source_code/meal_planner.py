# meal_planner.py
# AI Technique: Greedy Search Algorithm with serving multiplier
# Selects best food AND calculates exact servings to hit macro targets

import pandas as pd
import os


def load_food_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "dataset", "food_data.csv")
    df = pd.read_csv(csv_path)
    return df


def filter_foods(df, diet_type, conditions):
    if diet_type == "Vegan":
        df = df[df["diet_type"] == "vegan"]
    elif diet_type == "Vegetarian":
        df = df[df["diet_type"].isin(["vegan", "vegetarian"])]
    if "Diabetes" in conditions:
        df = df[df["sugar_g"] <= 10]
    if "High Blood Pressure" in conditions:
        df = df[df["sodium_mg"] < 400]
    if "High Cholesterol" in conditions:
        df = df[df["fat_g"] < 12]
    return df.reset_index(drop=True)


def greedy_meal_search(foods_df, meal_category, target_calories,
                       target_protein, target_carbs, target_fat):
    """
    Greedy Search — picks best food then calculates
    exact number of servings to hit the calorie target.
    This makes daily totals match macro targets exactly.
    """
    meal_foods = foods_df[foods_df["category"] == meal_category].copy()

    if meal_foods.empty:
        return None

    # Score each food on all four targets
    meal_foods["cal_score"]  = abs(meal_foods["calories"]   - target_calories) / max(target_calories, 1)
    meal_foods["pro_score"]  = abs(meal_foods["protein_g"]  - target_protein)  / max(target_protein,  1)
    meal_foods["carb_score"] = abs(meal_foods["carbs_g"]    - target_carbs)    / max(target_carbs,    1)
    meal_foods["fat_score"]  = abs(meal_foods["fat_g"]      - target_fat)      / max(target_fat,      1)

    meal_foods["total_score"] = (
        meal_foods["cal_score"]  * 0.4 +
        meal_foods["pro_score"]  * 0.3 +
        meal_foods["carb_score"] * 0.2 +
        meal_foods["fat_score"]  * 0.1
    )

    meal_foods = meal_foods.sort_values("total_score")
    top_choices = meal_foods.head(5)
    chosen = top_choices.sample(1).iloc[0]

    # Calculate serving multiplier to hit calorie target exactly
    base_calories = float(chosen["calories"])
    if base_calories > 0:
        multiplier = round(target_calories / base_calories, 1)
        # Keep multiplier between 0.5 and 3.0 for realism
        multiplier = max(0.5, min(3.0, multiplier))
    else:
        multiplier = 1.0

    # Scale all nutrition by the multiplier
    actual_calories = round(base_calories        * multiplier)
    actual_protein  = round(float(chosen["protein_g"]) * multiplier, 1)
    actual_carbs    = round(float(chosen["carbs_g"])   * multiplier, 1)
    actual_fat      = round(float(chosen["fat_g"])     * multiplier, 1)

    # Format serving size with multiplier
    base_serving = str(chosen["serving_size"])
    if multiplier == 1.0:
        serving_display = base_serving
    elif multiplier == 0.5:
        serving_display = f"Half serving of {base_serving}"
    elif multiplier.is_integer():
        serving_display = f"{int(multiplier)}x {base_serving}"
    else:
        serving_display = f"{multiplier}x {base_serving}"# Format serving size naturally in human readable way
    import re
    base_serving = str(chosen["serving_size"])
    food_name    = str(chosen["food_name"]).lower()

    # Extract grams from bracket e.g. (200g)
    gram_match = re.search(r'\((\d+)g\)', base_serving)
    ml_match   = re.search(r'\((\d+)ml\)', base_serving)

    if "egg" in food_name or "egg" in base_serving.lower():
        eggs = max(1, round(2 * multiplier))
        unit = "egg" if eggs == 1 else "eggs"
        serving_display = f"{eggs} boiled {unit}"

    elif "scoop" in base_serving.lower():
        # Protein shake — show in ml
        actual_ml = round(300 * multiplier)
        scoops    = round(multiplier, 1)
        if scoops == int(scoops):
            scoops = int(scoops)
        serving_display = f"{scoops} scoop in {actual_ml}ml water"

    elif "idli" in food_name or "idli" in base_serving.lower():
        idlis = max(1, round(3 * multiplier))
        serving_display = f"{idlis} idlis with sambar"

    elif "dosa" in food_name or "dosa" in base_serving.lower():
        dosas = max(1, round(2 * multiplier))
        serving_display = f"{dosas} dosas with chutney"

    elif "slice" in base_serving.lower():
        slices = max(1, round(2 * multiplier))
        unit   = "slice" if slices == 1 else "slices"
        serving_display = f"{slices} {unit}"

    elif "piece" in base_serving.lower():
        pieces = max(1, round(multiplier))
        unit   = "piece" if pieces == 1 else "pieces"
        serving_display = f"{pieces} {unit}"

    elif "glass" in base_serving.lower():
        actual_ml = round(250 * multiplier)
        serving_display = f"{actual_ml}ml"

    elif "cup" in base_serving.lower():
        cups = round(multiplier, 1)
        if cups == int(cups):
            cups = int(cups)
        unit = "cup" if cups == 1 else "cups"
        serving_display = f"{cups} {unit}"

    elif ml_match:
        actual_ml = round(int(ml_match.group(1)) * multiplier)
        serving_display = f"{actual_ml}ml"

    elif gram_match:
        actual_grams = round(int(gram_match.group(1)) * multiplier)
        serving_display = f"{actual_grams}g"

    elif "banana" in food_name or "apple" in food_name \
      or "orange" in food_name or "mango" in food_name:
        count = max(1, round(multiplier))
        serving_display = f"{count} piece"

    elif "almond" in food_name:
        almonds = max(5, round(20 * multiplier))
        serving_display = f"{almonds} almonds"

    elif "plate" in base_serving.lower() or \
         "bowl"  in base_serving.lower():
        # Extract grams if available
        if gram_match:
            actual_grams = round(int(gram_match.group(1)) * multiplier)
            serving_display = f"{actual_grams}g"
        else:
            actual_grams = round(150 * multiplier)
            serving_display = f"{actual_grams}g"

    else:
        # Default fallback — estimate 100g base
        actual_grams = round(100 * multiplier)
        serving_display = f"{actual_grams}g"

    # Extract number and unit from serving size smartly
    # e.g. "2 whole eggs" with multiplier 2.5 = "5 whole eggs"
    # e.g. "1 cup cooked (195g)" with 1.5 = "1.5 cups cooked (293g)"

    if multiplier == 1.0:
        serving_display = base_serving

    elif "egg" in food_name or "egg" in base_serving.lower():
        # Eggs — show as number of eggs
        eggs = round(2 * multiplier)
        serving_display = f"{eggs} whole eggs"

    elif "cup" in base_serving.lower():
        # Cups — multiply the cup amount
        cups = round(multiplier, 1)
        if cups == int(cups):
            cups = int(cups)
        serving_display = base_serving.replace("1 cup", f"{cups} cups")

    elif "slice" in base_serving.lower():
        # Slices — multiply slices
        slices = round(2 * multiplier)
        serving_display = f"{slices} slices"

    elif "piece" in base_serving.lower():
        # Pieces
        pieces = round(multiplier)
        serving_display = f"{pieces} pieces"

    elif "glass" in base_serving.lower():
        # Glass
        glasses = round(multiplier, 1)
        if glasses == int(glasses):
            glasses = int(glasses)
        serving_display = f"{glasses} glass(es) (250ml each)"

    elif "plate" in base_serving.lower():
        # Plate
        if multiplier <= 0.5:
            serving_display = "Half plate"
        elif multiplier == 1.0:
            serving_display = base_serving
        else:
            serving_display = f"{round(multiplier, 1)} plates"

    elif "bowl" in base_serving.lower():
        # Bowl
        if multiplier <= 0.5:
            serving_display = "Half bowl"
        else:
            bowls = round(multiplier, 1)
            if bowls == int(bowls):
                bowls = int(bowls)
            serving_display = f"{bowls} bowl(s)"

    elif "g)" in base_serving.lower() or "g " in base_serving.lower():
        # Weight based — calculate grams
        import re
        nums = re.findall(r'\d+', base_serving)
        if nums:
            base_grams = int(nums[-1])
            actual_grams = round(base_grams * multiplier)
            serving_display = f"{actual_grams}g"
        else:
            serving_display = base_serving

    elif multiplier <= 0.5:
        serving_display = f"Half of {base_serving}"

    else:
        amt = round(multiplier, 1)
        if amt == int(amt):
            amt = int(amt)
        serving_display = f"{amt}x {base_serving}"

    return {
        "food":         chosen["food_name"],
        "calories":     actual_calories,
        "protein":      actual_protein,
        "carbs":        actual_carbs,
        "fat":          actual_fat,
        "category":     meal_category,
        "serving_size": serving_display,
        "multiplier":   multiplier
    }


def generate_daily_plan(df, daily_calories, daily_macros):
    """
    Generate one full day meal plan.
    Splits calories AND macros across 4 meals proportionally.
    """
    splits = {
        "breakfast": 0.25,
        "lunch":     0.35,
        "dinner":    0.30,
        "snack":     0.10,
    }

    plan           = {}
    total_calories = 0
    total_protein  = 0
    total_carbs    = 0
    total_fat      = 0

    for meal, pct in splits.items():
        target_cal  = round(daily_calories             * pct)
        target_pro  = round(daily_macros["protein_g"]  * pct)
        target_carb = round(daily_macros["carbs_g"]    * pct)
        target_fat  = round(daily_macros["fat_g"]      * pct)

        item = greedy_meal_search(
            df, meal,
            target_cal, target_pro, target_carb, target_fat
        )

        if item:
            plan[meal]      = item
            total_calories += item["calories"]
            total_protein  += item["protein"]
            total_carbs    += item["carbs"]
            total_fat      += item["fat"]

    plan["totals"] = {
        "calories": round(total_calories),
        "protein":  round(total_protein,  1),
        "carbs":    round(total_carbs,    1),
        "fat":      round(total_fat,      1),
    }
    return plan


def generate_weekly_plan(df, daily_calories, daily_macros):
    """Generate a 7-day meal plan passing macro targets each day."""
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    weekly = {}
    for day in days:
        weekly[day] = generate_daily_plan(df, daily_calories, daily_macros)
    return weekly


def get_dietary_warnings(conditions, diet_type):
    warnings = []
    if "Diabetes" in conditions:
        warnings.append(
            "Diabetic diet applied: high sugar foods removed. "
            "Monitor carbohydrate intake carefully.")
    if "High Blood Pressure" in conditions:
        warnings.append(
            "Low sodium diet applied: foods above 400mg sodium excluded.")
    if "High Cholesterol" in conditions:
        warnings.append(
            "Low fat diet applied: high fat foods excluded.")
    if diet_type == "Vegan":
        warnings.append(
            "Vegan diet: ensure adequate B12, iron and calcium "
            "from plant sources.")
    if diet_type == "Vegetarian":
        warnings.append(
            "Vegetarian diet: consider variety for iron and protein.")
    return warnings