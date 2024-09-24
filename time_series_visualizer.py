import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)
    df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    
    return df

def draw_line_plot():
    df = load_and_clean_data()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df = load_and_clean_data()

    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    fig = df_bar.plot(kind='bar', figsize=(12, 6), legend=True).figure
    plt.title("Monthly Average Page Views")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df = load_and_clean_data()

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    df_box['month'] = pd.Categorical(df_box['month'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig

