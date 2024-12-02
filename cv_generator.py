from fpdf import FPDF
from input_handler import get_input

def create_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", 'B', 20)
    pdf.cell(200, 10, txt="Resume", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {data['Name']}", ln=True)
    pdf.cell(200, 10, txt=f"Contact: {data['Contact']}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {data['Address']}", ln=True)
    
    pdf.cell(200, 10, txt="Career Objective:", ln=True)
    pdf.multi_cell(0, 10, txt=data['Objective'])
    
    pdf.cell(200, 10, txt="Education:", ln=True)
    for edu in data['Education']:
        pdf.multi_cell(0, 10, txt=f"{edu['degree']} from {edu['institution']} ({edu['year']})")

    pdf.cell(200, 10, txt="Experience:", ln=True)
    for exp in data['Experience']:
        pdf.multi_cell(0, 10, txt=f"{exp['job_title']} at {exp['company']} ({exp['year_start']} - {exp['year_end']})")
    
    pdf.cell(200, 10, txt="Skills:", ln=True)
    pdf.multi_cell(0, 10, txt=", ".join(data['Skills']))

    pdf.output(f"{data['Name']}_Resume.pdf")
    print(f"Resume saved as {data['Name']}_Resume.pdf")

def main():
    data = get_input()
    create_pdf(data)


main()
