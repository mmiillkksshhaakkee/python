
import numpy as np
import matplotlib.pyplot  as plt
import pandas as pd

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

dt = pd.DataFrame(x)

y = dt[['ID']]
z = dt['ID']

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
df = pd.read_csv(csv_path)

print(df.head())

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
df = pd.read_excel(xlsx_path)
print(df.head())

print(df.set_index(pd.Index(list('abcde')), inplace=True)) #returns None
print(df)

n = np.linspace(0, 2*np.pi,100)
l = np.sin(n)
plt.plot(n,l)
plt.show()

data = np.array([1, 2, 3, 4, 5])
std_dev = np.std(data)
print(std_dev) # Output: 1.4142135623730951

# Standard deviation along axis=0
data_2d = np.array([[1, 2, 3], [4, 5, 6]])
std_dev_axis0 = np.std(data_2d, axis=0)
print(std_dev_axis0) # Output: [1.5 1.5 1.5]

# Standard deviation along axis=1
std_dev_axis1 = np.std(data_2d, axis=1)
print(std_dev_axis1) # Output: [0.81649658 0.81649658]