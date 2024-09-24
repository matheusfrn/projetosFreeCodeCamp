import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_and_visualize():
    df = pd.read_csv("medical_examination.csv")

    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    return df

def draw_cat_plot(df):
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).size()

    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count", height=5, aspect=1).fig

    return fig

def draw_heat_map(df):
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, cmap='coolwarm', cbar_kws={"shrink": 0.5})

    return fig

if __name__ == "__main__":
    df = load_and_visualize()

    fig_cat = draw_cat_plot(df)
    fig_cat.savefig('catplot.png')

    fig_heat = draw_heat_map(df)
    fig_heat.savefig('heatmap.png')
