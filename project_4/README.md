 # Predicting Term Deposit Subscriptions

## Overview

This project aims to predict whether a client of a Portuguese banking institution will subscribe to a term deposit based on various customer features. The goal is to build a predictive model to assist the bank in targeting the right clients for future marketing campaigns. The project focuses on using different machine learning models to classify clients as likely to subscribe or not, using data such as personal details, bank account information, and past campaign history.

## Research Question

**Can we predict whether a client will subscribe to a term deposit based on their demographic and interaction data?**

## Objectives

- Analyze customer data to understand which features influence term deposit subscription.
- Build machine learning models to predict client subscription behavior.
- Evaluate model performance using appropriate metrics to ensure accurate and reliable predictions.
- Provide actionable insights for targeted marketing campaigns.

### Data Sources

- [Bank Marketing Dataset](https://www.kaggle.com/datasets/uciml/bank-marketing)

*The dataset includes customer data collected through direct marketing campaigns and aims to predict client subscription to a term deposit.*

## Methodology

1. **Problem Definition**  
   **Objective**: Predict whether a client will subscribe to a term deposit (binary classification: subscribe = 1, not subscribe = 0).

2. **Data Preprocessing**  
   - Handle missing values, outliers, and invalid categorical values.
   - Convert categorical features (such as marital status and education) to numerical formats using one-hot encoding or other encoding techniques.
   - Normalize numerical features where appropriate.

3. **Feature Engineering**  
   - Create derived features such as `month_sin` and `month_cos` to represent the cyclical nature of months.
   - Analyze correlations between features and the target variable to identify key predictors.

4. **Modeling**  
   **Classification Models**: Use a variety of models including Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Classifier (SVC), and Decision Trees to predict the target variable.  
   **Hyperparameter Tuning**: Perform hyperparameter tuning using GridSearchCV to optimize each model's performance based on relevant metrics.

5. **Evaluation**  
   **Model Evaluation**: Assess model performance using metrics such as accuracy, precision, recall, F1 score, and ROC AUC.  
   **Cross-validation**: Use 5-fold cross-validation to ensure reliable and generalizable model performance.

6. **Imbalance Handling**  
   Address the class imbalance issue, as the number of clients subscribing to the term deposit is smaller compared to those who do not subscribe. Techniques like resampling, adjusting class weights, and using Precision-Recall AUC can be explored.

## Tools and Libraries

- Python
- scikit-learn for machine learning models
- pandas for data manipulation
- matplotlib and seaborn for data visualization
- numpy for numerical operations

## Expected Outcomes

- Identification of key features influencing term deposit subscription.
- Accurate predictions of client subscription behavior based on demographic and interaction data.
- Actionable insights to guide targeted marketing campaigns and improve client engagement.

## Conclusion

This project leverages a range of machine learning models to predict whether a client will subscribe to a term deposit. By comparing different models, evaluating performance metrics, and addressing class imbalance, the project aims to provide reliable predictions that can help the bank optimize its marketing efforts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Mekonen - Project lead
- Viviana Marquez - Learning facilitator 

