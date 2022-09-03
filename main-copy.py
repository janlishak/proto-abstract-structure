# import pdb
#
#
# class Graph:
#     def __init__(self):
#         self.graph = {}
#         self.unique = {}
#
#     def abc(self, names):
#         for i in range(len(names)):
#             name = names[i]
#             if name[0] == "+":
#                 if name in self.unique:
#                     self.unique[name] += 1
#                     name = name[1:] + str(self.unique[name])
#                     names[i] = name
#                 else:
#                     self.unique[name] = 0
#                     name = name[1:] + str(self.unique[name])
#                     names[i] = name
#                 print(name)
#             if name not in self.graph:
#                 self.graph[name] = {}
#
#         node1 = self.graph[names[0]]
#         node2 = self.graph[names[1]]
#         node3 = self.graph[names[2]]
#
#         node1[names[1]] = node2
#         node2[names[0]] = node1
#         node2[names[2]] = node3
#         node3[names[1]] = node2
#
#
# if __name__ == '__main__':
#     graph = Graph()
#     file1 = open('myfile.txt', 'r')
#     lines = file1.readlines()
#     for line in lines:
#         line = line.strip()
#         args = line.split(" ")
#         if len(args) == 3:
#             print(args)
#             graph.abc(args)
#     pdb.set_trace()
