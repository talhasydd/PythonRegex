#Phone number and email scraper

import re, pyperclip

#regex for phone number
phoneNumber = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))?                        #area code(optional)
(\s|-)                                            #first separator
\d\d\d                                            #first 3 digits
-                                                 #second separator
\d\d\d\d                                          #last 4 digits
(((ext(\.)?\s)|x)                                 #extension(optional)
(\d{2,5}))?                                       #extension(optional)
)


''', re.VERBOSE)

#regex for email
email = re.compile('''

[a-zA-z0-9_.+]+                                   #custom character class for 1 or more characters
@                                                 #@ in email
.+                                                #any character 1 or more times

''', re.VERBOSE)

#paste text into variable
text = pyperclip.paste()

#extract data using the findall() method, returns list of tuples for phoneNumber
extractedNumber = phoneNumber.findall(text)
extractedEmail  = email.findall(text)

#create loop to extract first string in tuple
allNumbers = []
for phoneNumber in extractedNumber:
    allNumbers.append(phoneNumber[0])


result = 'Phone numbers:\n' + '\n'.join(allNumbers) + '\n\nEmail addresses:\n' + '\n'.join(extractedEmail)

print(result)                                   #It's also possible to use pyperclip.copy to copy it to clipboard for easy access
