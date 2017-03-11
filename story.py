import sys
tri = {}

for doc in sys.argv:
    with open(doc) as file:
        lines = ''.join(file.readlines()).split()
        for i in range(len(lines)):
            if (i+3 < len(lines)):
                if (lines[i] in tri):
                    if (lines[i+1] in tri[lines[i]]):
                        if (lines[i+2] in tri[lines[i]][lines[i+1]]):
                            tri[lines[i]][lines[i+1]][lines[i+2]] += 1
                        else:
                            tri[lines[i]][lines[i+1]][lines[i+2]] = 1
                    else:
                        tri1 = {}
                        tri2 = {}
                        tri2[lines[i + 2]] = 1
                        tri1[lines[i + 1]] = tri2
                else:
                    tri1 = {}
                    tri2 = {}
                    tri2[lines[i + 2]] = 1
                    tri1[lines[i + 1]] = tri2
                    tri[lines[i]] = tri1

for val in tri:
    print val, tri[val]


# tri1 = {}
# tri2 = {}
#
# tri2['monkey'] = 1
# tri1['eats'] = tri2
# tri['banana'] = tri1
#
# words = ['banana', 'eats', 'monkey']
# print tri[words[0]][words[1]][words[2]]
#
# if (words[0] in tri):
#     if (words[1] in tri[words[0]]):
#         if (words[2] in tri[words[0]][words[1]]):
#             tri[words[0]][words[1]][words[2]] += 1
#             print tri[words[0]][words[1]][words[2]]
