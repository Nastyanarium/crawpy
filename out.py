import json


class Out:
    def __init__(self, filename):
        self.filename = filename

    def write(self, outs):
        with open(self.filename, 'a') as output:
            for o in outs:
                string = json.dumps(o) + "\n"
                output.write(string)
            print(f'Wrote {len(outs)} object(s)')