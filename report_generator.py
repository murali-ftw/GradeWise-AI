from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def calculate_percentage(marks):
    return round(sum(marks.values()) / len(marks), 2)

def create_prompt(student):
    percentage = calculate_percentage(student["marks"])

    prompt = f"""
You are an experienced school teacher.

Generate a professional student performance report.

Student Details:
Name: {student['name']}
Class: {student['class']}
Percentage: {percentage}%
Attendance: {student['attendance']}%
Behavior: {student['behavior']}

Marks:
English: {student['marks']['English']}
Math: {student['marks']['Math']}
Science: {student['marks']['Science']}
Social: {student['marks']['Social']}
Physical Education: {student['marks']['Physical Education']}

The report must include:
1. Overall Performance
2. Subject-wise Analysis
3. Strengths
4. Areas for Improvement
5. Suggestions
6. Final Remark

Keep it structured in plain text. Do not use markdown symbols like ** or bullet points. Use simple sentences with line breaks.
Do Not Print name, class, attendance, percentage, behavior in the report. Give an analysis.
"""
    return prompt


def generate_report(student):
    prompt = create_prompt(student)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful and professional school teacher."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content