def get_file():
    file = open('lemoncake206.github.io/writing_storage.txt', 'r')
    line = file.readline().strip()
    lines = []
    count = 0

    while line != '':
        if count % 2 == 0:
            lines.append(line)
        else:
            lines.append(int(line))
        count += 1
        line = file.readline().strip()
    file.close()
    return lines
        
def rewrite_file(lines):
    file = open('lemoncake206.github.io/writing_storage.txt', 'w')
    for line in lines:
        file.write(str(line))
        file.write('\n')
    file.close()
    
    
def add_value(name: str, amount: int):
    lines = get_file()
    for x in range(len(lines)):
        if lines[x] == name:
            lines[x+1] += amount
    rewrite_file(lines)
            

def subtract_value(name: str, amount: int):
    lines = get_file()
    for x in range(len(lines)):
        if lines[x] == name:
            lines[x+1] -= amount
    rewrite_file(lines)
