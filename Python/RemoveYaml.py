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
        
        
        
        
import datetime

def delete_entry(env, spec_yaml, entry):
    env_key = env + ":"
    with open(spec_yaml, 'r') as input_file:
        input_lines = input_file.readlines()

    with open(spec_yaml, 'w') as output_file:
        env_found = False
        match_found = False
        for line in input_lines:
            line = line.lstrip()
            if not line.startswith(env_key) and not env_found:
                output_file.write(line)
            else:
                env_found = True
                if match_found or not line.startswith("- " + entry):
                    output_file.write(line)
                else:
                    match_found = True
                    output_file.write("# " + line.rstrip() + "  # Disabled by automation on " + str(datetime.datetime.now()) + "\n")

    if not match_found:
        print("Entry '{}' not found for environment '{}' in '{}'.".format(entry, env, spec_yaml))
        
        
import os
import pytest
import datetime
from delete_entry import delete_entry

@pytest.fixture
def spec_file(tmp_path):
    data = {'env1:': ['entry1', 'entry2'],
            'env2:': ['entry3', 'entry4']}
    file_path = tmp_path / 'spec.yml'
    with open(file_path, 'w') as f:
        for env, entries in data.items():
            f.write(env + '\n')
            for entry in entries:
                f.write('- ' + entry + '\n')
    return file_path

def test_delete_entry_success(spec_file):
    env = 'env1'
    entry = 'entry1'
    delete_entry(env, str(spec_file), entry)
    with open(spec_file, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
        assert '- ' + entry not in data

def test_delete_entry_not_found(spec_file):
    env = 'env1'
    entry = 'entry3'
    with pytest.raises(SystemExit):
        delete_entry(env, str(spec_file), entry)

def test_delete_entry_commented_out(spec_file):
    env = 'env1'
    entry = 'entry1'
    delete_entry(env, str(spec_file), entry)
    with open(spec_file, 'r') as f:
        for line in f:
            if line.startswith("# - " + entry):
                assert str(datetime.datetime.now().year) in line
                assert str(datetime.datetime.now().month) in line
                assert str(datetime.datetime.now().day) in line
                
                
   import yaml

def comment_out_entry(yml_file, section, entry):
    # Load the YAML file
    with open(yml_file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # Find the specified section and entry
    if section in data and entry in data[section]:
        # Comment out the entry by adding a '#' character to the beginning of the line
        data[section][entry] = '#' + str(data[section][entry])

    # Write the updated data back to the YAML file
    with open(yml_file, 'w') as f:
        yaml.dump(data, f)

  comment_out_entry('example.yml', 'database', 'password')

