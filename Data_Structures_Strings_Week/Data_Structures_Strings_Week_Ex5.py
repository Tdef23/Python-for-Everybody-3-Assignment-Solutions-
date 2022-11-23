#Exercise 5: Take the following Python code that stores
#a string:

#str = 'X-DSPAM-Confidence:0.8475'

#Use find and string slicing to extract the portion
#of the string after the colon character and then use
#the float function to convert the extracted string
#into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'

atpos = str.find(':')

spos = str.find(' ', atpos)

fpn = float(str[atpos+1:spos])

print(fpn)

print(type(fpn))
