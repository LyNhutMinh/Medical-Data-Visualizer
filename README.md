<h1 align="center">🏥 Medical Data Visualizer</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white" alt="Seaborn">
  <img src="https://img.shields.io/badge/freeCodeCamp-0A0A23?style=for-the-badge&logo=freecodecamp&logoColor=white" alt="freeCodeCamp">
</div>

<br>

## 📝 Overview
This is the third project of the **Data Analysis with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/). The core objective is to investigate and visualize the relationships between cardiac disease, body measurements, blood markers, and lifestyle choices using a robust data science stack (**Pandas, Seaborn, and Matplotlib**).

## ⚙️ Data Processing & Feature Engineering
Before generating visualizations, the raw medical examination dataset (`medical_examination.csv`) required strict data cleaning and feature engineering:
* **BMI Calculation:** Engineered an `overweight` column by calculating the Body Mass Index (BMI). Patients with a BMI > 25 were classified as overweight (1), and others as not (0).
* **Data Normalization:** Standardized the `cholesterol` and `gluc` (glucose) columns. Values of 1 (normal) were mapped to 0 ("good"), while values > 1 (above normal/well above normal) were mapped to 1 ("bad").
* **Outlier Removal:** Filtered out erroneous data segments, specifically:
  * Records where diastolic pressure was higher than systolic pressure.
  * Records where height and weight fell below the 2.5th percentile or above the 97.5th percentile.

## 📊 Visualizations

### 1. Categorical Plot
This plot illustrates the counts of good and bad outcomes for various health metrics (cholesterol, glucose, smoking, alcohol intake, and physical activity), explicitly split by the presence or absence of cardiovascular disease (`cardio`).
<div align="center">
  <img width="1058" alt="Categorical Plot" src="https://github.com/user-attachments/assets/e1e9edf5-dfee-4553-ad5f-320cff588303" />
</div>

### 2. Correlation Heat Map
A triangular correlation matrix visualized using a Seaborn masked heatmap. It displays the Pearson correlation coefficients between all numerical variables in the cleaned dataset, making it easy to spot strong relationships (e.g., weight and height).
<div align="center">
  <img width="1200" alt="Heat Map" src="https://github.com/user-attachments/assets/5f6287cb-6347-49ad-87d4-57390fcc6d85" />
</div>

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/LyNhutMinh/Medical-Data-Visualizer.git](https://github.com/LyNhutMinh/Medical-Data-Visualizer.git)
