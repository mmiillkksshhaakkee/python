from randomuser import RandomUser
import requests
import json
import pandas as pd

ru = RandomUser()
list_of_users = ru.generate_users(111)
print(f"list of users:\n{list_of_users[:15]}")

names = ru.get_full_name()
print(type(names))
print(f"names of users:\n{names}")

for user in list_of_users[:15]:
    print(user.get_full_name() + " " + user.get_email() + " " + user.get_picture())

def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_first_name(), "Gender":user.get_gender(), "DOB":user.get_dob(), "Photo":user.get_picture()})

    return pd.DataFrame(users)

df_ = pd.DataFrame(get_users())

new_ind = []
new_ind.extend('abcdefghjk')

df_.set_index([pd.Index(new_ind)], inplace=True)

############################
#obtaining an API from url
data_ab_fruits = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
# retrieving results
results = json.loads(data_ab_fruits.text)
# converting into pandas df, though this result will be in a nested json format, therefore we need to normalize it
df1_ = pd.DataFrame(results)
df2_ = pd.json_normalize(results)

print(df1_.iloc[0:10][1:5])
print(df2_.iloc[0:10][2:4])

cherry = df2_.loc[df2_["name"] == 'Cherry'] # choosing those rows whose 'name' is 'cherry'
print(type(cherry))
print((cherry.iloc[0]['family']), (cherry.iloc[0]['genus']))

cal_raspberry = df2_.loc[df2_["name"] == 'Raspberry']
print(cal_raspberry.iloc[0]['nutritions.calories'])
