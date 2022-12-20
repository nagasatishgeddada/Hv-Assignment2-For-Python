import pandas as pd
data_series1 = pd.Series([6,7,8,9,10])
data_series2 = pd.Series([1,2,3,4,5])
Total_data_series = data_series1 + data_series2
print("Add two data series : ")
print(Total_data_series)

Total_data_series = data_series1 - data_series2
print("Subtract two data series : ")
print(Total_data_series)

Total_data_series = data_series1 * data_series2
print("Multiply two data series : ")
print(Total_data_series)

Total_data_series = data_series1 / data_series2
print("Divde two data series : ")
print(Total_data_series)

Total_data_series = data_series1 %  data_series2
print("Percentage/Modulo two data series : ")
print(Total_data_series)