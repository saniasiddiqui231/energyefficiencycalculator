import csv

data = [
    ["Wind speed m/s", "output(kW)"],
    ["0", "-"],
    ["3", "22"],
    ["4", "85"],
    ["5", "110"],
    ["6",  "350"],
    ["7", "600"],
    ["8",  "900"],
    ["9", "1274"],
    ["10", "1533"],
    ["11", "1863"],
    ["12", "1960"],
    ["13", "1990"],
    ["14", "1998"],
    ["15", "2000"],
    ["16", "2000"],
    ["17", "2000"],
    ["18", "2000"],
    ["19", "2000"],
    ["20", "2000"],
    
]


file_name = "wind_turbine.csv"


with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    
    writer.writerows(data)