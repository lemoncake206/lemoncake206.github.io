file = open('writing_storage.txt','r')
current = file.readlines().strip()
for x in current:
    print(x)

def add_value(name: str, amount: int):
    if name == 'Kate':
        x = 0
    