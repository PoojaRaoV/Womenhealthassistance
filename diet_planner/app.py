from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from diet_planner.diet_logic import (
    generate_weekly_plan,
    generate_monthly_plan,
    generate_yearly_plan
)

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

app = FastAPI()

# ---------------- BMI ----------------
def calculate_bmi(weight, height):
    h = height / 100
    return round(weight / (h * h), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# ---------------- PDF GENERATION (FIXED ALIGNMENT) ----------------
def create_pdf(plan, filename="diet_plan.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    # ✅ IMPORTANT: style for wrapping text
    wrap_style = styles["BodyText"]
    wrap_style.wordWrap = "CJK"   # forces wrapping in ReportLab

    content = []

    content.append(Paragraph("AI Diet Plan - FemAI Care", styles["Title"]))
    content.append(Spacer(1, 12))

    for day, meals in plan.items():

        content.append(Paragraph(day, styles["Heading2"]))

        table_data = [["Meal Type", "Food Items"]]

        if isinstance(meals, dict):
            for meal, foods in meals.items():

                # ✅ FIX 1: Convert foods into clean bullet string
                if isinstance(foods, list):
                    food_text = "<br/>".join([f"• {f}" for f in foods])
                else:
                    food_text = str(foods)

                # ✅ FIX 2: Wrap using Paragraph (THIS FIXES OVERFLOW)
                meal_para = Paragraph(str(meal), wrap_style)
                food_para = Paragraph(food_text, wrap_style)

                table_data.append([meal_para, food_para])

        table = Table(table_data, colWidths=[130, 370], repeatRows=1)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e91e63")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

            # ✅ IMPORTANT FIXES
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),

            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))

        content.append(table)
        content.append(Spacer(1, 15))

    content.append(Spacer(1, 20))
    content.append(Paragraph("© 2026 FemAI Care | Designed for Easy Healthcare Access", styles["Normal"]))

    doc.build(content)


# ---------------- HOME ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>AI Diet Planner</title>

        <style>
            body {
                font-family: Arial;
                background: #fff0f5;
                text-align: center;
                margin: 0;
            }

            header {
                background: #e91e63;
                color: white;
                padding: 15px;
                font-size: 22px;
                font-weight: bold;
            }

            .container {
                width: 420px;
                margin: 40px auto;
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
            }

            input, select {
                width: 95%;
                padding: 10px;
                margin: 10px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
            }

            button {
                background: #e91e63;
                color: white;
                border: none;
                padding: 12px;
                width: 100%;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }

            button:hover {
                background: #c2185b;
            }

            footer {
                background: #e91e63;
                color: white;
                padding: 12px;
                position: fixed;
                bottom: 0;
                width: 100%;
                font-size: 14px;
            }
        </style>
    </head>

    <body>

    <header>FemAI Care</header>

    <div class="container">
        <form action="/generate" method="post">
            <input type="number" name="age" placeholder="Age" required>
            <input type="number" name="weight" placeholder="Weight (kg)" required>
            <input type="number" name="height" placeholder="Height (cm)" required>

            <select name="pcos">
                <option value="1">PCOS: Yes</option>
                <option value="0">PCOS: No</option>
            </select>

            <input type="number" name="hb" placeholder="Hemoglobin" required>

            <select name="plan_type">
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
            </select>

            <button type="submit">Generate Diet Plan</button>
        </form>
    </div>

    <footer>© 2026 FemAI Care | Designed for Easy Healthcare Access</footer>

    </body>
    </html>
    """


# ---------------- GENERATE ----------------
@app.post("/generate", response_class=HTMLResponse)
def generate(
    age: int = Form(...),
    weight: float = Form(...),
    height: float = Form(...),
    pcos: int = Form(...),
    hb: float = Form(...),
    plan_type: str = Form(...)
):

    user = {
        "age": age,
        "weight": weight,
        "height": height,
        "pcos": pcos,
        "hb": hb
    }

    if plan_type == "weekly":
        plan = generate_weekly_plan(user)
    elif plan_type == "monthly":
        plan = generate_monthly_plan(user)
    else:
        plan = generate_yearly_plan(user)

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    # Create PDF
    create_pdf(plan)

    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial;
                background: #fff0f5;
                text-align: center;
            }}

            header {{
                background: #e91e63;
                color: white;
                padding: 15px;
                font-size: 22px;
            }}

            .card {{
                background: white;
                width: 70%;
                margin: 20px auto;
                padding: 20px;
                border-radius: 10px;
                text-align: left;
                box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
            }}

            a {{
                display: inline-block;
                margin-top: 10px;
                padding: 10px;
                background: #e91e63;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }}

            footer {{
                background: #e91e63;
                color: white;
                padding: 12px;
                position: fixed;
                bottom: 0;
                width: 100%;
                font-size: 14px;
            }}
        </style>
    </head>

    <body>

    <header>AI Diet Planner</header>

    <div class="card">
        <h2>Health Summary</h2>
        <p><b>BMI:</b> {bmi}</p>
        <p><b>Category:</b> {category}</p>

        <h3>Your Diet PDF is Ready</h3>

        <a href="/download">⬇ Download PDF</a>
    </div>

    <footer>© 2026 FemAI Care | Designed for Easy Healthcare Access</footer>

    </body>
    </html>
    """


# ---------------- DOWNLOAD ----------------
@app.get("/download")
def download():
    return FileResponse("diet_plan.pdf", media_type="application/pdf", filename="diet_plan.pdf")