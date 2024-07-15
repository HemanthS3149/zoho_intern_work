import re

text="""
John Doe <john.doe@gmail.com>
Jane Smith <jane_smith123@gomain.org>
admin@yghin.co.uk
contact@company.com
"""

pattern=r'[\w\.-]+@[\w\.-]+\.\w+' #1st half matches 1 or more occurences of word,. or -. And \. means literal dot instead of meaning "Any character"

matches=re.findall(pattern,text)
print(matches)

#Phone number matching
text="""
John: (123) 456-7890
Jane: 123-456-7890
Ravi: +1-123-456-7890
"""

pattern=r'\+?\d{0,2}-?\(?\d{3}\)?-?\d{3}-\d{4}' #1st matches + literally
#? means matches 0 or 1 occurrence of the preceding character('+' in this case),,,,-? means matches '-' directly
matches=re.findall(pattern,text)

print(matches)

#Matching dates
text="""
Start Date: 2024-07-01
End Date: 01/07/2024
Event Date:July 1,2024
"""
pattern=r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|[A-Za-z]+ \d{1,2}, \d{4}'

matches=re.findall(pattern,text)
print(matches)

#Matching URLs
text="""
Visit our website at http://website.com
Secure site: https://secure-site.org.
Check out our page: www.page.com.
"""

pattern=r'https?://[\w\.-]+|www\.[\w\.-]+'
#https? means matches http by an optional s

matches=re.findall(pattern,text)
print(matches)
