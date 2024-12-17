# KAIM3 Week 1  

Welcome to the **KAIM3 Week 1** repository! This repository focuses on analyzing financial news articles and stock data using Python. It includes data loading, exploratory analysis, sentiment analysis, time series analysis, and quantitative stock analysis tasks.  

## Table of Contents  
- [Overview](#overview)  
- [Key Analyses](#key-analyses)  
- [Folder Structure](#folder-structure)  
- [Setup and Requirements](#setup-and-requirements)  
- [Usage](#usage)  
- [License](#license)  

---

## Overview  

This project loads and analyzes financial datasets, performs headline sentiment analysis, and generates insights into stock trends. Key features include:  
- Data preprocessing of stock and news data  
- Exploratory Data Analysis (EDA)  
- Sentiment analysis of headlines  
- Time series analysis for articles  
- Quantitative analysis for stock trends  

---

## Key Analyses  

### **1. Data Loading and Preparation**  
- Load libraries such as Pandas, Matplotlib, and Scikit-learn.  
- Process financial news data from a CSV file and stock price data.  

### **2. Exploratory Data Analysis (EDA)**  
- Calculate headline lengths and descriptive statistics.  
- Analyze article frequency per month, year, and specific high-activity days.  
- Identify March 12, 2020, as having the **highest article frequency**.  

### **3. Text Analysis**  
- Perform sentiment analysis to categorize headlines as positive, negative, or neutral.  
- Identify common bigrams in headlines, such as *"52 week"* and *"stocks moving"*.  
- Insights focus on market movements, analyst actions, and earnings updates.  

### **4. Time Series Analysis**  
- Plot time series data of article counts.  
- Analyze article publication times, showing peaks during early hours of the day.  

### **5. Publisher Analysis**  
- Analyze sentiment by publishers.  
- Identify the most frequent publisher, such as **benzinga.com**.  

### **6. Quantitative Analysis**  
- Load historical stock price data.  
- Calculate moving averages (SMA, EMA) to analyze trends.  
- Plot stock trends to visualize price movements.  

---

## Folder Structure  

```plaintext  
KAIM3-week1/  
│  
├── .github/workflows/     # GitHub workflows (e.g., unittest.yml)  
├── .vscode/               # VSCode configuration  
│   └── settings.json  
│  
├── notebooks/             # Jupyter Notebooks  
│   ├── data/              # Data files (CSV, processed)  
│   ├── __init__.py  
│   └── data_processing.ipynb  
│  
├── scripts/               # Python scripts  
│   ├── __init__.py  
│   ├── plot.py            # Plotting functions  
│   ├── utils.py           # Utility functions  
│   └── README.md  
│  
├── src/                   # Source code  
│   └── __init__.py  
│  
├── tests/                 # Test files  
│   └── __init__.py  
│  
├── .gitignore             # Git ignore file  
├── requirements.txt       # Python dependencies  
└── README.md              # Documentation  
```  

---

## Setup and Requirements  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/JONNY-ME/KAIM3-week1.git  
   cd KAIM3-week1  
   ```  

2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Data**: Ensure the required CSV files (e.g., news articles, stock data) are in the `notebooks/data` directory.  

---


**Happy Analyzing! 🚀**  