
# 🧭 PrepTrack

> **Student Placement Readiness Evaluation System**

---

## 📖 Executive Summary

PrepTrack is a Python-based command-line application that evaluates a student's placement readiness through a structured assessment workflow. The system validates student information, analyzes seven days of coding practice, calculates performance metrics, and generates a detailed placement readiness report.

---

## 🎯 Objectives

- Evaluate placement readiness
- Validate academic and profile information
- Analyze coding practice performance
- Generate performance analytics
- Produce actionable recommendations

---

## ✨ Feature Matrix

| Feature | Description | Status |
|:--------|:------------|:------:|
| Student Registration | Collects and validates student details | ✅ |
| Attendance Validation | Validates attendance percentage | ✅ |
| Practice Evaluation | Processes seven days of practice | ✅ |
| Performance Classification | Categorizes daily scores | ✅ |
| Performance Analytics | Calculates total, average, highest & lowest | ✅ |
| Critical Score Detection | Detects first critical score | ✅ |
| Placement Eligibility | Evaluates readiness | ✅ |
| Report Generation | Generates final report | ✅ |

---

## 📊 Evaluation Criteria

| Evaluation Metric | Requirement | Purpose |
|:------------------|:-----------:|:--------|
| Graduation Year | `2025–2027` | Eligible academic batch |
| Attendance | `≥ 75%` | Minimum attendance requirement |
| Practice Attempts | `≥ 6` | Ensures consistent practice |
| Passed Days | `≥ 4` | Demonstrates coding proficiency |
| Average Score | `≥ 70` | Indicates overall performance |
| Critical Scores | `None` | No score below 40 allowed |
| Project Status | `Completed` | Academic project completed |
| Profile Status | `Verified` | Student profile verified |

---

## 📈 Performance Classification

| Score Range | Category |
|:-----------:|:---------|
| 75 – 100 | Strong |
| 60 – 74 | Satisfactory |
| 40 – 59 | Needs Improvement |
| 0 – 39 | Critical |

---

## 🏗️ System Workflow

```text
Student Details
      │
      ▼
Input Validation
      │
      ▼
Practice Evaluation
      │
      ▼
Performance Analysis
      │
      ▼
Placement Eligibility
      │
      ▼
Final Report
```

---

## 🛠️ Technology Stack

| Category | Technology |
|:---------|:-----------|
| Language | Python 3 |
| Interface | Command Line (CLI) |
| IDE | Visual Studio Code |
| Version Control | Git |
| Repository | GitHub |

---

## 📁 Repository Structure

```text
PrepTrack/
├── main.py
├── README.md
└── output.txt
```

---

## ⚙️ Version Control Workflow

The project was developed incrementally using Git. Each completed module was committed with a meaningful commit message before being pushed to the GitHub repository.

### Step 1: Clone the Repository

```bash
git clone https://github.com/rahul777-code/preptrack-rahul.git
cd preptrack-rahul
```

### Step 2: Stage the Changes

```bash
git add .
```

### Step 3: Commit Each Module

```bash
git commit -m "Implement student profile validation"
git commit -m "Add attendance validation"
git commit -m "Develop practice score evaluation"
git commit -m "Implement performance classification"
git commit -m "Add performance analytics"
git commit -m "Generate placement readiness report"
git commit -m "Update README documentation"
```

> **Note:** Each completed module should have its own descriptive commit message instead of using generic messages like `"update"` or `"final"`.

### Step 4: Run the Application

```bash
python main.py
```

Follow the interactive prompts in the terminal to enter student details and seven days of practice scores. After processing the input, the application generates a detailed placement readiness report.

### Step 5: Push Changes to GitHub

```bash
git push origin main
```

## 📋 Report Summary

| **Report Section** | **Description** |
|:-------------------|:----------------|
| 👤 Student Information | Displays student profile and academic details. |
| 📅 Attendance Analysis | Shows attendance percentage and eligibility. |
| 💻 Practice Summary | Summarizes attempted, absent, passed, and failed practice days. |
| 📊 Performance Metrics | Displays total score, average score, highest score, and lowest score. |
| 🚨 Critical Analysis | Identifies the first critical score, if any. |
| 🎯 Placement Evaluation | Displays placement readiness status and eligibility result. |
| 💡 Recommendations | Suggests the next action based on the evaluation. |
---

## 🧠 Python Concepts Used

| Concept | Purpose |
|:--------|:--------|
| Variables | Store data |
| Data Types | Student information |
| Input Validation | Validate entries |
| if / elif / else | Decision making |
| while Loop | Repeated validation |
| for Loop | Process seven days |
| break / continue | Flow control |
| Boolean Logic | Eligibility checks |
| try / except | Handle invalid input |
| f-Strings | Formatted output |

---

## 🚀 Future Enhancements

- Database integration
- Multi-user support
- Login authentication
- GUI version
- PDF report generation
- Analytics dashboard
- AI-based recommendations

---

## 👨‍💻 Author

| Field | Information |
|:------|:------------|
| Name | Rahul S |
| Project | PrepTrack |
| GitHub |https://github.com/rahul777-code/preptrack-rahul|

---

## 📄 License

This project is intended for academic and educational purposes.
