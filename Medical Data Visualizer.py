import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column
# BMI = weight (kg) / [height (m)]^2. Lưu ý: height trong data tính bằng cm nên phải chia cho 100.
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data (0 là tốt, 1 là xấu)
# cholesterol và gluc: 1 -> 0 (tốt), 2 hoặc 3 -> 1 (xấu)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # 4. Create DataFrame for cat plot using pd.melt
    # Chỉ lấy các cột phân loại (categorical)
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 5. Group and reformat the data to split it by cardio
    # Đếm số lượng của từng biến và gộp lại
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 6 & 7. Create a chart that shows the value counts using sns.catplot()
    fig = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar'
    ).fig # Lấy đối tượng figure từ seaborn facetgrid

    # 8. Do not modify the next two lines (Lưu biểu đồ thành file ảnh)
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 9. Clean the data
    # Lọc bỏ các dòng dữ liệu vô lý (huyết áp tâm trương > tâm thu, chiều cao/cân nặng quá bất thường)
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 10. Calculate the correlation matrix
    # Tính ma trận tương quan giữa các cột
    corr = df_heat.corr()

    # 11. Generate a mask for the upper triangle
    # Tạo mặt nạ để che nửa trên của ma trận (vì ma trận tương quan có tính đối xứng)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 13. Plot the correlation matrix using sns.heatmap()
    # Vẽ biểu đồ nhiệt với các thông số tùy chỉnh cho đẹp mắt
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt='.1f', 
        center=0, 
        vmin=-0.1, 
        vmax=0.25, 
        cbar_kws={'shrink': .5}, 
        square=True, 
        linewidths=.5
    )

    # 14. Do not modify the next two lines (Lưu biểu đồ thành file ảnh)
    fig.savefig('heatmap.png')
    return fig


if __name__ == '__main__':
    draw_cat_plot()
    draw_heat_map()