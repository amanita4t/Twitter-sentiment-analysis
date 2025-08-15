import pandas as pd

def load_and_clean_tweets(csv_path="tweets.csv", save_cleaned=False, output_path=None):
    
    # Load CSV
    df = pd.read_csv(csv_path)

    # Standardize column names
    df.columns = ["Index", "Tweet", "Polarity", "Subjectivity"]

    # Remove leading/trailing spaces from text
    df["Tweet"] = df["Tweet"].astype(str).str.strip()

    # Convert Polarity & Subjectivity to float
    df["Polarity"] = pd.to_numeric(df["Polarity"], errors="coerce")
    df["Subjectivity"] = pd.to_numeric(df["Subjectivity"], errors="coerce")

    # Handle NaN values
    df = df.dropna(subset=["Tweet"])
    df = df.fillna({"Polarity": 0.0, "Subjectivity": 0.0})

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Save if requested
    if save_cleaned:
        if output_path is None:
            output_path = csv_path
        df.to_csv(output_path, index=False)

    return df
