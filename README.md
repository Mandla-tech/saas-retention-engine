# SaaS Retention & Analytics Engine
### Built in WSL (Ubuntu) | Python (Pandas) | Cloud Trajectory

This is an automated data pipeline that transforms raw SaaS subscription data into actionable business health reports.

## Why this is Analyst Developer Approach:
- **Resilient Pipeline:** Includes a custom Data Audit function to detect "Hidden Text" and missing values.
- **Smart Cleaning:** Automatically handles the 'TotalCharges' string for numbers trap and normalizes the input.
- **Meaningful Analysis:** Identifies that **Month-to-Month** contracts represent a **42% churn risk** vs **2.8%** for Two-Year plans. This propels informative decision making.

## Technical Stack & Environment:
- **OS:** Ubuntu 22.04 (via Windows Subsystem for Linux - WSL)
- **Engine:** Python 3.x with Pandas
- **Infrastructure:** Dockerfile included for Cloud-Native deployment.

## Business Impact:
This tool provides a 360-degree view of **MRR**, **ARPU**, and **Churn Segmentation**, allowing SaaS leaders to prioritize retention strategies for high-risk segments.

## Data Source
- **Dataset:** [Telco Customer Churn (IBM)](https://www.kaggle.com)
- **Description:** This dataset contains 7,043 rows of subscription data, including demographic, account, and service information for a telecommunications company.
- **Context:** Used as a foundation to simulate real-world SaaS growth and retention analytics.
