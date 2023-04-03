import yaml
import pytest
from tempfile import NamedTemporaryFile
#from remove_yaml_line import remove_yaml_line

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




@pytest.fixture
def yaml_file():
    # create a temporary YAML file for testing
    file = NamedTemporaryFile(mode='w', delete=False)
    file.write('section1:\n  - item1\n  # comment\n  - item2\nsection2:\n  - item3\n')
    file.close()
    yield file.name
    # delete the temporary file after the test is done
    import os
    os.remove(file.name)

def test_remove_line(yaml_file):
    # test removing a line from a YAML file
    remove_yaml_line(yaml_file, 'item2')
    with open(yaml_file, 'r') as f:
        assert f.read() == 'section1:\n  - item1\nsection2:\n  - item3\n'
        
def test_remove_line_with_comments(yaml_file):
    # test removing a line with comments from a YAML file
    remove_yaml_line(yaml_file, 'item1')
    with open(yaml_file, 'r') as f:
        assert f.read() == 'section1:\n  # comment\n  - item2\nsection2:\n  - item3\n'

def test_remove_line_in_section(yaml_file):
    # test removing a line in a specific section from a YAML file
    remove_yaml_line(yaml_file, 'item3', 'section2')
    with open(yaml_file, 'r') as f:
        assert f.read() == 'section1:\n  - item1\n  # comment\n  - item2\nsection2:\n'

def test_remove_line_not_found(yaml_file):
    # test removing a line that is not found in a YAML file
    remove_yaml_line(yaml_file, 'item4')
    with open(yaml_file, 'r') as f:
        assert f.read() == 'section1:\n  - item1\n  # comment\n  - item2\nsection2:\n  - item3\n'

def test_remove_line_in_nonexistent_section(yaml_file):
    # test removing a line in a nonexistent section from a YAML file
    remove_yaml_line(yaml_file, 'item2', 'section3')
    with open(yaml_file, 'r') as f:
        assert f.read() == 'section1:\n  - item1\n  # comment\n  - item2\nsection2:\n  - item3\n'
