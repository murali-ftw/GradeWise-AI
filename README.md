# 🎓 GPT-Based Student Report Generator

## 📌 Overview

This project is an NLP-based application that automatically generates detailed student performance reports using Generative AI (GPT models).

The system takes structured student data (marks, attendance, behavior) and produces human-like feedback similar to what a teacher would write.

---

## 🚀 Features

* Automated report generation using GPT
* Personalized feedback for each student
* Structured output (performance, strengths, weaknesses, suggestions)
* Handles multiple students
* Saves reports to file
* Modular and scalable design

---

## 🧠 Technologies Used

* Python
* OpenAI GPT API
* JSON (for data storage)
* Natural Language Processing (NLP)

---

## 🏗️ System Architecture

Student Data → Preprocessing → Prompt Engineering → GPT Model → Report Output

---

## 📂 Project Structure

gpt-student-report-generator/
│
├── main.py                # Entry point
├── report_generator.py    # Core NLP logic
├── config.py              # API key configuration
├── students.json          # Input data
├── requirements.txt       # Dependencies
├── reports/               # Output folder
│   └── output.txt
└── README.md              # Documentation

---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone <your-repo-link>
cd gpt-student-report-generator

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add API Key

Open config.py and replace:
API_KEY = "YOUR_API_KEY"

### 4. Create output folder

mkdir reports

---

## ▶️ Usage

Run the program:

python main.py

The system will:

* Read student data from students.json
* Generate reports using GPT
* Print results in terminal
* Save reports in reports/output.txt

---

## 🧪 Sample Input

{
"name": "Rahul",
"marks": "Math: 85, Science: 78, English: 90",
"attendance": "92%",
"behavior": "Good"
}

---

## 📝 Sample Output

Rahul has demonstrated strong academic performance, particularly in English.
He maintains good attendance and shows positive classroom behavior.
With more focus on Science, he can further improve his results.

---

## 🧩 Key Concepts

### 🔹 Natural Language Processing (NLP)

Used to generate meaningful human-like feedback.

### 🔹 Generative AI

The model creates new text instead of selecting existing content.

### 🔹 Prompt Engineering

Carefully designed prompts guide the model to produce structured reports.

---

## ⚠️ Challenges

* Output depends on prompt quality
* Requires API usage
* May produce generic feedback if input is limited

---

## 🔮 Future Enhancements

* Web interface (Streamlit)
* Multi-language report generation
* Integration with school databases
* Real-time performance tracking

---

## 👥 Team Contribution

* 23N248 - Sanjeev MS: Introduction & Problem Statement
* 23N236 - Pranika S: System Overview & Architecture
* 23N205 - Abishiek C: Data Handling & Preprocessing
* 23N230 - Muralikarthik : Model & Implementation
* 24N434 - Priyanka S: Evaluation & Analysis

---

## 📚 Conclusion

This project demonstrates how NLP and Generative AI can automate student feedback generation, reducing teacher workload while maintaining quality and personalization.

---

## 🙌 Acknowledgment

We thank our faculty and institution for supporting this NLP project.

---
