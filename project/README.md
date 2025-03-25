# Network Traffic Anomaly Detection

## Video demo : https://youtu.be/C6Bn9T1_gHI

## 📌 Project Overview
This project analyzes network traffic data to detect anomalies using statistical methods. It employs **Rolling Window Smoothing**, **Standard Deviation Thresholding**, and **Interquartile Range (IQR) Analysis** to identify unusual patterns in the dataset. The detected anomalies are saved to a separate file for further analysis.

## 📂 Files in the Project
- **`all_data.csv`** - The dataset containing network traffic metrics.
- **`final_project.py`** - The main script that loads data, applies anomaly detection, and generates visualizations.
- **`Fixed_Anomalies.csv`** - The output file containing detected anomalies.
- **`test_final_project.py`** - Pytest-based test suite to validate the correctness of the anomaly detection process.

## 📊 Methodology
1. **Data Loading & Preprocessing**
   - Reads network traffic data from `all_data.csv`.
   - Applies a **rolling window (size=50)** to smooth incoming and outgoing traffic.

2. **Anomaly Detection Techniques**
   - **Standard Deviation Method**: Flags data points exceeding ±2 standard deviations from the mean.
   - **Interquartile Range (IQR) Method**: Identifies outliers using Q1 - 1.5*IQR and Q3 + 1.5*IQR thresholds.
   - Anomaly scores are calculated based on the number of flagged columns per row.

3. **Data Visualization**
   - Line plots of network traffic trends.
   - Scatter plots highlighting detected anomalies.
   - Threshold lines for upper and lower bounds.

4. **Output Generation**
   - Saves identified anomalies and their scores in `Fixed_Anomalies.csv`.

## 🛠️ Setup & Usage
### 1️⃣ Install Dependencies
Ensure you have the required libraries installed:
```bash
pip install pandas numpy matplotlib pytest
```

### 2️⃣ Run the Anomaly Detection Script
```bash
python final_project.py
```

### 3️⃣ View Results
- **Graphical Output**: The script generates a plot showing normal and anomalous data points.
- **CSV Output**: The detected anomalies are stored in `Fixed_Anomalies.csv`.

### 4️⃣ Run Tests
To validate the functionality, run:
```bash
pytest test_final_project.py
```

## ✅ Test Coverage
The `test_final_project.py` script ensures:
- Data is loaded properly.
- Rolling window transformation is applied.
- Anomalies are detected correctly.
- IQR-based filtering works.
- The output CSV is generated with the expected structure.

## 🚀 Future Improvements
- Implement real-time anomaly detection.
- Integrate machine learning models for advanced anomaly detection.
- Add timestamp indexing for better time-series analysis.

## 🏆 Conclusion
This project provides a structured approach to detecting anomalies in network traffic, making it a valuable tool for network security and monitoring. 🚀

