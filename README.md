# Medical Data Visualizer

This is the third project of the **Data Analysis with Python** certification from freeCodeCamp. In this project, I visualized and made calculations from medical examination data using **Pandas**, **Seaborn**, and **Matplotlib**.

## Project Description

The goal of this project is to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices. I performed the following tasks:
* **Data Cleaning**: Filtered out incorrect data segments (outliers) such as cases where diastolic pressure is higher than systolic, or height/weight fall outside the 2.5th and 97.5th percentiles.
* **Feature Engineering**: Added an `overweight` column based on Body Mass Index (BMI).
* **Data Normalization**: Normalized data to make 0 "good" and 1 "bad" for cholesterol and glucose levels.
* **Categorical Plotting**: Created a chart showing the counts of good and bad outcomes for various health variables, split by cardiovascular disease presence.
* **Heat Map**: Calculated the correlation matrix and visualized it using a masked heatmap.

## Technologies Used
* **Python 3.x**
* **Pandas**: For data cleaning and manipulation.
* **Seaborn & Matplotlib**: For creating complex data visualizations.
* **NumPy**: For mathematical operations and creating the heatmap mask.

## Visualizations

### 1. Categorical Plot
This plot shows the counts of features like cholesterol, glucose, smoking, alcohol intake, and physical activity for patients with and without cardiovascular disease.
<img width="1058" height="500" alt="image" src="https://github.com/user-attachments/assets/e1e9edf5-dfee-4553-ad5f-320cff588303" />


### 2. Correlation Heat Map
This heatmap shows the correlation between all variables in the dataset.
<img width="1200" height="1200" alt="image" src="https://github.com/user-attachments/assets/5f6287cb-6347-49ad-87d4-57390fcc6d85" />


## How to Run
1.  Install the required libraries:
    ```bash
    pip install pandas seaborn matplotlib numpy
    ```
2.  Ensure `medical_examination.csv` is in the project directory.
3.  Run the main script:
    ```bash
    python "Medical Data Visualizer.py"
    ```

---
*Developed as part of the freeCodeCamp Data Analysis Curriculum.*
