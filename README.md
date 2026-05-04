## 🌐 Live Demo
https://nutriagent-ai-x2y5pnr46xr3mnthzmxt6y.streamlit.app# NutriAgent AI — Dietician AI Agent

## What is this project?

NutriAgent AI is a dietician agent I built as part of my AIKR S2026 course project. The idea came from a simple problem — most people do not know how many calories they need or what to eat based on their health condition and goals. This agent solves that by taking your basic health details and generating a full 7-day personalised meal plan with exact serving sizes and nutrition info.It also helps you in knowing how many calories protiens are there in the food that you eat by clicking the picture of it

The agent works in three steps:
1. It collects your health profile (age, weight, height, goal)
2. It calculates your calorie needs using the BMR formula
3. It searches a food database and builds your meal plan

## Agent Details

- Agent Type  : Goal-based AI Agent
- AI Logic    : Rule-based reasoning + Greedy Search Algorithm
- Language    : Python 3.10
- UI          : Streamlit web app
- Dataset     : Custom food nutrition CSV (40+ foods)

## Project Structure

DieticianAgent/
├── source_code/
│   ├── agent.py          main agent — perceive, reason, act
│   ├── calculator.py     BMR, TDEE and macro calculations
│   ├── meal_planner.py   greedy search over food database
│   ├── app.py            streamlit web interface
│   └── food_vision.py    food image analyzer
├── dataset/
│   └── food_data.csv     food nutrition knowledge base
├── README.md
└── requirements.txt

## How to Install and Run

Step 1 — Go into the project folder
    cd DieticianAgent

Step 2 — Create a virtual environment
    python3 -m venv venv

Step 3 — Activate it
    source venv/bin/activate

Step 4 — Install the required packages
    pip install -r requirements.txt

Step 5 — Run the app
    cd source_code
    streamlit run app.py

Step 6 — Open your browser
    Go to http://localhost:8501

## How to Use It

1. Fill in your details on the left side panel
   - your age, weight, height and sex
   - your health goal (lose weight / maintain / gain muscle)
   - your activity level
   - your diet type (non-veg / vegetarian / vegan)
   - any medical conditions you have

2. Click Generate My Diet Plan

3. You will see:
   - your BMI, BMR, TDEE and daily calorie target
   - your protein, carbs and fat targets
   - a full 7-day meal plan with serving sizes
   - a macro pie chart and weekly calorie bar chart
   - option to download your meal plan as a CSV file

4. Scroll down to use the Food Image Analyzer
   - upload a photo of any food
   - rename the photo to the food name before uploading
     for example: rice.jpg or chicken.jpg or banana.jpg
   - it shows full nutrition info and how much to eat

## Example

Input:
  Age 25, Weight 80kg, Height 175cm, Male
  Goal: Lose Weight
  Activity: Moderately Active
  Diet: Non-Vegetarian
  Conditions: None

Output:
  BMI: 26.1 — Overweight
  BMR: 1897 kcal
  TDEE: 2940 kcal
  Calorie Goal: 2440 kcal
  Protein: 214g | Carbs: 244g | Fat: 68g
  7-day meal plan with breakfast lunch dinner and snack
  Each meal includes food name, serving size and full nutrition

## AI Techniques Used

Rule-based reasoning
  Used the Harris-Benedict equation to calculate BMR and TDEE.
  Applied goal-based macro splits and condition filtering rules.

Greedy Search Algorithm
  For each meal slot the agent picks the food from the database whose calories are closest to the target. This is greedy because it always takes the locally best option at each step.

Knowledge Base
  The food_data.csv file acts as the knowledge base. It stores 40+ foods with their calories, protein, carbs, fat, sugar, sodium and serving size.

## AI Tools Declaration

I used Claude AI while building this project.
It helped me with:
  - understanding the agent architecture design
  - structuring my Python files
  - debugging errors and indentation with comments in the code
  - styling the Streamlit UI

Claude helped me to understand topic more detail and clearly suggested few codes
I wrote the core logic myself — the BMR formulas, the greedy search, the condition rules and the food knowledge base.
I did not copy a full project. Claude was used like a coding assistant to help me learn and build faster.

## Requirements

streamlit==1.55.0
pandas==2.3.3
plotly==6.6.0
numpy==2.2.6
pillow==12.1.1

## Developer

Name        : Anvith Kilari
Roll Number : S20240030380
Course      : AIKR S2026
Due Date    : 04 May 2026
