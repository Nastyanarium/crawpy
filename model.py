import unittest

class Attribute:
    def __init__(self, name: str, selector: str, attribute: str, many=False):
        self.name = name
        self.selector = selector
        self.attribute = attribute
        self.many = many

    def __str__(self):
        return f'Attribute(name={self.name}, selector={self.selector}, attribute={self.attribute}, many={self.many})'


class Extractor:
    def __init__(self, name: str, selector: str, attributes: list[Attribute]):
        self.name = name
        self.selector = selector
        self.attributes = attributes

    def __str__(self):
        attrstr = '\n'.join(str(i) for i in self.attributes)
        return f'Extractor(name={self.name}, selector={self.selector}, attributes={attrstr})'


class Queue:
    def __init__(self):
        self.queue = list()

    def add_element(self, val):
        self.queue.append(val)

    def size(self):
        return len(self.queue)

    def next(self):
        if self.size() > 0:
            return self.queue.pop(0)


class TestQueue(unittest.TestCase):
    def test_add(self):
        tqueue = Queue()
        tqueue.size()
        tqueue.add_element('poper')
        tqueue.add_element('mister')
        tqueue.add_element('plister')
        self.assertEqual(tqueue.queue, ['poper', 'mister', 'plister'])

    def test_remove(self):
        trqueue = Queue()
        trqueue.add_element(6)
        trqueue.add_element(9)
        trqueue.add_element(2)
        last = trqueue.next()
        print(trqueue.queue)
        self.assertEqual(trqueue.size(), 2)
        self.assertEqual(last, 6)



class Task:
    def __init__(self, name: str, url: str, extractors: list[Extractor]):
        self.name = name
        self.url = url
        self.extractors = extractors

    def printinfo(self):
        print(self.name, self.url)
        for e in self.extractors:
            print(e)



class TaskInstance:
    def __init__(self, url: str, taskname: str):
        self.url = url
        self.taskname = taskname

def tasl_from_json(json:str) -> Task:
    pass



