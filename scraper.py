import urllib2,re,string,operator

# create the request object and set some headers
req = urllib2.Request("http://www.eld.gov.sg/finalresults2015.html")
# make the request and print the results
res = urllib2.urlopen(req)
result= res.read()

location = {
'AJ':'Aljunied',
'AM':'Ang Mo Kio',
'BS':'Bishan-Toa Payoh',
'BK':'Bukit Batok', 
'BP':'Bukit Panjang', 
'CK':'Chua Chu Kang', 
'EC':'East Coast', 
'FS':'Fengshan', 
'HT':'Holland-Bukit Timah',
'HN':'Hong Kah North', 
'HG':'Hougang', 
'JB':'Jalan Besar', 
'JR':'Jurong', 
'MP':'MacPherson',
'MA':'Marine Parade', 
'MY':'Marsiling-Yew Tee', 
'MB':'Mountbatten',
'NS':'Nee Soon',
'PN':'Pasir Ris-Punggol',
'PI':'Pioneer',
'PS':'Potong Pasir',
'PE':'Punggol East',
'RM':'Radin Mas',
'SB':'Sembawang',
'SW':'Sengkang West',
'TM':'Tampines',
'TP':'Tanjong Pagar',
'WE':'West Coast',
'YH':'Yuhua'
}

count = dict()

results = re.findall(r'<!--(.*)_(.*)_FR-->\r\n([<b>\r\n]*.*[</b>]*)\r\n',result)

req = urllib2.Request("http://www.eld.gov.sg/samplecount2015.html")
# make the request and print the results
res = urllib2.urlopen(req)
result= res.read()

sc = re.findall(r'<!--(.*)_(.*)_SC-->\r\n(.*)',result)


for i,x in enumerate(results):
	if x[0] in location:
		if location[x[0]] in count:
			count[location[x[0]]] = count[location[x[0]]]+1
		else:
			count[location[x[0]]] = 1
		results[i] = (location[x[0]], x[1], x[2])
		print results[i]

for i,x in enumerate(sc):
	if x[0] in location:
		sc[i] = (location[x[0]], x[1], x[2])


output = file("index.html","wb")

output.write("<html><head><style>body {margin:0px;padding:0px} a {color:black;}.nothing{background-color:#aaa!important} .lose {background-color:#CD5C5C !important;}.win {background-color:#90EE90!important } * {font-family: 'Calibri';font-size:12px;}</style>")
output.write("<link rel='stylesheet' href='http://yui.yahooapis.com/pure/0.6.0/pure-min.css'></head><body>")


output.write("<h3>Final Results</h3><table class='pure-table'><thead>")
for i,x in enumerate(sorted(location.items(), key=operator.itemgetter(1))):
		output.write("<th colspan='"+str(count[location[x[0]]])+"''>"+location[x[0]]+"</th>")
output.write("</thead>")

output.write("<tr>")
for i,x in enumerate(results):
	output.write("<td>"+results[i][1]+"</td>")
output.write("</tr>")

output.write("<tr>")
for i,x in enumerate(results):
	if results[i][2][0:3] == "<b>":
		output.write("<td class='win'>"+results[i][2]+"</td>")
	elif results[i][2][0] == "-":
		output.write("<td class='nothing'>"+results[i][2]+"</td>")
	else:
		output.write("<td class='lose'>"+results[i][2]+"</td>")
output.write("</tr></table>")

if True == True :

	output.write("<h3>Sample Results</h3><table class='pure-table'><thead>")
	for i,x in enumerate(sorted(location.items(), key=operator.itemgetter(1))):
		output.write("<th colspan='"+str(count[location[x[0]]])+"''>"+location[x[0]]+"</th>")
	output.write("</thead>")

	output.write("<tr>")
	for i,x in enumerate(sc):
		output.write("<td>"+sc[i][1]+"</th>")
	output.write("</tr>")

	output.write("<tr>")
	for i,x in enumerate(sc):
		output.write("<td>"+sc[i][2]+"</th>")
	output.write("</tr></table>Summary made by <a href='https://sg.linkedin.com/in/quanyang'><b>Quan Yang</b></a>")

output.write("</body></html>")
