# Capstone Project 2  
## Predicting Diabetes Risk Through Lifestyle Factors Using Classification Models

### Overview

This project aims to predict the risk of developing diabetes based on various lifestyle factors, including physical activity, alcohol consumption, sleep patterns, BMI, hypertension, and age. Using a classification approach, the goal is to accurately categorize individuals into high-risk or low-risk groups for developing diabetes. The project leverages a series of machine learning models, with an emphasis on evaluating the performance of different classifiers to determine the most effective approach for this task.

### Research Question

**How can machine learning classification models predict the risk of developing diabetes based on lifestyle factors?**

### Objectives

- To predict diabetes risk based on lifestyle factors and categorize individuals into high-risk or low-risk groups.
- To compare the performance of different classification models to identify the most effective algorithm.
- To analyze which lifestyle factors are most significant in predicting diabetes risk.

### Data Requirements

#### Lifestyle Factors

- Physical activity (active vs. inactive)
- Alcohol consumption (yes vs. no)
- Sleep disorder (yes vs. no)
- BMI (normal vs. obese)
- Hypertension (yes vs. no)
- High cholesterol (yes vs. no)
- Age (in years)
- Gender (female vs. male)

#### Data Sources

- [Synthetic Diabetes 2 Type Prediction Dataset](https://www.kaggle.com/datasets/nigoraxonnasimova/synthetic-diabetes-2-type-prediction-dataset)
- [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

*The datasets have been merged, focusing on lifestyle-related indicators to predict diabetes risk.*

### Methodology

1. **Problem Definition**  
   **Objective**: To classify individuals into high-risk or low-risk categories for diabetes based on lifestyle factors.

2. **Data Preprocessing**  
   - Clean and preprocess the data, handling missing values, encoding categorical features, and scaling numeric features where necessary.
   - Merge datasets, ensuring consistency across features.

3. **Modeling**  
   The following classification models are used in this project:
   - Logistic Regression
   - K-Nearest Neighbors (KNN)
   - Decision Tree Classifier
   - Support Vector Classifier (SVC)
   - Random Forest Classifier
   - Gradient Boosting Classifier
   - AdaBoost Classifier
   - XGBoost Classifier

   These models will be trained on the data and evaluated for their classification performance. For each model, hyperparameters will be tuned using GridSearchCV with 5-fold cross-validation and the F1 score as the evaluation metric.

4. **Model Evaluation**  
   - **Classification Task**: Classify individuals as either low-risk or high-risk for diabetes.
   - **Metrics**: Evaluate using accuracy, precision, recall, F1 score, AUC-ROC, and confusion matrices.
   - **Comparison**: Compare the models’ performance based on the metrics and analyze which model performs best for this classification task.

5. **Feature Importance**  
   Use models like Random Forest and XGBoost to assess feature importance and identify the key lifestyle factors that predict diabetes risk.

### Tools and Libraries

- Python
- scikit-learn for machine learning models and evaluation
- XGBoost for gradient boosting
- pandas for data preprocessing
- matplotlib and seaborn for data visualization

### Expected Results

1. **Accurate Classification**: The machine learning models will provide a reliable classification of individuals into high-risk or low-risk categories for developing diabetes.
2. **Key Insights**: Identify the lifestyle factors that most influence diabetes risk.
3. **Public Health Applications**: Provide insights that can be used for public health interventions, wellness programs, and insurance risk modeling.

### Conclusion

This project demonstrates the use of various classification algorithms to predict the risk of diabetes based on lifestyle factors. By evaluating multiple models, the project will determine which classifier provides the best performance for predicting diabetes risk. This will allow for more effective targeting of individuals at higher risk and offer insights into the lifestyle factors contributing to diabetes.

### Getting Started

1. Clone the repository to your local machine.
2. Install dependencies by running:
   ```bash
   pip install -r requirements.txt

## Acknowledgments

- Mekonen - Project lead
- Viviana Marquez - Learning facilitator 

