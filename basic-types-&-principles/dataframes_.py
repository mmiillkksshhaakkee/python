import pandas as pd

#creating a dataframe from a dictionary

songs = {'album':['thriller', 'back in black', 'the dark side of the moon',\
                  'the bodyguard', 'bat out of hell'],
         'released': [1982,1980,1973,1992,1977],
         'length':['00:42:19','00:42:11','00:42:49','00:57:44','00:46:33']
         }
songs_frame = pd.DataFrame(songs)

print(songs_frame)

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
for i, num in enumerate(data):
    print(f'the index is {i}, number is {num}')

path = '/home/PycharmProjects/'
read_a = None
read_r = None

with open(path + 'textfile.txt', 'w+') as f:
    f.write(f"overwriting!\n")

with open(path + 'textfile.txt', 'a+') as f:
    f.write(f"appending and reading!\n")

with open(path + 'textfile.txt', 'r+') as f:
    f.seek(0,2)
    f.write(f"writing in r+ mode! at the end of f\n")
    f.seek(0)
    print(f'printing from r+ mode: from the beg of f \n' + f.read())

with open(path + 'textfile.txt', 'r+') as f:
    content = f.read() #now the offset is in the end
    f.write(f"writing to the end from r+ mode\n")
    f.seek(0)
    print(f'from here: ' + f.read())

with open(path + 'textfile.txt', 'rb') as f:
    f.seek(-20, 2)
    last_20_bytes = f.read()
    print(last_20_bytes.decode('utf-8'))