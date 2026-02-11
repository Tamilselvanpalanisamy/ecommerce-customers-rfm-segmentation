import pandas as pd

#Loading the dataset
df=pd.read_csv(r'C:\Users\Tamil\OneDrive\Desktop\E-commerce RFM data analysis\Data\ecommerce_transactions_rfm.csv')

############################################ DATA CLEANING ##################################################

#Formatting the date column
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])

#Dropping the rows with missing values in the 'CustomerID' column
df=df.dropna(subset = ['CustomerID'])

#Removing the rows with negative or zero values in the 'Quantity' and 'UnitPrice' columns
df=df[df['Quantity']>0]

#Removing the rows with negative or zero values in the 'UnitPrice' column
df=df[df['UnitPrice']>0]

#Creating a new column 'TotalAmount' by multiplying the 'Quantity' and 'UnitPrice' columns
df['TotalAmount']=df['Quantity']*df['UnitPrice']

######################################################## RFM CALCULATIONS ##################################################

#Calculating the reference date for recency calculation as one day after the last transaction date in the dataset
last_transaction_date=df['InvoiceDate'].max()
reference_date = last_transaction_date + pd.Timedelta(days=1)

 #Calculating recency   
customer_last_purchase = (
    df.groupby('CustomerID')['InvoiceDate']
    .max()
    .reset_index()
)
customer_last_purchase['Recency'] = (
    reference_date - customer_last_purchase['InvoiceDate']
).dt.days

recency_df = customer_last_purchase[['CustomerID', 'Recency']]

#Calculating frequency
customer_frequency = (
    df.groupby('CustomerID')['InvoiceNo']
    .nunique()
    .reset_index(name='Frequency')
)

freq_df = customer_frequency[['CustomerID', 'Frequency']]

#Calculating monetary value
customer_monetory = (
    df.groupby('CustomerID')['TotalAmount']
    .sum()
    .reset_index(name='Monetary')   
)
monetory_df = customer_monetory[['CustomerID', 'Monetary']]

#Combining recency anf frequency dataframes
rf_df = pd.merge(
    recency_df,
    freq_df,
    on='CustomerID',
    how='inner'
)

#combining monetory dataframe with the recency and frequency dataframe to create the final RFM dataframe
rfm_df = pd.merge(
    rf_df,
    monetory_df,
    on='CustomerID',
    how='inner'
)


#Assigning R, F, and M scores based on quintiles
rfm_df["R_score"]=pd.qcut(rfm_df['Recency'],q=5,labels=[5,4,3,2,1])
rfm_df["F_score"]=pd.qcut(rfm_df['Frequency'],q=5,labels=[1,2,3,4,5])
rfm_df["M_score"]=pd.qcut(rfm_df['Monetary'],q=5,labels=[1,2,3,4,5])

#Converting R, F, and M scores to integers and creating a combined RFM score
rfm_df [['R_score','F_score','M_score']]=rfm_df[['R_score','F_score','M_score']].astype(int)
rfm_df['RFM_Score']=rfm_df['R_score'].astype(str)+rfm_df['F_score'].astype(str)+rfm_df['M_score'].astype(str)

#Defining a function to segment customers based on their R, F, and M scores
def rfm_segment(row):
    if row['R_score'] >= 4 and row['F_score'] >= 4 and row['M_score'] >= 4:
        return 'Champions'
    elif row['F_score'] >= 4 and row['M_score'] >= 3:
        return 'Loyal Customers'
    elif row['R_score'] == 5 and row['F_score'] <= 2:
        return 'New Customers'
    elif row['R_score'] <= 2 and row['F_score'] >= 3 and row['M_score'] >= 3:
        return 'At Risk'
    elif row['R_score'] == 1 and row['F_score'] == 1 and row['M_score'] == 1:
        return 'Lost Customers'
    else:
        return 'Need Attention'

rfm_df['Customer_Segment'] = rfm_df.apply(rfm_segment, axis=1)

#Saving the final RFM dataframe to a new CSV file
rfm_df.to_csv(r'C:\Users\Tamil\OneDrive\Desktop\E-commerce RFM data analysis\Output\rfm_analysis_results.csv', index=False)
