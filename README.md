# 📊 Loan Repayment Schedule Calculator

A web app to generate and visualize loan repayment schedules based on EMI or loan duration. Built with Flask + Chart.js, with support to download the schedule as an Excel file.

---

## 🚀 Features

- Calculate EMI or loan duration
- View full monthly schedule (EMI, Interest, Principal)
- Line chart visualization (Interest vs Principal)
- Export repayment schedule as Excel file

---

## 🛠 Setup Instructions

### 🔗 Prerequisites

- Python 3.8+
- pip (Python package manager)

---

### 💻 Local Setup

#### Step 1: Clone the Repository

```bash
git clone https://github.com/Prashanna313/home-loan-calculator.git
cd home-loan-calculator
```

#### Step 2: Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Run the App

```bash
python app.py
```

App will start at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🪄 One-Click Scripts

### 🐧 Linux / macOS:

```bash
./scripts/run.sh
```

### 🪟 Windows:

```powershell
.\scripts\run.ps1
```

These scripts will:
- Set up a virtual environment
- Install dependencies
- Run the Flask app

---

## 📦 Export

Click the `Download as Excel` button to download the repayment schedule in `.xlsx` format.

---

## 📈 Chart

Visualize principal and interest paid over time using an interactive Chart.js graph.

---

## 🧪 Tech Stack

- Flask
- Chart.js
- Pandas
- XlsxWriter
- Bootstrap

---

## 📬 License

MIT – free for personal or commercial use.
Feel free to modify and distribute.