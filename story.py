import sys
import random
tri = {}

for doc in sys.argv:
    with open(doc, 'r') as file:
        lines = ''.join(file.readlines()).lower().split()
        for i in range(len(lines)):
            if (i+3 < len(lines)):
                if (lines[i] in tri):
                    if (lines[i+1] in tri[lines[i]]):
                        if (lines[i+2] in tri[lines[i]][lines[i+1]]):
                            tri[lines[i]][lines[i+1]][lines[i+2]] += 1
                        else:
                            tri[lines[i]][lines[i+1]][lines[i+2]] = 1
                    else:
                        tri2 = {}
                        tri2[lines[i + 2]] = 1
                        tri[lines[i]][lines[i + 1]] = tri2
                else:
                    tri1 = {}
                    tri2 = {}
                    tri2[lines[i + 2]] = 1
                    tri1[lines[i + 1]] = tri2
                    tri[lines[i]] = tri1


newStory = []
key = random.choice(tri.keys())
key1 = random.choice(tri[key].keys())
newStory.append(key)
newStory.append(key1)

for j in range(2, 1000):
    posNextWord = tri[newStory[j-2]][newStory[j-1]]
    probArr = []
    for key in posNextWord:
        for i in range(posNextWord[key]):
            probArr.append(key)

    newStory.append(random.choice(probArr))


with open('story.txt', 'w') as writeFile:
    writeFile.write(" ".join(newStory))
