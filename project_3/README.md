# Investigating Lifestyle Factors and Diabetes Prevalence

## Overview

This project aims to investigate the relationship between common lifestyle factors—such as diet, physical activity, sleep patterns, and stress levels—and the prevalence of major lifestyle diseases, specifically diabetes. By understanding these relationships, the project seeks to provide insights into effective public health interventions and lifestyle modifications that may reduce the risk of developing diabetes.

## Research Question

**How do common lifestyle factors influence the prevalence of diabetes in different demographics?**

## Objectives

- Analyze how different lifestyle factors correlate with diabetes prevalence.
- Identify patterns and trends that may indicate higher risks.
- Suggest actionable recommendations for individuals and public health initiatives.

## Data Requirements

### Lifestyle Factors

- Daily fruit consumption
- Physical activity
- Sleep patterns (e.g., average hours of sleep per night)
- Alcohol consumption
- Smoking

### Data Sources

- [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
- [Synthetic Diabetes 2 Type Prediction Dataset](https://www.kaggle.com/datasets/nigoraxonnasimova/synthetic-diabetes-2-type-prediction-dataset)

*I am merging the above two datasets, focusing only on features with lifestyle indicators.*

## Methodology

1. **Problem Definition**  
   **Objective**: Predict the risk of developing diabetes based on various lifestyle factors and classify individuals into risk categories (e.g., low, moderate, high).

2. **Data Collection and Preprocessing**  
   - Clean and preprocess data (handling missing values, outliers).
   - Engineer features that will be used in modeling.

3. **Regression Model**  
   **Modeling**: Using regression techniques to predict the risk score.  
   **Risk Score Calculation**: This will provide a numerical value indicating the likelihood of developing diabetes based on the features.

4. **Classification Model**  
   **Thresholding**: Define thresholds for the risk score to categorize individuals:  
   - Low Risk: Score < X  
   - Moderate Risk: Score between X and Y  
   - High Risk: Score > Y  
   **Modeling**: Use classification techniques (e.g., decision trees) to assign individuals to these risk categories based on their risk scores.

5. **Evaluation**  
   **Regression Evaluation**: Use metrics like RMSE or R² to evaluate the regression model’s performance.  
   **Classification Evaluation**: Use accuracy, precision, recall, F1 score, and AUC-ROC to evaluate the classification model's performance.  
   **Comparison**: Compare the performance of logistic regression and decision trees to identify which model provides better insights and predictions.

## Tools and Libraries

- Python
- scikit-learn for modeling
- pandas for data manipulation
- matplotlib and seaborn for visualization

## Expected Outcomes

- Identification of key lifestyle factors significantly associated with diabetes.
- Recommendations for public health interventions aimed at promoting healthier lifestyle choices.

## Conclusion

This hybrid approach leverages the strengths of both logistic regression and decision trees, providing both a nuanced risk score and clear categorizations. By comparing the two models, you can gain deeper insights into the relationships between lifestyle factors and diabetes risk.

## Getting Started

1. Clone the repository to your local machine.
2. Install any necessary dependencies (see requirements.txt for details).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Mekonen - Project lead
- Viviana Marquez - Learning facilitator 



