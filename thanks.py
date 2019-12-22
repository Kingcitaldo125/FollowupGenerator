import re
import configparser

#includeLinkedIn = False
includeLinkedIn = True

cnfg = configparser.ConfigParser()
cnfg.read('configfile.ini')

name = str(cnfg['SectionOne']['NAME'])
company = str(cnfg['SectionOne']['COMPANY'])
role = str(cnfg['SectionOne']['ROLE'])
email = str(cnfg['SectionOne']['EMAIL'])
linkedin = str(cnfg['SectionOne']['LINKEDIN'])

genStr = ""
templateHolder=""

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
