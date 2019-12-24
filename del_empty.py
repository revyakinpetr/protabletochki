import os
for file in os.listdir("data"):
    if file.endswith(".json"):
        with open('data/'+file, 'r') as f:
            content = f.readlines()
            if content == ['[]']:
                print('del', file)
                os.remove('data/'+file)