import yaml

def remove_yaml_line(yaml_file, string_to_remove):
    with open(yaml_file, 'r') as f:
        data = f.read().split('\n')
    
    i = 0
    while i < len(data):
        if string_to_remove in data[i]:
            j = i - 1
            while j >= 0 and data[j].startswith('#'):
                j -= 1
            if j >= 0 and data[j].strip() == '':
                j -= 1
            if j >= 0 and data[j].startswith('- '):
                k = j - 1
                while k >= 0 and data[k].startswith('#'):
                    k -= 1
                if k >= 0 and data[k].strip() == '':
                    k -= 1
                data = data[:k+1] + data[j+1:i] + data[i+1:]
                i = k
            else:
                data = data[:j+1] + data[i+1:]
                i = j
        i += 1
    
    with open(yaml_file, 'w') as f:
        f.write('\n'.join(data))



def remove_yaml_line(yaml_file, string_to_remove):
    with open(yaml_file, 'r') as f:
        data = f.read().split('\n')
    
    i = 0
    while i < len(data):
        if string_to_remove in data[i]:
            j = i - 1
            while j >= 0 and data[j].startswith('#'):
                j -= 1
            if j >= 0 and data[j].strip() == '':
                j -= 1
            if j >= 0 and data[j].startswith('- '):
                k = j - 1
                while k >= 0 and data[k].startswith('#'):
                    k -= 1
                if k >= 0 and data[k].strip() == '':
                    k -= 1
                data = data[:k+1] + data[j+1:i] + data[i+1:]
                i = k
            else:
                data = data[:j+1] + data[i+1:]
                i = j
        i += 1
    
    with open(yaml_file, 'w') as f:
        f.write('\n'.join(data))
