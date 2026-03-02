print("Script Started...")
import pandas as pd
import sys

def clean_data(df):
    print("---Starting the Data Cleaning & Audit---")

    #Standardizing column names to lowercase, and striping whitespace
    df.columns = df.columns.str.lower().str.strip()

    #Checking for duplicates using primary key Customer ID
    duplicate_count = df['customerid'].duplicated().sum()
    if duplicate_count > 0:
        print(f"Found {duplicate_count} Duplicate Customer IDs. Removing duplicates")
        df = df.drop_duplicates(subset=['customerid'], keep='last')

    #Cleaning TotalCharges, set all entry as numbers
    #coerce turns empty space into NaN
    df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')

    #Handling missing values
    null_count = df['totalcharges'].isnull().sum()
    if null_count > 0:
        print(f"Handling {null_count} missing values in TotalCharges")
        df['totalcharges'] = df['totalcharges'].fillna(0)

    #Trim whitespace from all text columns
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    print("Data Cleaning Complete.\n")
    return df

def calculate_metrics(df):
    total_customers = len(df)

    # Calculating global Churn rate
    churned_customers = len(df[df['churn'] == 'Yes'])
    churn_rate = (churned_customers / total_customers) * 100

    # Calculating Revenue (Simulating an MRR column if not present)
    total_mrr = df['monthlycharges'].sum()

    #Calculating arpu (Average Revenue Per User)
    arpu = total_mrr/total_customers

    print(f"--- SaaS Business Health Report ---")
    print(f"Total Customers: {total_customers}")
    print(f"Churn Rate: {churn_rate:.2f}%")
    print(f"Monthly Recurring Revenue (MRR): ${total_mrr:,.2f}")
    print(f"Average Revenue Per User (ARPU): ${arpu:.2f}")

    #Churning by contract type (I logically make 1= churn and 0=stay)
    df['churn_bool'] = df['churn'].apply(lambda x: 1 if x == 'Yes' else 0)

    #Grouping by contract typpe for average churn percentage
    contract_stat = df.groupby('contract')['churn_bool'].mean() * 100

    print("\n --Churn by contract type---")
    print(contract_stat.map("{:.2f}%".format))

    #High churn risk monitor
    high_risk = contract_stat.idxmax()
    print(f"\n Alert: High churn risk detected {high_risk} contracts")
    
    return {"churn_rate": churn_rate, "mrr": total_mrr}

if __name__ == "__main__":
    file_name = 'your_data.csv'

    try:
        # Loading the data
        raw_df = pd.read_csv('your_data.csv') 

        #Loading cleaned dataset
        cleaned_df = clean_data(raw_df)

        #Analyzing and show results
        calculate_metrics(cleaned_df)

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please check the file path.")
    
    except Exception as e:
         print(f"An unexpected error occurred: {e}")
