from flask import Flask, render_template, request
from module3_app import HealthSystem

app = Flask(__name__)
system = HealthSystem()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            name = request.form["name"]
            age = int(request.form["age"])
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            condition = request.form["condition"]
            period = request.form["period"]
            tsh = float(request.form["tsh"])
            hb = float(request.form["hb"])

            data = system.process_user_data(name, age, height, weight, condition)
            next_period = system.get_period_prediction(period)
            report = system.analyze_reports(tsh, hb)

            result = {
                "bmi": data["bmi"],
                "category": data["category"],
                "period": next_period,
                "thyroid": report["thyroid"],
                "hemoglobin": report["hemoglobin"]
            }

            return render_template("index.html", result=result)

        except Exception:
            return render_template("index.html", result="Invalid Input")

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)