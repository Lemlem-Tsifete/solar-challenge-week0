# 🌞 Solar Data Discovery – Week 0 Challenge  

## 📘 Project Overview
This project analyzes solar radiation data from **Benin**, **Togo**, and **Sierra Leone** to identify the most promising country for solar energy investment.  
It was completed as part of **10 Academy’s Artificial Intelligence Mastery – Week 0 Challenge**.

---

## 🧩 Tasks Completed
### ✅ Task 1 – Git & Environment Setup
- Created repo: `solar-challenge-week0`
- Setup virtual environment, installed dependencies
- Added `.gitignore`, `requirements.txt`, and GitHub Actions

### ✅ Task 2 – Data Profiling, Cleaning & EDA
- Cleaned and analyzed datasets for each country
- Removed missing values & outliers using Z-score
- Exported cleaned data:
  - `data/benin_clean.csv`
  - `data/togo_clean.csv`
  - `data/sierraleone_clean.csv`

### ✅ Task 3 – Cross-Country Comparison
- Combined all datasets into one DataFrame  
- Compared **GHI**, **DNI**, and **DHI** values  
- Generated visual insights and summary statistics  
- Identified **Benin** as the best candidate for solar development

---

## Key Findings
| Country | Mean GHI | Mean DNI | Mean DHI |
|----------|-----------|-----------|-----------|
| **Benin** | 240.38 | 167.09 | 115.29 |
| **Togo** | 229.93 | 150.89 | 116.21 |
| **Sierra Leone** | 195.98 | 112.40 | 111.79 |

 **Conclusion:**  
Benin demonstrates the highest solar energy potential, followed by Togo and Sierra Leone.

---

## Technologies Used
- **Python**: Pandas, NumPy, Matplotlib, Seaborn, SciPy  
- **Version Control**: Git & GitHub  
- **Environment**: venv / Anaconda  
- **Visualization**: Jupyter Notebooks & Streamlit *(optional)*  

---

## Repository Structure
```
solar-challenge-week0/
|
├── app/
│   └── main.py  
├── data/
│   ├── benin_clean.csv
│   ├── togo_clean.csv
│   ├── sierraleone_clean.csv
│
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   └── compare_countries.ipynb
│
├── src/
├── tests/
├── .github/workflows/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run
1. Clone the repo  
   ```bash
   git clone https://github.com/Lemlem-Tsifete/solar-challenge-week0.git
   cd solar-challenge-week0
   ```
2. Create a virtual environment and install dependencies:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
3. Run notebooks inside `/notebooks/` to reproduce analysis.  

---
## ✅ Task 4 – Dashboard Development (Streamlit)
Developed an interactive dashboard to visualize solar energy data across the three countries.
**Features :**
- Country filter (Benin, Togo, Sierra Leone)
- Summary statistics (Mean GHI, DNI, DHI)
- Boxplots and bar charts
- Correlation heatmap toggle
- Responsive and modern layout

## How to Run

# Activate environment
venv\Scripts\activate

# Run Streamlit app
streamlit run app/main.py

Access the dashboard locally at:
 http://localhost:8501
---

## Author
**Lemlem Tsifete**  
Junior Data & Machine Learning Enthusiast  
10 Academy – Artificial Intelligence Mastery Cohort 

## 💡 Acknowledgment

- Special thanks to 10 Academy mentors and peers for continuous guidance and collaboration during this project.