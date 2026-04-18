from fpdf import FPDF
import random

def generate_medical_report(name, age, details):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Medical Report", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Patient Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Details: {details}", ln=True)
    pdf.ln(10)
    
    # Blood test info
    pdf.cell(200, 10, txt="Blood Test Results:", ln=True)
    tests = ["Hemoglobin", "White Blood Cells", "Red Blood Cells", "Platelets", "Cholesterol", "Glucose", "Triglycerides", "HDL", "LDL"]
    for test in tests:
        value = random.randint(50, 200)
        pdf.cell(200, 10, txt=f"{test}: {value} mg/dL", ln=True)
    
    # Add more pages
    for page in range(2, 6):  # 5 pages total
        pdf.add_page()
        pdf.cell(200, 10, txt=f"Page {page} - Additional Notes", ln=True)
        pdf.multi_cell(0, 10, txt="This is additional medical information. The patient is a software development engineer working in a multinational company. He was born and brought up in West Bengal, studied at NIT Durgapur, and loves gymming. Dummy IDs: Voter ID: ABC1234567, Aadhar: 1234-5678-9012, PAN: ABCDE1234F.")
        # More dummy blood tests
        pdf.ln(10)
        for i in range(5):
            test = random.choice(tests)
            value = random.randint(50, 200)
            pdf.cell(200, 10, txt=f"{test}: {value} mg/dL", ln=True)
    
    return pdf

# Generate two reports
report1 = generate_medical_report("John Doe", 28, "SDE in MNC, born in WB, studied in NIT Durgapur, loves gymming")
report1.output("/Users/sahilgupta/Desktop/personal-ai-knowledge-vault/data/raw/medical_report_1.pdf")

report2 = generate_medical_report("Jane Smith", 30, "Similar profile, additional tests")
report2.output("/Users/sahilgupta/Desktop/personal-ai-knowledge-vault/data/raw/medical_report_2.pdf")

print("Dummy PDFs created.")