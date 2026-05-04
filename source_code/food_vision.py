# food_vision.py
# Free Food Image Analyzer — 50+ foods including Indian foods
# No API key needed — rule-based knowledge base

def analyze_food_image_free(image_file):
    filename = image_file.name.lower()
    filename = filename.replace("_", " ").replace("-", " ")
    filename = filename.replace(".jpg","").replace(".jpeg","")
    filename = filename.replace(".png","").replace(".webp","").strip()

    food_knowledge = {

        # ── Rice & Grains ──────────────────────────────────────────────────
        "rice": {
            "food_name": "White Rice",
            "serving_size": "1 cup cooked (195g)",
            "calories_per_serving": 206,
            "protein_g": 4.3, "carbs_g": 44.5, "fat_g": 0.4,
            "health_rating": "Moderate",
            "recommended_daily_amount": "1-2 cups per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Quick energy source", "Easy to digest", "Gluten free"],
            "tips": "Prefer brown rice for more fiber and nutrients.",
            "warnings": ["High glycemic index — diabetics limit portions"]
        },
        "brown rice": {
            "food_name": "Brown Rice",
            "serving_size": "1 cup cooked (195g)",
            "calories_per_serving": 215,
            "protein_g": 5.0, "carbs_g": 45.0, "fat_g": 1.8,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 cups per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["High fiber", "Rich in magnesium", "Lowers cholesterol"],
            "tips": "Soak for 30 minutes before cooking to reduce cooking time.",
            "warnings": []
        },
        "oats": {
            "food_name": "Oatmeal",
            "serving_size": "1 cup cooked (240g)",
            "calories_per_serving": 150,
            "protein_g": 5.0, "carbs_g": 27.0, "fat_g": 3.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day at breakfast",
            "best_time_to_eat": "Breakfast",
            "benefits": ["Lowers cholesterol", "Keeps you full longer", "Stabilizes blood sugar"],
            "tips": "Add fruits and nuts instead of sugar.",
            "warnings": []
        },
        "bread": {
            "food_name": "Whole Wheat Bread",
            "serving_size": "2 slices (60g)",
            "calories_per_serving": 120,
            "protein_g": 4.0, "carbs_g": 22.0, "fat_g": 2.0,
            "health_rating": "Moderate",
            "recommended_daily_amount": "2-4 slices per day",
            "best_time_to_eat": "Breakfast or lunch",
            "benefits": ["Complex carbohydrates", "Contains fiber", "B vitamins"],
            "tips": "Choose whole wheat over white bread.",
            "warnings": ["Contains gluten"]
        },
        "roti": {
            "food_name": "Whole Wheat Roti",
            "serving_size": "2 rotis (60g)",
            "calories_per_serving": 150,
            "protein_g": 5.0, "carbs_g": 30.0, "fat_g": 2.5,
            "health_rating": "Healthy",
            "recommended_daily_amount": "2-4 rotis per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Good complex carbs", "High fiber", "Low fat"],
            "tips": "Use whole wheat atta for maximum nutrition.",
            "warnings": []
        },
        "chapati": {
            "food_name": "Chapati",
            "serving_size": "2 chapatis (60g)",
            "calories_per_serving": 150,
            "protein_g": 5.0, "carbs_g": 30.0, "fat_g": 2.5,
            "health_rating": "Healthy",
            "recommended_daily_amount": "2-4 per day with vegetables",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Good complex carbs", "High fiber", "Low fat"],
            "tips": "Pair with dal and vegetables for a complete meal.",
            "warnings": []
        },
        "idli": {
            "food_name": "Idli with Sambar",
            "serving_size": "3 idlis + 1 cup sambar",
            "calories_per_serving": 200,
            "protein_g": 7.0, "carbs_g": 38.0, "fat_g": 2.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "3-4 idlis per breakfast",
            "best_time_to_eat": "Breakfast",
            "benefits": ["Fermented — good for gut health", "Low fat", "Easy to digest"],
            "tips": "Eat with sambar and chutney for complete nutrition.",
            "warnings": []
        },
        "dosa": {
            "food_name": "Dosa with Chutney",
            "serving_size": "2 dosas (120g)",
            "calories_per_serving": 220,
            "protein_g": 5.0, "carbs_g": 38.0, "fat_g": 6.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "2 dosas per breakfast",
            "best_time_to_eat": "Breakfast",
            "benefits": ["Fermented food", "Good carb source", "Low in sugar"],
            "tips": "Choose plain dosa over masala dosa to reduce calories.",
            "warnings": []
        },
        "upma": {
            "food_name": "Upma",
            "serving_size": "1 plate (150g)",
            "calories_per_serving": 200,
            "protein_g": 5.0, "carbs_g": 35.0, "fat_g": 5.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 plate per breakfast",
            "best_time_to_eat": "Breakfast",
            "benefits": ["Good energy source", "Contains vegetables", "Low sugar"],
            "tips": "Add mixed vegetables to increase nutrition.",
            "warnings": []
        },
        "poha": {
            "food_name": "Poha",
            "serving_size": "1 plate (150g)",
            "calories_per_serving": 180,
            "protein_g": 4.0, "carbs_g": 35.0, "fat_g": 4.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 plate per breakfast",
            "best_time_to_eat": "Breakfast",
            "benefits": ["Light on stomach", "Good iron source", "Low fat"],
            "tips": "Add peanuts for extra protein.",
            "warnings": []
        },
        "quinoa": {
            "food_name": "Quinoa",
            "serving_size": "1 cup cooked (185g)",
            "calories_per_serving": 222,
            "protein_g": 8.0, "carbs_g": 39.0, "fat_g": 4.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Complete protein with all amino acids", "Gluten free", "High fiber"],
            "tips": "Rinse well before cooking to remove bitterness.",
            "warnings": []
        },

        # ── Proteins ───────────────────────────────────────────────────────
        "egg": {
            "food_name": "Boiled Eggs",
            "serving_size": "2 whole eggs (100g)",
            "calories_per_serving": 155,
            "protein_g": 13.0, "carbs_g": 1.1, "fat_g": 11.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 eggs per day",
            "best_time_to_eat": "Breakfast",
            "benefits": ["Complete protein", "Rich in B12 and Vitamin D", "Brain health"],
            "tips": "Boiled or poached is healthier than fried.",
            "warnings": []
        },
        "chicken": {
            "food_name": "Grilled Chicken Breast",
            "serving_size": "1 piece (100g)",
            "calories_per_serving": 165,
            "protein_g": 31.0, "carbs_g": 0.0, "fat_g": 3.6,
            "health_rating": "Healthy",
            "recommended_daily_amount": "100-150g per meal",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Excellent lean protein", "Supports muscle growth", "Low fat"],
            "tips": "Grill or bake instead of frying.",
            "warnings": []
        },
        "fish": {
            "food_name": "Grilled Fish",
            "serving_size": "1 fillet (100g)",
            "calories_per_serving": 200,
            "protein_g": 25.0, "carbs_g": 0.0, "fat_g": 10.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "100-150g, 2-3 times per week",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Rich in Omega-3 fatty acids", "High protein", "Heart healthy"],
            "tips": "Steam or grill for the healthiest preparation.",
            "warnings": []
        },
        "salmon": {
            "food_name": "Grilled Salmon",
            "serving_size": "1 fillet (100g)",
            "calories_per_serving": 208,
            "protein_g": 28.0, "carbs_g": 0.0, "fat_g": 10.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "100-150g, 2 times per week",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Highest Omega-3 source", "Anti-inflammatory", "Brain health"],
            "tips": "Do not overcook — keep slightly pink inside for best nutrition.",
            "warnings": []
        },
        "paneer": {
            "food_name": "Paneer",
            "serving_size": "100g",
            "calories_per_serving": 265,
            "protein_g": 18.0, "carbs_g": 3.0, "fat_g": 20.0,
            "health_rating": "Moderate",
            "recommended_daily_amount": "100g per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["High protein for vegetarians", "Rich in calcium", "Good fat source"],
            "tips": "Choose low fat paneer to reduce calories.",
            "warnings": ["High in saturated fat — limit if high cholesterol"]
        },
        "tofu": {
            "food_name": "Tofu",
            "serving_size": "1 cup (180g)",
            "calories_per_serving": 200,
            "protein_g": 15.0, "carbs_g": 12.0, "fat_g": 10.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "100-150g per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Excellent vegan protein", "Isoflavones for heart health", "Low calorie"],
            "tips": "Press tofu before cooking to remove excess water for better texture.",
            "warnings": []
        },
        "dal": {
            "food_name": "Dal (Lentil Curry)",
            "serving_size": "1 cup (200g)",
            "calories_per_serving": 230,
            "protein_g": 18.0, "carbs_g": 40.0, "fat_g": 1.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Best plant protein", "High fiber", "Rich in iron"],
            "tips": "Add a squeeze of lemon for better iron absorption.",
            "warnings": []
        },
        "lentil": {
            "food_name": "Lentils",
            "serving_size": "1 cup cooked (200g)",
            "calories_per_serving": 230,
            "protein_g": 18.0, "carbs_g": 40.0, "fat_g": 1.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["High plant protein", "Excellent fiber", "Heart healthy"],
            "tips": "Combine with rice for a complete protein meal.",
            "warnings": []
        },
        "chickpea": {
            "food_name": "Chickpeas",
            "serving_size": "1 cup (164g)",
            "calories_per_serving": 270,
            "protein_g": 15.0, "carbs_g": 45.0, "fat_g": 4.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "Half to 1 cup per day",
            "best_time_to_eat": "Lunch or snack",
            "benefits": ["High protein and fiber", "Regulates blood sugar", "Good for gut health"],
            "tips": "Use in salads, curries or roast for a healthy snack.",
            "warnings": []
        },
        "rajma": {
            "food_name": "Rajma (Kidney Beans)",
            "serving_size": "1 cup (200g)",
            "calories_per_serving": 230,
            "protein_g": 13.0, "carbs_g": 40.0, "fat_g": 3.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day with rice or roti",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["High protein for vegetarians", "Rich in fiber", "Good iron source"],
            "tips": "Soak overnight before cooking to reduce cooking time and gas.",
            "warnings": []
        },

        # ── Dairy ──────────────────────────────────────────────────────────
        "milk": {
            "food_name": "Milk",
            "serving_size": "1 glass (250ml)",
            "calories_per_serving": 150,
            "protein_g": 8.0, "carbs_g": 12.0, "fat_g": 8.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 glasses per day",
            "best_time_to_eat": "Morning or before bed",
            "benefits": ["Rich in calcium", "Good protein", "Vitamin D"],
            "tips": "Choose low fat milk if watching calories.",
            "warnings": ["Avoid if lactose intolerant"]
        },
        "yogurt": {
            "food_name": "Greek Yogurt",
            "serving_size": "1 cup (200g)",
            "calories_per_serving": 100,
            "protein_g": 17.0, "carbs_g": 6.0, "fat_g": 0.7,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Breakfast or snack",
            "benefits": ["High protein", "Probiotics for gut health", "Low fat"],
            "tips": "Choose plain over flavoured to avoid added sugar.",
            "warnings": []
        },
        "curd": {
            "food_name": "Curd (Dahi)",
            "serving_size": "1 cup (200g)",
            "calories_per_serving": 120,
            "protein_g": 8.0, "carbs_g": 9.0, "fat_g": 5.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Lunch or as a snack",
            "benefits": ["Probiotics for digestion", "Good calcium source", "Cooling effect"],
            "tips": "Eat at room temperature rather than cold for better digestion.",
            "warnings": []
        },

        # ── Fruits ─────────────────────────────────────────────────────────
        "banana": {
            "food_name": "Banana",
            "serving_size": "1 medium banana (118g)",
            "calories_per_serving": 89,
            "protein_g": 1.1, "carbs_g": 23.0, "fat_g": 0.3,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 per day",
            "best_time_to_eat": "Morning or pre-workout",
            "benefits": ["Rich in potassium", "Natural energy boost", "Vitamin B6"],
            "tips": "Eat slightly unripe for lower sugar and more resistant starch.",
            "warnings": ["Diabetics monitor intake"]
        },
        "apple": {
            "food_name": "Apple",
            "serving_size": "1 medium (182g)",
            "calories_per_serving": 95,
            "protein_g": 0.5, "carbs_g": 25.0, "fat_g": 0.3,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 per day",
            "best_time_to_eat": "Morning snack",
            "benefits": ["High fiber", "Rich in antioxidants", "Regulates blood sugar"],
            "tips": "Eat with the skin for maximum fiber.",
            "warnings": []
        },
        "orange": {
            "food_name": "Orange",
            "serving_size": "1 medium (131g)",
            "calories_per_serving": 62,
            "protein_g": 1.2, "carbs_g": 15.0, "fat_g": 0.2,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 per day",
            "best_time_to_eat": "Morning or snack",
            "benefits": ["Very high Vitamin C", "Boosts immunity", "Low calorie"],
            "tips": "Eat whole rather than juice to keep the fiber.",
            "warnings": []
        },
        "mango": {
            "food_name": "Mango",
            "serving_size": "1 cup sliced (165g)",
            "calories_per_serving": 107,
            "protein_g": 1.4, "carbs_g": 28.0, "fat_g": 0.4,
            "health_rating": "Moderate",
            "recommended_daily_amount": "Half to 1 cup per day",
            "best_time_to_eat": "Morning or afternoon",
            "benefits": ["Rich in Vitamin A and C", "Supports immunity", "Good for skin"],
            "tips": "Eat in moderation as it is high in natural sugar.",
            "warnings": ["High sugar — diabetics should limit"]
        },
        "watermelon": {
            "food_name": "Watermelon",
            "serving_size": "2 cups (280g)",
            "calories_per_serving": 85,
            "protein_g": 1.7, "carbs_g": 21.0, "fat_g": 0.4,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 cups per day",
            "best_time_to_eat": "Afternoon snack",
            "benefits": ["92% water — great hydration", "Low calorie", "Rich in lycopene"],
            "tips": "Best eaten fresh on its own as a snack.",
            "warnings": []
        },
        "grapes": {
            "food_name": "Grapes",
            "serving_size": "1 cup (150g)",
            "calories_per_serving": 104,
            "protein_g": 1.1, "carbs_g": 27.0, "fat_g": 0.2,
            "health_rating": "Moderate",
            "recommended_daily_amount": "Half to 1 cup per day",
            "best_time_to_eat": "Snack",
            "benefits": ["Rich in antioxidants", "Heart healthy", "Anti-inflammatory"],
            "tips": "Choose red or purple grapes for more antioxidants.",
            "warnings": ["Diabetics limit due to natural sugars"]
        },

        # ── Vegetables ─────────────────────────────────────────────────────
        "salad": {
            "food_name": "Mixed Salad",
            "serving_size": "1 large bowl (200g)",
            "calories_per_serving": 80,
            "protein_g": 3.0, "carbs_g": 10.0, "fat_g": 2.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 bowls per day",
            "best_time_to_eat": "With any meal",
            "benefits": ["Very low calorie", "High vitamins", "Great for weight loss"],
            "tips": "Add protein like boiled eggs or chickpeas to make it a full meal.",
            "warnings": []
        },
        "broccoli": {
            "food_name": "Broccoli",
            "serving_size": "1 cup (90g)",
            "calories_per_serving": 55,
            "protein_g": 3.7, "carbs_g": 11.0, "fat_g": 0.6,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Anti-cancer compounds", "Very high Vitamin C", "High fiber"],
            "tips": "Steam instead of boil to preserve nutrients.",
            "warnings": []
        },
        "spinach": {
            "food_name": "Spinach",
            "serving_size": "1 cup cooked (180g)",
            "calories_per_serving": 41,
            "protein_g": 5.3, "carbs_g": 6.8, "fat_g": 0.5,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Very high iron", "Rich in Vitamin K", "Eye health"],
            "tips": "Cook with a little fat to improve absorption of fat-soluble vitamins.",
            "warnings": []
        },
        "carrot": {
            "food_name": "Carrots",
            "serving_size": "1 cup (128g)",
            "calories_per_serving": 52,
            "protein_g": 1.2, "carbs_g": 12.0, "fat_g": 0.3,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Any time as snack or with meals",
            "benefits": ["Very high beta-carotene", "Good for eyesight", "Boosts immunity"],
            "tips": "Eat cooked carrots for better beta-carotene absorption.",
            "warnings": []
        },
        "sweet potato": {
            "food_name": "Sweet Potato",
            "serving_size": "1 medium (130g)",
            "calories_per_serving": 130,
            "protein_g": 2.0, "carbs_g": 30.0, "fat_g": 0.1,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 medium per day",
            "best_time_to_eat": "Lunch or snack",
            "benefits": ["Very high Vitamin A", "High fiber", "Natural sweetness"],
            "tips": "Bake or steam — avoid frying.",
            "warnings": ["Diabetics monitor intake"]
        },

        # ── Indian dishes ──────────────────────────────────────────────────
        "biryani": {
            "food_name": "Chicken Biryani",
            "serving_size": "1 plate (300g)",
            "calories_per_serving": 450,
            "protein_g": 20.0, "carbs_g": 55.0, "fat_g": 15.0,
            "health_rating": "Moderate",
            "recommended_daily_amount": "1 plate occasionally — not daily",
            "best_time_to_eat": "Lunch",
            "benefits": ["Good protein from chicken", "Spices have anti-inflammatory properties"],
            "tips": "Choose smaller portions and pair with raita to balance the meal.",
            "warnings": ["High calorie — limit if trying to lose weight"]
        },
        "samosa": {
            "food_name": "Samosa",
            "serving_size": "2 pieces (100g)",
            "calories_per_serving": 300,
            "protein_g": 5.0, "carbs_g": 35.0, "fat_g": 15.0,
            "health_rating": "Unhealthy",
            "recommended_daily_amount": "Limit to 1-2 pieces occasionally",
            "best_time_to_eat": "Occasional snack only",
            "benefits": ["Contains vegetables inside"],
            "tips": "Baked samosas are a much healthier alternative to fried.",
            "warnings": ["Deep fried — high in unhealthy fat", "High calorie snack"]
        },
        "curry": {
            "food_name": "Vegetable Curry",
            "serving_size": "1 cup (200g)",
            "calories_per_serving": 180,
            "protein_g": 5.0, "carbs_g": 28.0, "fat_g": 6.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1 cup per meal",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["Spices boost metabolism", "Good fiber", "Anti-inflammatory"],
            "tips": "Use less oil and coconut milk to reduce calories.",
            "warnings": []
        },
        "palak": {
            "food_name": "Palak Paneer",
            "serving_size": "1 cup (200g)",
            "calories_per_serving": 260,
            "protein_g": 15.0, "carbs_g": 12.0, "fat_g": 18.0,
            "health_rating": "Moderate",
            "recommended_daily_amount": "1 cup per day",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": ["High protein from paneer", "Iron from spinach", "Calcium rich"],
            "tips": "Use low fat paneer to reduce calorie content.",
            "warnings": ["High fat — limit if high cholesterol"]
        },

        # ── Snacks & Fast food ─────────────────────────────────────────────
        "pizza": {
            "food_name": "Pizza",
            "serving_size": "2 slices (200g)",
            "calories_per_serving": 500,
            "protein_g": 20.0, "carbs_g": 58.0, "fat_g": 20.0,
            "health_rating": "Unhealthy",
            "recommended_daily_amount": "Limit to 1-2 slices occasionally",
            "best_time_to_eat": "Occasional treat at lunch",
            "benefits": ["Calcium from cheese"],
            "tips": "Choose thin crust with vegetables and less cheese.",
            "warnings": ["High sodium and saturated fat", "Not suitable for daily consumption"]
        },
        "burger": {
            "food_name": "Burger",
            "serving_size": "1 regular burger (200g)",
            "calories_per_serving": 450,
            "protein_g": 22.0, "carbs_g": 40.0, "fat_g": 20.0,
            "health_rating": "Unhealthy",
            "recommended_daily_amount": "Limit to once a week maximum",
            "best_time_to_eat": "Occasional lunch only",
            "benefits": ["Some protein from patty"],
            "tips": "Choose grilled over fried patty and add extra vegetables.",
            "warnings": ["High in sodium and saturated fat", "Low in fiber"]
        },
        "nuts": {
            "food_name": "Mixed Nuts",
            "serving_size": "1 small handful (30g)",
            "calories_per_serving": 180,
            "protein_g": 5.0, "carbs_g": 6.0, "fat_g": 16.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "30g per day — do not exceed",
            "best_time_to_eat": "Morning snack",
            "benefits": ["Healthy fats for heart", "Rich in Vitamin E", "Keeps you full"],
            "tips": "Choose unsalted and unroasted nuts for maximum benefit.",
            "warnings": ["High calorie — easy to overeat"]
        },
        "almonds": {
            "food_name": "Almonds",
            "serving_size": "20 almonds (28g)",
            "calories_per_serving": 164,
            "protein_g": 6.0, "carbs_g": 6.0, "fat_g": 14.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "20-25 almonds per day",
            "best_time_to_eat": "Morning snack",
            "benefits": ["Heart healthy fats", "High Vitamin E", "Brain health"],
            "tips": "Soak overnight before eating for better nutrient absorption.",
            "warnings": []
        },

        # ── Drinks ─────────────────────────────────────────────────────────
        "tea": {
            "food_name": "Chai (Milk Tea)",
            "serving_size": "1 cup (200ml)",
            "calories_per_serving": 60,
            "protein_g": 2.0, "carbs_g": 8.0, "fat_g": 2.0,
            "health_rating": "Moderate",
            "recommended_daily_amount": "1-2 cups per day maximum",
            "best_time_to_eat": "Morning or evening",
            "benefits": ["Antioxidants from tea", "Mental alertness"],
            "tips": "Use less sugar and less milk for a healthier cup.",
            "warnings": ["Too much can affect iron absorption", "Limit sugar"]
        },
        "coffee": {
            "food_name": "Black Coffee",
            "serving_size": "1 cup (240ml)",
            "calories_per_serving": 5,
            "protein_g": 0.3, "carbs_g": 0.0, "fat_g": 0.0,
            "health_rating": "Healthy",
            "recommended_daily_amount": "1-2 cups per day",
            "best_time_to_eat": "Morning",
            "benefits": ["Boosts metabolism", "Improves focus", "Rich in antioxidants"],
            "tips": "Avoid adding sugar — try with a little milk if needed.",
            "warnings": ["Avoid after 2pm — affects sleep"]
        },
    }

    # ── Match filename to food ────────────────────────────────────────────────
    matched_food = None
    for keyword, data in food_knowledge.items():
        if keyword in filename:
            matched_food = data
            break

    # ── Default if not recognized ─────────────────────────────────────────────
    if not matched_food:
        matched_food = {
            "food_name": f"Food Item ({filename.title()})",
            "serving_size": "1 standard serving (100g)",
            "calories_per_serving": 200,
            "protein_g": 8.0, "carbs_g": 25.0, "fat_g": 7.0,
            "health_rating": "Moderate",
            "recommended_daily_amount": "1 serving per meal as part of a balanced diet",
            "best_time_to_eat": "Lunch or dinner",
            "benefits": [
                "Provides essential macronutrients",
                "Part of a balanced diet",
                "Contributes to daily calorie needs"
            ],
            "tips": "Rename your image file to the food name for accurate results. Example: rice.jpg, chicken.jpg, banana.jpg",
            "warnings": []
        }

    return matched_food