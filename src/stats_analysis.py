from scipy.stats import f_oneway

def anova_test(*datasets):
    """
    Performs a one-way ANOVA test across multiple datasets.
    Returns F-statistic and p-value.
    """
    f_stat, p_val = f_oneway(*[df["GHI"] for df in datasets])
    return {"F-statistic": f_stat, "p-value": p_val}
