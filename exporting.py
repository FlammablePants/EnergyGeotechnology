# HCPSphere output to create new templatemaker document
import re
count = 1
# newpos = re.split('; |, |\*|\n',f)
# pos = f.find("("):f.find(")")]

with open('list.txt') as f:
    content = f.readlines()
print content

# for i in range(1, len(content)):
# 	newlist = content.split(' ')
# print newlist
pos = []
for row in content:
	pos.append(row[6:-1])
print pos

f2 = open('positions.txt', 'wb')
f2.write("def templatemaker" + "\n")
f2.write("bs = 0.55" + "\n")
f2.write("command" + "\n")
f2.write("clump template make mygrain 941 &" + "\n")
f2.write("radii bs &" + "\n")
for i in pos:
	f2.write("bs &" + "\n")
f2.write("pos" + "\t")
for i in pos:
	f2.write(i + "\t" + "&" + "\n")

f2.write(pos[len(pos)-1] + "\n")
f2.write("end_command" + "\n")
f2.write("end" + "\n" + "\n")
f2.write("templatemaker") 


