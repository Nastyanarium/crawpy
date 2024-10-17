import lxml.html


class Parser:

    def extract(self, task, text):
        tree = lxml.html.fromstring(text)
        outs = []

        for extractor in task.extractors:
            elements = tree.cssselect(extractor.selector)
            for elem in elements:
                out = {}
                for a in extractor.attributes:
                    out[a.name] = ""
                    if a.selector:
                        selected = elem.cssselect(a.selector)
                        if len(selected) == 0: continue
                        selectorElem = selected[0]
                        if a.attribute and a.attribute in selectorElem.attrib:
                            value = selectorElem.attrib[a.attribute]
                            out[a.name] = value
                        if not a.attribute:
                            value = selectorElem.text_content()
                            out[a.name] = value
                    else:
                        if a.attribute and a.attribute in elem.attrib:
                            value = elem.attrib[a.attribute]
                            out[a.name] = value

                outs.append(out)

        return outs