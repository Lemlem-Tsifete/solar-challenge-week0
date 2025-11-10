import seaborn as sns
import matplotlib.pyplot as plt

def plot_bar(df):
    """Plot mean GHI per country."""
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(data=df, x="Country", y="GHI", estimator="mean", errorbar=None, ax=ax)
    ax.set_title("Average GHI by Country")
    return fig

def plot_box(df):
    """Plot GHI distribution."""
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(data=df, x="Country", y="GHI", ax=ax)
    ax.set_title("GHI Distribution")
    return fig
