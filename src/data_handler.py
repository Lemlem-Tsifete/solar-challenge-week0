import pandas as pd
from scipy.stats import zscore

class SolarDataProcessor:
    """
    Handles loading, cleaning, and summarizing solar data.
    """

    def __init__(self, filepath: str, country: str):
        self.filepath = filepath
        self.country = country
        self.data = pd.read_csv(filepath)
        self.cleaned_data = None

    def clean_data(self):
        """Clean the dataset: fill numeric nulls and remove outliers."""
        df = self.data.copy()

        # ✅ Fill only numeric columns with their median
        num_cols = df.select_dtypes(include='number').columns
        df[num_cols] = df[num_cols].fillna(df[num_cols].median())

        # ✅ Remove outliers using Z-score on GHI only
        if "GHI" in df.columns:
            df['z_GHI'] = zscore(df['GHI'])
            df = df[df['z_GHI'].abs() < 3]
            df.drop(columns=['z_GHI'], inplace=True)

        # ✅ Add country label
        df["Country"] = self.country

        self.cleaned_data = df
        return df

    def summarize(self):
        """Return summary statistics for GHI, DNI, and DHI."""
        if self.cleaned_data is None:
            raise ValueError("Please run clean_data() first.")
        summary = self.cleaned_data[["GHI", "DNI", "DHI"]].describe().T[["mean", "50%", "std"]]
        summary.columns = ["Mean", "Median", "Std"]
        summary["Country"] = self.country
        return summary.reset_index().rename(columns={"index": "Metric"})
