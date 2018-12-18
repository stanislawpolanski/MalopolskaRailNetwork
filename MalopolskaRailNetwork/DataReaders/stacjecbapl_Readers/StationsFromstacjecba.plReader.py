#inputs:
path = r'C:\Users\Dell\source\repos\MalopolskaRailNetwork\MalopolskaRailNetwork\SourceFiles\MSK\stacjecbapl20180912_1020.xml'

#parse xml and select 'table' nodes (those with data)
from xml.dom.minidom import parse
dom = parse(path)
xmlnodes = dom.getElementsByTagName('table')

#seperate nodes from xml file
nodesList = []
for n in xmlnodes:
	currentNodeToList = dict()

	currentNodeToList['name'] = n.getAttribute('name')

	elements = n.getElementsByTagName('column')

	for e in elements:
		key = e.getAttribute('name')
		currentNodeToList[key] = e.firstChild.nodeValue

	nodesList.append(currentNodeToList)
#extract railways
#extract owners
#extract stations to railways
#extract stations from objects