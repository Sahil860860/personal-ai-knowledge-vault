from fpdf import FPDF

def generate_resume():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Resume - John Doe", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Personal Information:", ln=True)
    pdf.cell(200, 10, txt="Name: John Doe", ln=True)
    pdf.cell(200, 10, txt="Age: 28", ln=True)
    pdf.cell(200, 10, txt="Location: Kolkata, West Bengal", ln=True)
    pdf.cell(200, 10, txt="Email: john.doe@example.com", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Education:", ln=True)
    pdf.cell(200, 10, txt="B.Tech in Computer Science, NIT Durgapur (2015-2019)", ln=True)
    pdf.cell(200, 10, txt="High School, West Bengal Board (2013-2015)", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Work Experience:", ln=True)
    pdf.cell(200, 10, txt="Software Development Engineer, TechCorp MNC (2020-Present)", ln=True)
    pdf.multi_cell(0, 10, txt="Developed scalable web applications using Python, React, and cloud technologies. Led a team of 5 developers on microservices architecture.")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Skills:", ln=True)
    pdf.cell(200, 10, txt="- Programming: Python, JavaScript, Java", ln=True)
    pdf.cell(200, 10, txt="- Frameworks: FastAPI, React, Django", ln=True)
    pdf.cell(200, 10, txt="- Tools: Git, Docker, AWS", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Hobbies:", ln=True)
    pdf.cell(200, 10, txt="- Gymming and fitness", ln=True)
    pdf.cell(200, 10, txt="- Reading tech blogs", ln=True)
    
    return pdf

def generate_transcript():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Academic Transcript - NIT Durgapur", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Student Name: John Doe", ln=True)
    pdf.cell(200, 10, txt="Roll Number: CS2015001", ln=True)
    pdf.cell(200, 10, txt="Degree: Bachelor of Technology in Computer Science", ln=True)
    pdf.cell(200, 10, txt="Year of Graduation: 2019", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Semester-wise Grades:", ln=True)
    semesters = [
        ("Semester 1", "8.5"),
        ("Semester 2", "8.7"),
        ("Semester 3", "8.9"),
        ("Semester 4", "9.0"),
        ("Semester 5", "8.8"),
        ("Semester 6", "9.1"),
        ("Semester 7", "8.6"),
        ("Semester 8", "9.2")
    ]
    
    for sem, gpa in semesters:
        pdf.cell(200, 10, txt=f"{sem}: GPA {gpa}", ln=True)
    
    pdf.ln(10)
    pdf.cell(200, 10, txt="Overall CGPA: 8.85", ln=True)
    pdf.cell(200, 10, txt="Honors: Dean's List (Semesters 4, 6, 8)", ln=True)
    
    return pdf

def generate_journal():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Personal Journal - April 15, 2026", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Today's Reflections:", ln=True)
    pdf.multi_cell(0, 10, txt="Today was a productive day at work. I'm working on an exciting AI project at TechCorp. The team is building a knowledge vault system, which reminds me of my own personal goals. Born and raised in West Bengal, I often think about how far I've come from my roots in Kolkata.")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Gym Session:", ln=True)
    pdf.multi_cell(0, 10, txt="Hit the gym after work. Did chest and triceps. Feeling strong! My routine: Bench press 3x10, Incline dumbbells 3x12, Tricep dips 3x15. Loving the progress.")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Goals for Tomorrow:", ln=True)
    pdf.cell(200, 10, txt="- Finish the FastAPI integration", ln=True)
    pdf.cell(200, 10, txt="- Call mom back home in WB", ln=True)
    pdf.cell(200, 10, txt="- Read about vector databases", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Random Thoughts:", ln=True)
    pdf.multi_cell(0, 10, txt="Sometimes I miss the simple life in Durgapur during college. But the opportunities in this MNC are incredible. Balancing work, fitness, and personal growth is key.")
    
    return pdf

# Generate the PDFs
resume_pdf = generate_resume()
resume_pdf.output("/Users/sahilgupta/Desktop/personal-ai-knowledge-vault/data/raw/resume_john_doe.pdf")

transcript_pdf = generate_transcript()
transcript_pdf.output("/Users/sahilgupta/Desktop/personal-ai-knowledge-vault/data/raw/transcript_nit_durgapur.pdf")

journal_pdf = generate_journal()
journal_pdf.output("/Users/sahilgupta/Desktop/personal-ai-knowledge-vault/data/raw/personal_journal_april_2026.pdf")

print("Additional dummy PDFs created.")