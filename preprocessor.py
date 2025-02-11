import pandas as pd

def load_data(file_path):
    """Load the CSV data into a DataFrame."""
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """Preprocess the DataFrame."""
    # Convert date columns to datetime
    df['first_funding_at'] = pd.to_datetime(df['first_funding_at'], errors='coerce')
    df['last_funding_at'] = pd.to_datetime(df['last_funding_at'], errors='coerce')
    
    # Extract year
    df['first_funding_year'] = df['first_funding_at'].dt.year
    df['last_funding_year'] = df['last_funding_at'].dt.year
    
    # Fill missing values
    df['market'] = df['market'].fillna("Unknown")
    
    # Determine funding type based on funding columns
    def determine_funding_type(row):
        if row['seed'] > 0:
            return 'Seed'
        elif row['angel'] > 0:
            return 'Angel'
        elif row['round_A'] > 0:
            return 'Round A'
        elif row['round_B'] > 0:
            return 'Round B'
        elif row['round_C'] > 0:
            return 'Round C'
        elif row['round_D'] > 0:
            return 'Round D'
        elif row['round_E'] > 0:
            return 'Round E'
        elif row['round_F'] > 0:
            return 'Round F'
        elif row['round_G'] > 0:
            return 'Round G'
        elif row['round_H'] > 0:
            return 'Round H'
        elif row['venture'] > 0:
            return 'Venture'
        elif row['debt_financing'] > 0:
            return 'Debt Financing'
        elif row['private_equity'] > 0:
            return 'Private Equity'
        elif row['grant'] > 0:
            return 'Grant'
        elif row['equity_crowdfunding'] > 0:
            return 'Equity Crowdfunding'
        elif row['convertible_note'] > 0:
            return 'Convertible Note'
        elif row['undisclosed'] > 0:
            return 'Undisclosed'
        else:
            return 'Unknown'

    df['funding_type'] = df.apply(determine_funding_type, axis=1)
    
    return df