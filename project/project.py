import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_csv(n):
    return pd.read_csv(n)

def smooth(df,column,n):
    return df[column].rolling(window=n).mean()

def lbound(n,m):
    return n - 1.5 * m

def ubound(n,m):
    return n + 1.5 * m

def main():
    df = load_csv("all_data.csv")

    #Creates a rolling window for a smoother plotting instead of messy lines
    df['in_smooth'] = smooth(df,'ifInOctets11',50)
    df['out_smooth'] = smooth(df,'ifOutOctets11',50)

    #Mean and Standard Deviation calculation for ifInOctets11
    mean_in = df['in_smooth'].mean()
    std_in = df['in_smooth'].std()

    #Mean and Standard Deviation calculation for ifOutOctets11
    mean_out = df['out_smooth'].mean()
    std_out = df['out_smooth'].std()

    #Anything above or below than the Upper or Lower bound respectively is detected through the formula mean +/- 2 * std for both
    df['anamoly_in'] = (df['in_smooth'] > mean_in + 2 * std_in) | (df['in_smooth'] < mean_in - 2 * std_in)
    df['anamoly_out'] = (df['out_smooth'] > mean_out + 2 * std_out) | (df['out_smooth'] < mean_out - 2 * std_out)

    #Plotting the whole data and marking with "X" anything that goes above or below the bounds
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['in_smooth'], label="Incoming Smooth")
    plt.plot(df.index, df['out_smooth'], label="Outgoing Smooth")
    plt.plot(df.index, df['tcpOutRsts'], label="Tcp Out Resets")
    plt.axhline(mean_in + 2 * std_in, color='r', linestyle='dashed',label='Incoming Upper Threshhold')
    plt.axhline(mean_in - 2 * std_in, color='r', linestyle='dotted', label="Incoming Lower Threshold")
    plt.axhline(mean_out + 2 * std_out, color='b', linestyle='dashed',label='Outgoing Upper Threshhold')
    plt.scatter(df.index[df['anamoly_in']], df['in_smooth'][df['anamoly_in']], color="red", label="Incoming Anamolies", s=100, marker="x")
    plt.scatter(df.index[df['anamoly_out']],df['out_smooth'][df['anamoly_out']], color="red", label="Outgoing Anamolies", s=100, marker="x")
    plt.xlabel("Time")
    plt.ylabel("Bytes")
    plt.title("Fluctiations In Data")
    plt.grid(True)
    plt.legend()
    plt.show()

    #Anomalies detection through IQR method
    Q1 = df.select_dtypes(include=[np.number]).quantile(0.25)
    Q3 = df.select_dtypes(include=[np.number]).quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = lbound(Q1, IQR)
    upper_bound = ubound(Q3,IQR)

    #Flagging the anomalies
    anomaly_flags =  df.select_dtypes(include=[np.number]).apply(lambda x: (x > upper_bound[x.name]) | (x < lower_bound[x.name]), axis=0)

    #Looping through each numeric columna and assiginig anomaly flags
    for col in anomaly_flags.columns:
        df[f"{col}_anomaly"] = anomaly_flags[col]
    #Printing the sum of sum of all columns
    print(anomaly_flags.sum().sum())

    #Assiging a variable that only takes "_anomaly" values and print them to a csv file with a score column that tells how many anomalies each row has
    anomalies_only = df[df.filter(like="_anomaly").any(axis=1)]
    anomalies_only['anomalies_score'] = anomalies_only.filter(like='_anomaly').sum(axis=1)
    anomalies_only = anomalies_only.sort_values(by='anomalies_score', ascending=False)# As it should be based on severity so, Descending order
    anomalies_only.to_csv("Fixed_Anomalies.csv", index=False)

    #Confirms anomalies detection completed and CSV export
    print("✅ Fixed anomalies saved successfully!")

    #Reading the newly created csv file that has values from previous data and anomalies detected and its score too in each column
    df_fixed_anomalies = pd.read_csv("Fixed_Anomalies.csv")
    print(df_fixed_anomalies['anomalies_score'])

if __name__ == "__main__":
    main()