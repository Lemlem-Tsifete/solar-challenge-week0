import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# --- Title ---
st.title(" Solar Data Comparison Dashboard")
st.write("Visual comparison of solar irradiance across Benin, Togo, and Sierra Leone")

# --- Load data ---
@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    sierra = pd.read_csv("data/sierraleone_clean.csv")

    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"

    df = pd.concat([benin, togo, sierra])
    return df

df = load_data()

# --- Sidebar ---
st.sidebar.header("🔍 Filter Options")
countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

# Filter data
df_filtered = df[df["Country"].isin(countries)]

# --- Display key metrics ---
st.subheader("📊 Summary Statistics")
summary = df_filtered.groupby("Country")[["GHI", "DNI", "DHI"]].mean().round(2)
st.dataframe(summary)

# --- Chart: Average GHI by Country ---
st.subheader("☀️ Average GHI Comparison")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=df_filtered, x="Country", y="GHI", estimator="mean", ci=None)
plt.ylabel("Mean GHI (W/m²)")
plt.title("Average GHI by Country")
st.pyplot(fig)

# --- Chart: GHI Distribution ---
st.subheader("📈 GHI Distribution by Country")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df_filtered, x="Country", y="GHI")
plt.ylabel("GHI (W/m²)")
st.pyplot(fig2)

# --- Optional: Correlation Heatmap ---
if st.checkbox("Show Correlation Heatmap"):
    corr = df_filtered[["GHI", "DNI", "DHI"]].corr()
    fig3, ax3 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)

st.markdown("---")
st.caption("Developed by Lemlem Tsifete | 10 Academy Week 0 Challenge")
