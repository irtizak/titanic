# Load libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
def run():
    titanic = pd.read_csv('../data/raw/titanic.csv')

    # Instantiate model
    model = RandomForestClassifier(random_state=42)

    # Create training dataset
    X = titanic.iloc[:,1:]
    sex = pd.get_dummies(X['Sex'])
    X.drop(['Name', 'Sex'], axis=1, inplace=True)
    X = pd.concat([X, sex], axis=1)
    X = X[['Pclass', 'Age']]
    y = titanic.iloc[:,0]
    print('Model features: {}'.format(list(X.columns)))

    # Fit model
    model.fit(X, y)
    print('Model trained.')

    # Save model
    joblib.dump(model, '../model/model.joblib')
    print('Model saved.')

if __name__ == '__main__':
    run()
