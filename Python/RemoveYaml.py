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


remove_yaml_line('example.yml', 'string_to_remove')



def remove_yaml_line(yaml_file, string_to_remove, section=None):
    with open(yaml_file, 'r') as f:
        data = f.readlines()
    
    indexes_to_remove = []
    section_found = not section
    for i, line in enumerate(data):
        if line.strip().startswith(section):
            section_found = True
        elif section_found and string_to_remove in line:
            j = i - 1
            while j >= 0 and (data[j].startswith('#') or not data[j].strip()):
                j -= 1
            if j >= 0 and data[j].startswith('-'):
                k = j - 1
                while k >= 0 and (data[k].startswith('#') or not data[k].strip()):
                    k -= 1
                indexes_to_remove.extend(range(k+1, i+1))
            else:
                indexes_to_remove.extend(range(j+1, i+1))
    
    new_data = [line for i, line in enumerate(data) if i not in indexes_to_remove]
    
    with open(yaml_file, 'w') as f:
        f.writelines(new_data)

remove_yaml_line('example.yml', 'string_to_remove', 'section_name')
