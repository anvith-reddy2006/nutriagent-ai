# app.py
# Dietician AI Agent - Professional UI
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agent import DieticianAgent

st.set_page_config(
    page_title="NutriAgent AI",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background: #f0faf5; }
    [data-testid="stSidebar"] { background: #1a6b4a; }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
    }
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] div {
        color: #0f4c35 !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] {
        background-color: #ffffff !important;
    }
    [data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] div {
        color: #0f4c35 !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] input {
        background-color: #ffffff !important;
        color: #0f4c35 !important;
    }
    .hero-section {
        background: linear-gradient(135deg, #0f4c35, #1D9E75);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero-title { font-size: 3rem; font-weight: 800; color: white; margin: 0; }
    .hero-subtitle { color: #c8e6c9; font-size: 1.1rem; margin-top: 0.5rem; }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        border: 1px solid rgba(255,255,255,0.4);
        border-radius: 20px;
        padding: 0.3rem 1rem;
        color: white;
        font-size: 0.8rem;
        margin: 0.3rem;
    }
    .steps-row { display: flex; gap: 1rem; margin-bottom: 2rem; }
    .step-box {
        flex: 1; background: white; border-radius: 12px;
        padding: 1rem; text-align: center; border: 1px solid #c8e6c9;
    }
    .step-number {
        width: 36px; height: 36px;
        background: linear-gradient(135deg, #1D9E75, #0f4c35);
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        color: white; font-weight: 700; font-size: 1rem;
        margin: 0 auto 0.5rem;
    }
    .step-label { font-size: 0.9rem; font-weight: 700; color: #0f4c35; }
    .step-desc  { font-size: 0.78rem; color: #555; margin-top: 0.2rem; }
    .metric-row {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .metric-box {
        background: white; border-radius: 14px;
        padding: 1.2rem 1rem; text-align: center; border: 1px solid #c8e6c9;
    }
    .metric-value { font-size: 1.6rem; font-weight: 700; color: #0f4c35; }
    .metric-label { font-size: 0.75rem; color: #777; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0.2rem; }
    .metric-sub   { font-size: 0.72rem; color: #1D9E75; margin-top: 0.2rem; font-weight: 600; }
    .section-title {
        font-size: 1.3rem; font-weight: 700; color: #0f4c35;
        margin: 2rem 0 1rem; padding-bottom: 0.4rem;
        border-bottom: 2px solid #1D9E75;
    }
    .meal-card {
        background: white; border-radius: 14px;
        padding: 1rem 1.2rem; margin-bottom: 0.8rem;
        border: 1px solid #c8e6c9;
        display: flex; align-items: flex-start; gap: 1rem;
    }
    .meal-icon-box {
        width: 44px; height: 44px; border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.4rem; flex-shrink: 0;
    }
    .meal-icon-breakfast { background: #fff8e1; }
    .meal-icon-lunch     { background: #e8f5e9; }
    .meal-icon-dinner    { background: #e8eaf6; }
    .meal-icon-snack     { background: #fce4ec; }
    .meal-content { flex: 1; }
    .meal-type {
        font-size: 0.7rem; font-weight: 700;
        text-transform: uppercase; letter-spacing: 0.08em; color: #1D9E75;
    }
    .meal-name    { font-size: 1rem; font-weight: 600; color: #0f4c35; margin: 0.1rem 0; }
    .meal-serving { font-size: 0.78rem; color: #777; margin-bottom: 0.4rem; }
    .meal-stats   { display: flex; gap: 0.5rem; flex-wrap: wrap; }
    .meal-stat {
        background: #f0faf5; border-radius: 6px;
        padding: 0.2rem 0.5rem; font-size: 0.72rem;
        color: #0f4c35; font-weight: 500;
    }
    .alert-box {
        background: #fff8e1; border-radius: 12px;
        padding: 0.9rem 1.2rem; border-left: 4px solid #FFC107;
        margin-bottom: 0.6rem; font-size: 0.88rem; color: #5d4e00;
    }
    .totals-card {
        background: linear-gradient(135deg, #0f4c35, #1D9E75);
        border-radius: 14px; padding: 1.2rem; color: white;
    }
    .totals-title {
        font-size: 0.8rem; text-transform: uppercase;
        letter-spacing: 0.08em; color: #c8e6c9;
        margin-bottom: 0.8rem; font-weight: 700;
    }
    .totals-row {
        display: flex; justify-content: space-between;
        padding: 0.4rem 0; border-bottom: 1px solid rgba(255,255,255,0.15);
    }
    .totals-row:last-child { border-bottom: none; }
    .totals-key { font-size: 0.82rem; color: #c8e6c9; }
    .totals-val { font-size: 0.95rem; font-weight: 700; color: white; }
    .features-row {
        display: grid; grid-template-columns: repeat(4, 1fr);
        gap: 1rem; margin-bottom: 2rem; align-items: stretch;
    }
    .welcome-feature {
        background: white; border-radius: 14px; padding: 1.5rem;
        text-align: center; border: 1px solid #c8e6c9;
        display: flex; flex-direction: column;
        align-items: center; justify-content: flex-start;
        min-height: 200px;
    }
    .feature-icon  { font-size: 2.5rem; margin-bottom: 0.8rem; }
    .feature-title { font-size: 1rem; font-weight: 700; color: #0f4c35; margin-bottom: 0.5rem; }
    .feature-desc  { font-size: 0.85rem; color: #555; line-height: 1.6; }
    .vision-result {
        background: white; border-radius: 14px;
        padding: 1.5rem; border: 1px solid #c8e6c9;
    }
    .nutrition-grid {
        display: grid; grid-template-columns: repeat(4, 1fr);
        gap: 0.6rem; margin: 1rem 0;
    }
    .nutrition-cell {
        background: #f0faf5; border-radius: 8px;
        padding: 0.6rem; text-align: center;
    }
    .nutrition-val   { font-size: 1.1rem; font-weight: 700; color: #0f4c35; }
    .nutrition-label { font-size: 0.7rem; color: #777; margin-top: 0.1rem; }
    .stButton > button {
        background: linear-gradient(135deg, #1D9E75, #0f4c35) !important;
        color: white !important; border: none !important;
        border-radius: 10px !important; font-weight: 700 !important;
        font-size: 1rem !important; padding: 0.7rem !important;
    }
    .macro-info {
        background: #e8f5e9; border-radius: 10px;
        padding: 0.8rem 1rem; margin-top: 0.8rem;
        font-size: 0.8rem; color: #0f4c35;
        border-left: 3px solid #1D9E75;
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🥗 NutriAgent AI</div>
    <div class="hero-subtitle">Your personalised AI-powered dietician</div>
    <div style="margin-top:1rem;">
        <span class="hero-badge">Goal-based AI Agent</span>
        <span class="hero-badge">Rule-based Reasoning</span>
        <span class="hero-badge">Greedy Search Algorithm</span>
        <span class="hero-badge">Knowledge Base</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Steps ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="steps-row">
    <div class="step-box">
        <div class="step-number">1</div>
        <div class="step-label">Perceive</div>
        <div class="step-desc">Collects your health profile and goals</div>
    </div>
    <div class="step-box">
        <div class="step-number">2</div>
        <div class="step-label">Reason</div>
        <div class="step-desc">Calculates BMR, TDEE and macro targets</div>
    </div>
    <div class="step-box">
        <div class="step-number">3</div>
        <div class="step-label">Act</div>
        <div class="step-desc">Searches food database with greedy algorithm</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:1rem 0 1.5rem;'>
        <div style='font-size:2.5rem;'>🥗</div>
        <div style='font-size:1.2rem;font-weight:700;color:#ffffff;'>NutriAgent AI</div>
        <div style='font-size:0.8rem;color:#c8e6c9;margin-top:0.3rem;'>Fill your profile below</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='color:#ffffff;font-weight:700;font-size:0.95rem;'>👤 Personal Details</p>",
                unsafe_allow_html=True)
    age    = st.slider("Age (years)",  15,  80, 25)
    weight = st.slider("Weight (kg)",  30, 150, 70)
    height = st.slider("Height (cm)", 140, 220, 170)
    sex    = st.radio("Sex", ["Male", "Female"], horizontal=True)

    st.markdown("<hr style='border-color:rgba(255,255,255,0.2);'>", unsafe_allow_html=True)
    st.markdown("<p style='color:#ffffff;font-weight:700;font-size:0.95rem;'>🎯 Health Goal</p>",
                unsafe_allow_html=True)
    goal = st.selectbox("Select your goal", ["Lose Weight","Maintain Weight","Gain Muscle"])

    st.markdown("<p style='color:#ffffff;font-weight:700;font-size:0.95rem;'>🏃 Activity Level</p>",
                unsafe_allow_html=True)
    activity = st.selectbox("Select activity level", [
        "Sedentary (little or no exercise)",
        "Lightly Active (1-3 days/week)",
        "Moderately Active (3-5 days/week)",
        "Very Active (6-7 days/week)",
        "Athlete (twice a day training)"
    ])

    st.markdown("<p style='color:#ffffff;font-weight:700;font-size:0.95rem;'>🥦 Diet Type</p>",
                unsafe_allow_html=True)
    diet_type = st.selectbox("Select diet type", ["Non-Vegetarian","Vegetarian","Vegan"])

    st.markdown("<p style='color:#ffffff;font-weight:700;font-size:0.95rem;'>🏥 Medical Conditions</p>",
                unsafe_allow_html=True)
    conditions = st.multiselect("Select if any", ["Diabetes","High Blood Pressure","High Cholesterol"])

    st.markdown("<hr style='border-color:rgba(255,255,255,0.2);'>", unsafe_allow_html=True)
    generate_btn = st.button("🚀 Generate My Diet Plan", use_container_width=True)


# ── Food Analyzer ─────────────────────────────────────────────────────────────
def show_food_analyzer():
    st.markdown('<div class="section-title">📸 Food Image Analyzer</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <div style="background:white;border-radius:14px;padding:1rem 1.5rem;
    border:1px solid #c8e6c9;margin-bottom:1.5rem;">
        <div style="font-size:1rem;font-weight:600;color:#0f4c35;margin-bottom:0.3rem;">
            Don't know the nutrition of a food? Upload a photo!
        </div>
        <div style="font-size:0.85rem;color:#555;">
            Rename your image to the food name before uploading.
            Example: <strong>rice.jpg</strong>, <strong>chicken.jpg</strong>,
            <strong>banana.jpg</strong>, <strong>biryani.jpg</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    img_col1, img_col2 = st.columns([1, 1])
    with img_col1:
        uploaded_image = st.file_uploader(
            "Upload a food photo",
            type=["jpg","jpeg","png","webp"],
            key="food_uploader"
        )
        analyze_btn = st.button("🔍 Analyze Food", use_container_width=True, key="analyze_btn")
        if uploaded_image:
            st.image(uploaded_image, caption="Your uploaded food", use_column_width=True)

    with img_col2:
        if analyze_btn and uploaded_image:
            with st.spinner("Analyzing your food..."):
                try:
                    from food_vision import analyze_food_image_free
                    uploaded_image.seek(0)
                    nutrition = analyze_food_image_free(uploaded_image)
                    rating_colors = {
                        "Healthy":   "#1D9E75",
                        "Moderate":  "#F2A623",
                        "Unhealthy": "#E24B4A"
                    }
                    rc = rating_colors.get(nutrition.get("health_rating","Moderate"), "#F2A623")
                    st.markdown(f"""
                    <div class="vision-result">
                        <div style="display:flex;justify-content:space-between;
                        align-items:center;margin-bottom:0.8rem;">
                            <div>
                                <div style="font-size:1.3rem;font-weight:700;
                                color:#0f4c35;">{nutrition['food_name']}</div>
                                <div style="font-size:0.8rem;color:#777;">
                                Serving: {nutrition['serving_size']}</div>
                            </div>
                            <div style="background:{rc};color:white;padding:0.3rem 0.8rem;
                            border-radius:20px;font-size:0.8rem;font-weight:600;">
                                {nutrition['health_rating']}
                            </div>
                        </div>
                        <div class="nutrition-grid">
                            <div class="nutrition-cell">
                                <div class="nutrition-val">{nutrition['calories_per_serving']}</div>
                                <div class="nutrition-label">kcal</div>
                            </div>
                            <div class="nutrition-cell">
                                <div class="nutrition-val" style="color:#1D9E75;">
                                {nutrition['protein_g']}g</div>
                                <div class="nutrition-label">protein</div>
                            </div>
                            <div class="nutrition-cell">
                                <div class="nutrition-val" style="color:#378ADD;">
                                {nutrition['carbs_g']}g</div>
                                <div class="nutrition-label">carbs</div>
                            </div>
                            <div class="nutrition-cell">
                                <div class="nutrition-val" style="color:#F2A623;">
                                {nutrition['fat_g']}g</div>
                                <div class="nutrition-label">fat</div>
                            </div>
                        </div>
                        <div style="background:#e8f5e9;border-radius:8px;
                        padding:0.8rem;margin-bottom:0.8rem;">
                            <div style="font-size:0.72rem;font-weight:700;
                            color:#0f4c35;margin-bottom:0.3rem;">RECOMMENDED DAILY AMOUNT</div>
                            <div style="font-size:0.88rem;color:#1a6b4a;">
                            {nutrition['recommended_daily_amount']}</div>
                        </div>
                        <div style="background:#fff8e1;border-radius:8px;
                        padding:0.8rem;margin-bottom:0.8rem;">
                            <div style="font-size:0.72rem;font-weight:700;
                            color:#633806;margin-bottom:0.3rem;">BEST TIME TO EAT</div>
                            <div style="font-size:0.88rem;color:#5d4e00;">
                            {nutrition['best_time_to_eat'].capitalize()}</div>
                        </div>
                        <div style="margin-bottom:0.8rem;">
                            <div style="font-size:0.72rem;font-weight:700;
                            color:#0f4c35;margin-bottom:0.4rem;">HEALTH BENEFITS</div>
                            {"".join([f'<div style="font-size:0.82rem;color:#1a6b4a;padding:0.15rem 0;">✓ {b}</div>'
                            for b in nutrition['benefits']])}
                        </div>
                        <div style="background:#f8f9fa;border-radius:8px;padding:0.8rem;">
                            <div style="font-size:0.72rem;font-weight:700;
                            color:#0f4c35;margin-bottom:0.3rem;">DIETICIAN TIP</div>
                            <div style="font-size:0.82rem;color:#555;">
                            {nutrition['tips']}</div>
                        </div>
                        {"".join([f'<div class="alert-box" style="margin-top:0.5rem;">⚠️ {w}</div>'
                        for w in nutrition.get("warnings",[])])}
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error analyzing image: {str(e)}")
        elif analyze_btn and not uploaded_image:
            st.warning("Please upload a food image first.")
        else:
            st.markdown("""
            <div style="background:#f8f9fa;border-radius:14px;padding:2.5rem;
            text-align:center;border:2px dashed #c8e6c9;margin-top:1rem;">
                <div style="font-size:2.5rem;margin-bottom:0.8rem;">📸</div>
                <div style="font-size:0.95rem;font-weight:600;color:#0f4c35;
                margin-bottom:0.4rem;">Upload any food photo</div>
                <div style="font-size:0.82rem;color:#888;line-height:1.6;">
                Rename file to food name<br>
                e.g. rice.jpg · chicken.jpg · banana.jpg · biryani.jpg
                </div>
            </div>
            """, unsafe_allow_html=True)


# ── Main ──────────────────────────────────────────────────────────────────────
if generate_btn:
    user_profile = {
        "age": age, "weight": weight, "height": height,
        "sex": sex, "goal": goal, "activity_level": activity,
        "diet_type": diet_type, "conditions": conditions,
    }

    with st.spinner("Agent is thinking... perceiving → reasoning → acting..."):
        agent = DieticianAgent()
        agent.run(user_profile)
        results = agent.get_results()

    weekly = results["weekly_plan"]
    days   = list(weekly.keys())

    # ── Warnings ──────────────────────────────────────────────────────────────
    if results["warnings"]:
        st.markdown('<div class="section-title">⚠️ Dietary Alerts</div>',
                    unsafe_allow_html=True)
        for w in results["warnings"]:
            st.markdown(f'<div class="alert-box">⚠️ {w}</div>',
                        unsafe_allow_html=True)

    # ── Key metrics ───────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">📊 Your Nutritional Targets</div>',
                unsafe_allow_html=True)
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-box">
            <div class="metric-value">{results['bmi']}</div>
            <div class="metric-label">BMI</div>
            <div class="metric-sub">{results['bmi_category']}</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">{results['bmr']}</div>
            <div class="metric-label">BMR (kcal)</div>
            <div class="metric-sub">Resting calories</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">{results['tdee']}</div>
            <div class="metric-label">TDEE (kcal)</div>
            <div class="metric-sub">Daily energy need</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">{results['calorie_goal']}</div>
            <div class="metric-label">Calorie Goal</div>
            <div class="metric-sub">{goal}</div>
        </div>
        <div class="metric-box">
            <div class="metric-value" style="font-size:1rem;">{diet_type}</div>
            <div class="metric-label">Diet Type</div>
            <div class="metric-sub">Your preference</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Macro section — uses actual Monday totals so numbers always match ─────
    st.markdown('<div class="section-title">🍽️ Daily Nutrition Breakdown</div>',
                unsafe_allow_html=True)

    # Get actual totals from Monday meals
    monday          = weekly["Monday"]["totals"]
    actual_calories = monday["calories"]
    actual_protein  = monday["protein"]
    actual_carbs    = monday["carbs"]
    actual_fat      = monday["fat"]

    col_macro, col_pie = st.columns([1, 1])

    with col_macro:
        st.markdown(f"""
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
            <div class="metric-box">
                <div class="metric-value" style="color:#1D9E75;">{actual_protein}g</div>
                <div class="metric-label">Protein</div>
                <div class="metric-sub">4 kcal per gram</div>
            </div>
            <div class="metric-box">
                <div class="metric-value" style="color:#378ADD;">{actual_carbs}g</div>
                <div class="metric-label">Carbs</div>
                <div class="metric-sub">4 kcal per gram</div>
            </div>
            <div class="metric-box">
                <div class="metric-value" style="color:#F2A623;">{actual_fat}g</div>
                <div class="metric-label">Fat</div>
                <div class="metric-sub">9 kcal per gram</div>
            </div>
            <div class="metric-box">
                <div class="metric-value" style="color:#0f4c35;">{actual_calories}</div>
                <div class="metric-label">Total kcal</div>
                <div class="metric-sub">Monday total</div>
            </div>
        </div>
        <div class="macro-info">
            ✓ Protein {actual_protein}g × 4 = {round(actual_protein*4)} kcal &nbsp;|&nbsp;
            Carbs {actual_carbs}g × 4 = {round(actual_carbs*4)} kcal &nbsp;|&nbsp;
            Fat {actual_fat}g × 9 = {round(actual_fat*9)} kcal &nbsp;|&nbsp;
            <strong>Total = {round(actual_protein*4 + actual_carbs*4 + actual_fat*9)} kcal</strong>
        </div>
        """, unsafe_allow_html=True)

    with col_pie:
        fig_pie = px.pie(
            values=[actual_protein*4, actual_carbs*4, actual_fat*9],
            names=["Protein", "Carbohydrates", "Fat"],
            color_discrete_sequence=["#1D9E75", "#378ADD", "#F2A623"],
            hole=0.55
        )
        fig_pie.update_traces(textposition="outside", textinfo="percent+label")
        fig_pie.update_layout(
            showlegend=False,
            margin=dict(t=20,b=20,l=20,r=20),
            height=260,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # ── 7 day plan ────────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">📅 Your 7-Day Meal Plan</div>',
                unsafe_allow_html=True)

    tabs = st.tabs(days)
    meal_config = {
        "breakfast": ("🌅","meal-icon-breakfast"),
        "lunch":     ("☀️","meal-icon-lunch"),
        "dinner":    ("🌙","meal-icon-dinner"),
        "snack":     ("🍎","meal-icon-snack"),
    }

    for i, tab in enumerate(tabs):
        with tab:
            day_plan = weekly[days[i]]
            totals   = day_plan.get("totals",{})
            left, right = st.columns([2,1])

            with left:
                for meal_type, (icon, icon_class) in meal_config.items():
                    if meal_type in day_plan:
                        item = day_plan[meal_type]
                        st.markdown(f"""
                        <div class="meal-card">
                            <div class="meal-icon-box {icon_class}">{icon}</div>
                            <div class="meal-content">
                                <div class="meal-type">{meal_type}</div>
                                <div class="meal-name">{item['food']}</div>
                                <div class="meal-serving">📏 {item['serving_size']}</div>
                                <div class="meal-stats">
                                    <span class="meal-stat">🔥 {item['calories']} kcal</span>
                                    <span class="meal-stat">💪 {item['protein']}g protein</span>
                                    <span class="meal-stat">🌾 {item['carbs']}g carbs</span>
                                    <span class="meal-stat">🧈 {item['fat']}g fat</span>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

            with right:
                # Daily summary shows actual sum of meals
                t_pro  = totals.get('protein',0)
                t_carb = totals.get('carbs',0)
                t_fat  = totals.get('fat',0)
                t_cal  = totals.get('calories',0)
                check  = round(t_pro*4 + t_carb*4 + t_fat*9)
                st.markdown(f"""
                <div class="totals-card">
                    <div class="totals-title">Daily Total</div>
                    <div class="totals-row">
                        <span class="totals-key">Calories</span>
                        <span class="totals-val">{t_cal} kcal</span>
                    </div>
                    <div class="totals-row">
                        <span class="totals-key">Protein</span>
                        <span class="totals-val">{t_pro}g</span>
                    </div>
                    <div class="totals-row">
                        <span class="totals-key">Carbs</span>
                        <span class="totals-val">{t_carb}g</span>
                    </div>
                    <div class="totals-row">
                        <span class="totals-key">Fat</span>
                        <span class="totals-val">{t_fat}g</span>
                    </div>
                    <div style="margin-top:0.8rem;padding-top:0.6rem;
                    border-top:1px solid rgba(255,255,255,0.2);
                    font-size:0.72rem;color:#c8e6c9;line-height:1.6;">
                    ✓ {t_pro}×4 + {t_carb}×4 + {t_fat}×9<br>
                    = {check} kcal from macros
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # ── Weekly bar chart ──────────────────────────────────────────────────────
    st.markdown('<div class="section-title">📈 Weekly Calorie Overview</div>',
                unsafe_allow_html=True)
    week_cals = {day: weekly[day]["totals"]["calories"] for day in days}
    fig_bar   = go.Figure()
    fig_bar.add_trace(go.Bar(
        x=list(week_cals.keys()), y=list(week_cals.values()),
        marker_color="#1D9E75",
        text=list(week_cals.values()), textposition="outside",
        textfont=dict(color="#0f4c35", size=12)
    ))
    fig_bar.add_hline(
        y=results["calorie_goal"], line_dash="dash",
        line_color="#F2A623", line_width=2,
        annotation_text=f"  Target: {results['calorie_goal']} kcal",
        annotation_font_color="#F2A623"
    )
    fig_bar.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(
            gridcolor="rgba(0,0,0,0.05)",
            title=dict(text="Calories (kcal)", font=dict(color="#0f4c35")),
            tickfont=dict(color="#0f4c35")
        ),
        xaxis=dict(tickfont=dict(color="#0f4c35")),
        height=350, margin=dict(t=30,b=30)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ── Full table ────────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">📋 Full Weekly Plan Table</div>',
                unsafe_allow_html=True)
    rows = []
    for day, plan in weekly.items():
        for meal_type in ["breakfast","lunch","dinner","snack"]:
            if meal_type in plan:
                item = plan[meal_type]
                rows.append({
                    "Day":         day,
                    "Meal":        meal_type.capitalize(),
                    "Food":        item["food"],
                    "Serving":     item["serving_size"],
                    "Calories":    item["calories"],
                    "Protein (g)": item["protein"],
                    "Carbs (g)":   item["carbs"],
                    "Fat (g)":     item["fat"],
                })
    df_table = pd.DataFrame(rows)
    st.dataframe(df_table, use_container_width=True, hide_index=True)
    csv = df_table.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Full Meal Plan as CSV",
        data=csv, file_name="nutriagent_meal_plan.csv",
        mime="text/csv", use_container_width=True
    )

    show_food_analyzer()

else:
    st.markdown("""
    <div style="text-align:center;padding:1rem 0 2rem;">
        <div style="font-size:1.05rem;color:#444;">
            Fill in your profile on the left and click
            <strong style="color:#0f4c35;">Generate My Diet Plan</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="features-row">
        <div class="welcome-feature">
            <div class="feature-icon">🧮</div>
            <div class="feature-title">BMR Calculator</div>
            <div class="feature-desc">Uses Harris-Benedict formula to calculate your base metabolic rate from age, weight, height and sex</div>
        </div>
        <div class="welcome-feature">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Greedy Search</div>
            <div class="feature-desc">Scans 40+ foods and picks the best calorie-matching meals for breakfast, lunch, dinner and snack</div>
        </div>
        <div class="welcome-feature">
            <div class="feature-icon">🏥</div>
            <div class="feature-title">Condition Aware</div>
            <div class="feature-desc">Automatically removes unsuitable foods for diabetes, high blood pressure and high cholesterol</div>
        </div>
        <div class="welcome-feature">
            <div class="feature-icon">📸</div>
            <div class="feature-title">Food Analyzer</div>
            <div class="feature-desc">Upload any food photo to get full nutrition info, serving size and daily recommendations</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    show_food_analyzer()