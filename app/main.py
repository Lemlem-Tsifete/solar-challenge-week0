import sys
import os

# ✅ Add project root to Python path first — before other imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.data_handler import SolarDataProcessor
from src.visualization import plot_bar, plot_box
from src.stats_analysis import anova_test

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("🌞 Solar Energy Data Comparison Dashboard")

@st.cache_data
def load_all_data():
    countries = {
        "Benin": "data/benin_clean.csv",
        "Togo": "data/togo_clean.csv",
        "Sierra Leone": "data/sierraleone_clean.csv"
    }
    datasets = []
    for name, path in countries.items():
        processor = SolarDataProcessor(path, name)
        df = processor.clean_data()
        datasets.append(df)
    return datasets

datasets = load_all_data()
combined_df = pd.concat(datasets)
selected = st.sidebar.multiselect("Select countries", combined_df["Country"].unique(), combined_df["Country"].unique())
filtered = combined_df[combined_df["Country"].isin(selected)]

# Summary table
st.subheader("Summary Statistics")
summary = filtered.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])
st.dataframe(summary)

# Visuals
st.subheader("Visualizations")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_bar(filtered))
with col2:
    st.pyplot(plot_box(filtered))

# ANOVA test
st.subheader("Statistical Comparison (ANOVA)")
result = anova_test(*datasets)
st.write(result)
