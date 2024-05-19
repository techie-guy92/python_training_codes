import re 

myInfo="""
Conference1
Topic: Object Oriented Programming
Date: 09/20/2022
Location: U.S.
Web: conf.usa/09/2022
Cost:     $1200
Conference2
Topic:    Python3
Date: 01/31/2022
Location: France
Web: conf.france/01/2022
Cost:$600
Conference3
Topic: Data Science
Date: 07/09/2022
Location: UK
Web: conf.org
Cost: $900
Conference4
Topic: Web Development
Date: 08/29/2022
Location: Canada
Web: conf.ca
Cost:      $1100
Conference5
Topic: Python for Beginners
Date: 05/09/2022
Location: Turkey
Web: conf.com
Cost: $90000
"""


CostOfConference=re.findall(r"Cost:\s*(\$.+)",myInfo)
# DateOfConference=re.findall(r"Date:\s(\d{2}/\d{2}/\d{4})",myInfo)
# TopicOfConference=re.findall(r"Topic:\s*(.+)",myInfo)
# LocationOfConference=re.findall(r"Location:\s*(.+)",myInfo)
# WebOfConference=re.findall(r"Web:\s*(.+[a-zA-Z])",myInfo)


CostOfConference2=re.sub(r"\s*\$.+",'\g<1>',CostOfConference)

print(CostOfConference2)
# print(DateOfConference)
# print(TopicOfConference)
# print(LocationOfConference)
# print(WebOfConference)