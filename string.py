# mystr = "akash bhai sabsay jhakkaaas"

# print(mystr[0:5])
# print(len(mystr))

# print(mystr[0:5:2]) # it skip 1 character

# print(mystr[::-1]) # it reverse string 

# print(mystr.endswith("jhakkaaas"))

# print(mystr.count("a"))

# print(mystr.capitalize())

# print(mystr.find("sabsay"))

# print(mystr.lower())
# print(mystr.upper())

# print(mystr.replace("sabsay", "maha"))

# name = "amar-akbar-anthony"
# a = name.split("-")
# print(a)


###################### Regular Expressions ##################################################
# it is used to extract specific pattern in a string
import re

# what we do using Regular Expressions
# findall: It finds all search for matches and print resultant in the form of a list.
# search: It works the same as a findall, but the resultant is a matched object, if any found.
# split: The split function splits the string from every matched into two new strings.
# sub: The sub-function works exactly like a replace function in notepad or MS Word,
#          it replaces the original word, with a word of our choice.
# finditer: The finditer yields an iterator as a resultant with all the objects that match 
#           the one we sent it) finditer supports more attributes than any other function 
#           defined above. It also provides more details related to the matched object. 
#           So, most of the examples we are going to see next will contain a finditer function
#           in them.

"""
Meta Characters

[] -> A set of characters
\ -> Signals a special sequence (can also be used to escape special characters)
. -> Any character (except newline character)
^ -> Starts with
$ -> Ends with
*->  Zero or more occurrences
+ -> One or more occurrences
{} ->  Exactly the specified number of occurrences
| -> Either or
()->  Capture and group

Special Sequences

\A -> Returns a match if the specified characters are at the beginning of the string
\b -> Returns a match where the specified characters are at the beginning or
       at the end of a word r"ain\b"
\B->  Returns a match where the specified characters are present, 
        but NOT at the beginning (or at the end) of a word

\d -> Returns a match where the string contains digits (numbers from 0-9)
\D -> Returns a match where the string DOES NOT contain digits
\s -> Returns a match where the string contains a white space character
\S -> Returns a match where the string DOES NOT contain a white space character
\w -> Returns a match where the string contains any word characters 
      (characters from a to Z, digits from 0-9, and the underscore _ character)
\W ->  Returns a match where the string DOES NOT contain any word characters
\Z ->  Returns a match if the specified characters are at the end of the string

"""

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# findall, search, split, sub, finditer
# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
patt = re.compile(r'\d{5}-\d{4}')
# Task
# Given a string with a lot of indian phone numbers starting from +91

# to run our results

matches = patt.finditer(mystr)
for match in matches:
    print(match)
