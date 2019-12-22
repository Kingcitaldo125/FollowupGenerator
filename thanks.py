import re

#includeLinkedIn = False
includeLinkedIn = True

name = str(input('Enter your name\n'))
company = str(input('Enter the company name\n'))
role = str(input('Enter the role\n'))
email = str(input('Enter your email address\n'))

genStr = ""
templateHolder=""

if includeLinkedIn:
	linkedin=""
	with open('linkedin.txt', 'r') as f:
		linkedin = f.readline()

with open('template.txt', 'r') as f:
	for ff in f.readlines():
		if not includeLinkedIn:
			m = re.search(r'LinkedIn', ff, re.M|re.I)
			if not m: # if the line is not the linkedin line, add it to the holder
				templateHolder += str(ff)
		else:
			templateHolder += str(ff)

templateHolder = re.sub(r'\[company\]', company, templateHolder, re.M|re.I)
templateHolder = re.sub(r'\[role\]', role, templateHolder, re.M|re.I)
templateHolder = re.sub(r'\[email\]', email, templateHolder, re.M|re.I)

if includeLinkedIn:
	templateHolder = re.sub(r'\[linkedin\]', linkedin, templateHolder, re.M|re.I)
	
templateHolder = re.sub(r'\[name\]', name, templateHolder, re.M|re.I)

templateHolder = re.sub(r'[.]$',".\n",templateHolder,re.I)

with open('out.txt', 'w') as f:
	f.write(templateHolder)
	f.write("\n")
