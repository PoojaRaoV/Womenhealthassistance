class ReportAnalysis:

    def analyze_thyroid(self, tsh):
        if tsh < 0.4:
            return "Hyperthyroidism (Low TSH)"
        elif tsh > 4.0:
            return "Hypothyroidism (High TSH)"
        else:
            return "Normal Thyroid"

    def analyze_hemoglobin(self, hb):
        if hb < 12:
            return "Anemia (Low Hemoglobin)"
        else:
            return "Normal Hemoglobin"
        
        def pcos_risk(self, irregular_periods, weight_gain):
            if irregular_periods and weight_gain:
                return "High chance of PCOS - consult doctor"
                return "Low risk"