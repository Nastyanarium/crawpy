from model import Queue, TaskInstance
from out import *
from parser import *
from requester import *
import utils
import sys

def process_task(elem, tasks, outputs, flow, requester, parser, queue):
    html_text = requester.request(elem.url)
    
    task = tasks[elem.taskname]
    data = parser.extract(task, html_text)

    out = Out(outputs[task.name])
    out.write(data)

    child_tasks = flow.get(task.name, [])
    print('get child task', child_tasks)

    for one in data:
        for child in child_tasks:
            url = requester.template(tasks[child].url, one)
            print(url)
            task_instance = TaskInstance(url, child)
            queue.add_element(task_instance)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Insert file name')
        sys.exit()

    data = utils.read_flow_from_file(sys.argv[1])
    flow, tasks, outputs, first_tasks = utils.read_flow(data)

    queue = Queue()

    for taskname in first_tasks:
        task = tasks[taskname]
        task_instance = TaskInstance(task.url, task.name)
        queue.add_element(task_instance)

    requester = Requester()
    parser = Parser()

    while queue.size():
        elem = queue.next()
        try:
            process_task(elem, tasks, outputs, flow, requester, parser, queue)
        except Exception as e:
            print(f"Error processing task {elem.taskname}: {e}")
