import tkinter as tk
from tkinter import messagebox
from module3_app import HealthSystem

system = HealthSystem()

def process_data():
    try:
        result = system.process_user_data(
            entry_name.get(),
            int(entry_age.get()),
            float(entry_height.get()),
            float(entry_weight.get()),
            entry_condition.get()
        )

        period = system.get_period_prediction(entry_period.get())
        report = system.analyze_reports(
            float(entry_tsh.get()),
            float(entry_hb.get())
        )

        output_label.config(
            text=f"BMI: {result['bmi']} ({result['category']})\n"
                 f"Next Period: {period}\n"
                 f"Thyroid: {report['thyroid']}\n"
                 f"Hemoglobin: {report['hemoglobin']}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# WINDOW
root = tk.Tk()
root.title("Women's Health Tracker")
root.geometry("600x700")
root.configure(bg="#f5f5f5")

# HEADER
tk.Label(root, text="Women's Health Tracker",
         bg="#d32f2f", fg="white",
         font=("Arial", 16, "bold"),
         pady=10).pack(fill="x")

# CENTER FRAME (important)
center_frame = tk.Frame(root, bg="#f5f5f5")
center_frame.pack(expand=True)

# CARD
card = tk.Frame(center_frame, bg="white", padx=25, pady=25)
card.pack()

def field(label):
    tk.Label(card, text=label, bg="white", anchor="w").pack(fill="x")
    
    entry = tk.Entry(card, font=("Arial", 11), bd=1, relief="solid")
    entry.pack(fill="x", pady=8, ipady=6)   # ipady makes box taller
    
    return entry

# YOUR FIELDS
entry_name = field("Name")
entry_age = field("Age")
entry_height = field("Height (cm)")
entry_weight = field("Weight (kg)")
entry_condition = field("Condition (PCOS/PCOD/None)")
entry_period = field("Last Period Date (MM/DD/YYYY)")
entry_tsh = field("TSH Level")
entry_hb = field("Hemoglobin")

# BUTTON
tk.Button(root, text="Submit",
          bg="#d32f2f", fg="white",
          font=("Arial", 12, "bold"),
          padx=20, pady=5,
          command=process_data).pack(pady=10)

# OUTPUT
output_label = tk.Label(root, text="", bg="#f5f5f5", fg="blue", font=("Arial", 11))
output_label.pack()

root.mainloop()