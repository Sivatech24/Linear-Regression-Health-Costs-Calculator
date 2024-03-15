# Load the dataset
data = pd.read_csv('insurance.csv')

# Preprocessing
# Convert categorical data to numerical format using one-hot encoding or label encoding
# Handle missing values if any
# Split the data into features (X) and labels (y)
X = data.drop(columns=['expenses'])
y = data['expenses']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
