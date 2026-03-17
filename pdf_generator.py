from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def clean_report(report):
    report = report.replace("**", "")
    report = report.replace("\n", "<br/>")
    return report

def generate_pdf(student, report, filename):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph("STUDENT PERFORMANCE REPORT", styles['Title']))
    content.append(Spacer(1, 15))

    # Student Info Table
    info_data = [
        ["Name", student['name']],
        ["Class", student['class']],
        ["Attendance", f"{student['attendance']}%"],
        ["Behavior", student['behavior']]
    ]

    info_table = Table(info_data, colWidths=[120, 250])
    info_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("PADDING", (0,0), (-1,-1), 6),
    ]))

    content.append(info_table)
    content.append(Spacer(1, 20))

    # Marks Table
    marks_data = [["Subject", "Marks"]]
    for subject, mark in student["marks"].items():
        marks_data.append([subject, mark])

    marks_table = Table(marks_data, colWidths=[200, 100])
    marks_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("ALIGN", (1,1), (-1,-1), "CENTER"),
        ("PADDING", (0,0), (-1,-1), 6),
    ]))

    content.append(Paragraph("ACADEMIC PERFORMANCE", styles['Heading2']))
    content.append(Spacer(1, 10))
    content.append(marks_table)
    content.append(Spacer(1, 20))

    # Clean AI Report
    formatted_report = clean_report(report)

    content.append(Paragraph("TEACHER'S REMARKS", styles['Heading2']))
    content.append(Spacer(1, 10))
    content.append(Paragraph(formatted_report, styles['Normal']))

    doc.build(content)