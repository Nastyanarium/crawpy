import json
import yaml
from model import *

def read_task(filename):
    with open(filename) as file:
        data = json.load(file)
        return read_from_object(data)

def read_flow_from_file(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
        return data

def read_yaml(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
        return read_from_object(data)

def read_from_object(data):
    extractors = []
    for e in data['extractors']:
        attributes = []
        for a in e['attributes']:
            attribute = Attribute(a['name'], a.get('selector', ''), a.get('attribute', ''), a.get('many', False))
            attributes.append(attribute)

        extractor = Extractor(e['name'], e['selector'], attributes)
        extractors.append(extractor)

    return Task(data['name'], data['url'], extractors)

def read_flow(flows):
    flow = {}
    tasks = {}
    outputs = {}
    first_tasks = []

    def inner(data: dict):
        childs = data.get('childs', [])
        task = read_yaml(data['task'])
        tasks.update({task.name: task})
        outputs.update({task.name: data['output']})
    
        for child in childs:
            child_task = read_yaml(child['task'])
            
            # Если несколько дочерних задач, сохраняем их в список
            if task.name not in flow:
                flow[task.name] = []
            flow[task.name].append(child_task.name)

            inner(child)

    for f in flows['flows']:
        task = read_yaml(f['task'])
        first_tasks.append(task.name)
        inner(f)

    return flow, tasks, outputs, first_tasks


def write_page(filename, text):
    with open(filename, 'w') as f:
        f.write(text)


