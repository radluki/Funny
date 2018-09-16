import re


class NamespaceIndexer:

    def __init__(self, file_path, namespace_list, class_name, new_class_name):
        self.filePath = file_path
        self.namespaceList = namespace_list
        self.className = class_name
        self.newClassName = new_class_name

    def parse_namespaces(self, s):
        pattern = re.compile(r'[\w_:]+')

    def index(self):
        with open(self.filePath, 'r') as r, open('out.txt', 'w') as w:
            current_namespace = list()
            open_brackets = 0
            namespace_pattern = re.compile(r'namespace\s+([\w_]+)')
            for line in r:
                match = namespace_pattern.match(line)
                if match:
                    current_namespace.append(match.group(1))
                    print(line[:-1])
                else:
                    open_brackets += line.count('{')
                    open_brackets -= line.count('}')
                    current_namespace = current_namespace[:min(open_brackets, len(current_namespace))]
                    current_namespace_len = len(current_namespace)
                    expected_namespace_len = len(self.namespaceList)
                    if current_namespace_len <= expected_namespace_len and \
                            self.namespaceList[:current_namespace_len] == current_namespace:
                        remaining_namespaces = self.namespaceList[current_namespace_len:]
                        old = "::".join(remaining_namespaces + [self.className])
                        new = "::".join(remaining_namespaces + [self.newClassName])
                        line_out = re.sub(old, new, line)
                        print(line_out, end='')
                    else:
                        print(line, end='')


if __name__ == '__main__':
    indexer = NamespaceIndexer(r'.\tests\MyClassTest.cpp', ['x'], 'MyClass', 'NewClass')
    indexer.index()
