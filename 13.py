import pandas as pd
from sklearn.linear_model import LinearRegression

def calculate_bio_word_followers_slope(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Filter out users without bios and handle NaN values
    df = df[df['bio'].notna() & (df['bio'] != '')]
    
    # Calculate word count by splitting on whitespace
    df['word_count'] = df['bio'].str.split().str.len()
    
    # Prepare data for regression
    X = df['word_count'].values.reshape(-1, 1)
    y = df['followers'].values
    
    # Create and fit the regression model
    model = LinearRegression()
    model.fit(X, y)
    
    return round(model.coef_[0], 3)

# Calculate and print the regression slope
slope = calculate_bio_word_followers_slope('users.csv')
print(slope)