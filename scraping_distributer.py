import pandas as pd
import subprocess
import os
from pathlib import Path

# read DataFrame
data = pd.read_csv("params_02_01.csv")
data = data.drop(data.columns[0], axis=1)
# no of csv files with row size
number_of_file = 3
length = int(len(data) / number_of_file)
print("1. EACH MAHCINE HAS",length, "REQUESTS.")
for i in range(number_of_file):
    df = data[length * i:length * (i + 1)]
    df.to_csv(f'Params{i + 1}.csv', index=False)

data = pd.read_csv("Params1.csv")
data2 = pd.read_csv("Params2.csv")
data3 = pd.read_csv("Params3.csv")
data.to_csv("Params1_IN.csv", index=True)
data2.to_csv("Params2_IN.csv", index=True)
data3.to_csv("Params3_IN.csv", index=True)

Path("Params1_IN.csv").rename("./machine1/params.csv")
Path("Params2_IN.csv").rename("./machine2/params.csv")
Path("Params3_IN.csv").rename("./machine3/params.csv")
print("2. TASKS HAVE BEEN DISTRIBUTED TO 3 MACHINES")
print("3. MACHINES ARE RUNNING")
subprocess.call("./start_docker.sh", shell=True)
