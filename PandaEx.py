import pandas as pd


# Create a Pandas dataframe from the data.
df = pd.DataFrame({"SAEW02": [1,3,6,2,3,4,8], "SAEW03": [5,2,1,5,7,8,9]}, index=["12:00","13:00","14:00","15:00","16:00","17:00","18:00"])

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
col = 0
headers = df.dtypes.index
for i in range(len(df.columns)):
    col = i + 1
    chart.add_series({'name': headers[i], 'values': ['Sheet1', 1, col, 7, col]})

chart.set_x_axis({'name':'Date'})
chart.set_y_axis({'name':'Value'})

# Insert the chart into the worksheet.
worksheet.insert_chart('E2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
