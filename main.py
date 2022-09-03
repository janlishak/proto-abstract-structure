import pdb


class Graph:
    def __init__(self):
        self.graph = {}
        self.unique = {}

    def abc(self, names):
        nodes=[None]*3
        for i in range(3):
            name = names[i]
            if name[0] == "+":
                if name in self.unique:
                    self.unique[name] += 1
                    name = name[1:] + str(self.unique[name])
                    names[i] = name
                else:
                    self.unique[name] = 1
                    name = name[1:] + str(self.unique[name])
                    names[i] = name

            if name not in self.graph:
                self.graph[name] = {}

            nodes[i] = self.graph[names[i]]

        nodes[0][names[1]] = nodes[1]
        nodes[1][names[0]] = nodes[0]
        nodes[1][names[2]] = nodes[2]
        nodes[2][names[1]] = nodes[1]

    def get(self, names):
        try:
            node = self.graph

            if len(names) == 1:
                return list(node[names[0]].keys())

            for i in range(len(names)):
                if names[i][0] == "#":
                    for k in node:
                        if str(k).startswith(names[i][1:]):
                            node = node[k]
                            continue
                    continue
                if names[i][0] == "*":
                    for k in node:
                        if str(k).startswith(names[i][1:]):
                            node = node[k]
                            continue
                    continue

                node = node[names[i]]

            keysList = list(node.keys())
            keysList.remove(names[len(names)-2])
            return keysList
        except KeyError as e:
            return "empty"


if __name__ == '__main__':
    graph = Graph()
    file1 = open('myfile.txt', 'r')
    lines = file1.readlines()
    for line in lines:
        line = line.strip()
        args = line.split(" ")
        if len(args) == 3:
            graph.abc(args)
    # pdb.set_trace()
    while True:
        line = input()
        line = line.strip()
        args = line.split(" ")
        if len(args) > 1:
            if args[0] == "get":
                args.remove(args[0])
                print(graph.get(args))

            elif args[0] == "set":
                args.remove(args[0])
                graph.abc(args)

            else:
                print("unknown arg " + args[0])
        else:
            print("error")

