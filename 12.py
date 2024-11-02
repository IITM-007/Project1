import pandas as pd

def calculate_following_difference(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Convert hireable to boolean if it's in string format
    if df['hireable'].dtype == 'object':
        df['hireable'] = df['hireable'].map({'True': True, 'False': False})
    
    # Calculate average following for hireable users
    hireable_avg = df[df['hireable']]['following'].mean()
    
    # Calculate average following for non-hireable users
    non_hireable_avg = df[~df['hireable']]['following'].mean()
    
    # Calculate the difference
    difference = hireable_avg - non_hireable_avg
    
    return round(difference, 3)

# Use the function
difference = calculate_following_difference('users.csv')
print(difference)