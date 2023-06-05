import sys
import json

def main(tests, values):
    return fill_dict(tests, values)

def fill_dict(tests, values):
    id = tests['id']
    value = [v for v in values['values'] if v['id'] == id][0]
    tests['value'] = value['value']
    filled_tests = {'id': id, 'title':tests['title'], 'value': tests['value']}
    if 'values' in list(tests.keys()):
        filled_tests['values'] = []
        for test_inner in tests['values']:
            filled_tests['values'].append(fill_dict(test_inner, values))
    return filled_tests

if __name__ == "__main__":
    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])
    file3 = "report.json"
    with open(file1, 'r') as f:
        tests = json.loads(" ".join(f.readlines()))
    with open(file2, 'r') as f:
        values = json.loads(" ".join(f.readlines()))
    filled = main(tests, values)
    with open(file3, 'w+') as f:
        f.write(json.dumps(filled))