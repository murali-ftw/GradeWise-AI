from data import students
from report_generator import generate_report
from pdf_generator import generate_pdf

def main():
    roll = input("Enter Student Roll Number: ")

    if roll not in students:
        print("Student not found!")
        return

    student = students[roll]

    print("\nGenerating report...\n")

    report = generate_report(student)

    filename = f"reports/{student['name']}_report.pdf"

    generate_pdf(student, report, filename)

    print(f"PDF generated successfully: {filename}")

main()