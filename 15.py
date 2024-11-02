import pandas as pd

def calculate_email_sharing_difference(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Convert hireable to boolean if it's in string format
    if df['hireable'].dtype == 'object':
        df['hireable'] = df['hireable'].map({'True': True, 'False': False})
    
    # Count users with email for each group
    hireable_users = df[df['hireable']]
    non_hireable_users = df[~df['hireable']]
    
    # Calculate fractions
    hireable_email_fraction = (hireable_users['email'].notna().sum() / len(hireable_users)) if len(hireable_users) > 0 else 0
    non_hireable_email_fraction = (non_hireable_users['email'].notna().sum() / len(non_hireable_users)) if len(non_hireable_users) > 0 else 0
    
    # Calculate difference
    difference = hireable_email_fraction - non_hireable_email_fraction
    
    return round(difference, 3)

# Calculate and print the difference
difference = calculate_email_sharing_difference('users.csv')
print(difference)