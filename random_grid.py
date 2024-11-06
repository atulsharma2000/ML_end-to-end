import numpy as np
from sklearn.datasets import load_iris, load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Load datasets
iris = load_iris()
X_class, y_class = iris.data, iris.target

boston = load_boston()
X_reg, y_reg = boston.data, boston.target

# Split datasets into training and testing sets
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.2, random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Define hyperparameters for classification
param_grid_class = {
    'logistic_regression': {
        'model': LogisticRegression(),
        'params': {
            'C': [0.01, 0.1, 1, 10],
            'penalty': ['l2'],
            'solver': ['liblinear']
        }
    },
    'decision_tree': {
        'model': DecisionTreeClassifier(),
        'params': {
            'max_depth': [None, 5, 10],
            'min_samples_split': [2, 5]
        }
    },
    'random_forest': {
        'model': RandomForestClassifier(),
        'params': {
            'n_estimators': [10, 50],
            'max_features': ['auto', 'sqrt'],
            'min_samples_split': [2, 5]
        }
    },
    'svm': {
        'model': SVC(),
        'params': {
            'C': [0.1, 1, 10],
            'kernel': ['linear', 'rbf'],
            'gamma': ['scale', 'auto']
        }
    }
}

# Hyperparameter tuning for classification
for model_name in param_grid_class:
    model = param_grid_class[model_name]['model']
    params = param_grid_class[model_name]['params']
    
    grid_search = GridSearchCV(model, params, cv=5)
    grid_search.fit(X_train_class, y_train_class)
    
    print(f"{model_name} best parameters: {grid_search.best_params_}")

# Define hyperparameters for regression
param_grid_reg = {
    'ridge': {
        'model': Ridge(),
        'params': {
            'alpha': [0.1, 1.0, 10.0]
        }
    },
    'decision_tree_regressor': {
        'model': DecisionTreeRegressor(),
        'params': {
            'max_depth': [None, 5, 10],
            'min_samples_split': [2, 5]
        }
    },
    'random_forest_regressor': {
        'model': RandomForestRegressor(),
        'params': {
            'n_estimators': [10, 50],
            'max_features': ['auto', 'sqrt'],
            'min_samples_split': [2, 5]
        }
    }
}

# Hyperparameter tuning for regression
for model_name in param_grid_reg:
    model = param_grid_reg[model_name]['model']
    params = param_grid_reg[model_name]['params']
    
    grid_search = GridSearchCV(model, params, cv=5)
    grid_search.fit(X_train_reg, y_train_reg)
    
    print(f"{model_name} best parameters: {grid_search.best_params_}")