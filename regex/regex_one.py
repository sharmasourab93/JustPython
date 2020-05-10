import re


if __name__ == '__main__':
    text = """Now is the winter of our discontent
Made glorious summer by this sun of York;
And all the clouds that lour'd upon our house
In the deep bosom of the ocean buried.
Now are our brows bound with victorious wreaths;
Our bruised arms hung up for monuments;
Our stern alarums changed to merry meetings,
Our dreadful marches to delightful measures.
Grim-visaged war hath smooth'd his wrinkled front;
And now, instead of mounting barded steeds
To fright the souls of fearful adversaries,
He capers nimbly in a lady's chamber
To the lascivious pleasing of a lute.
But I, that am not shaped for sportive tricks,
Nor made to court an amorous looking-glass;
I, that am rudely stamp'd, and want love's majesty
To strut before a wanton ambling nymph;
I, that am curtail'd of this fair proportion,
Write to me on sourabthenap@gmail.com, sharmasourab93@gmail.com
My DOB is 22nd Nov 1993, 22-11-1993
Then what do you think I will do then
That
    """
    
    # To Match email Ids
    # matches = re.finditer(r"([a-zA-Z0-9]+\@\w+\.\w+)", text)
    
    matches = re.findall(r"\w+\'\w+", text)
    
    # To substitute string with a character
    string = "The white rain lies in the dark white."
    # using_sub = re.sub("([\W])", '%', string)
    # print(using_sub)

    match = re.finditer("(T|t)h(en|at|is)", text)
    #for i in match:
     #   print(i)
    
    spliter = re.split("^[^N]\w+$", text)
    
    # print(spliter)
    
    ip = "^(\d+\.){3}\d+"
    ip_match = re.fullmatch("^(\d+\.){3}\d+", ip)
    # print(ip_match)
    
    bday = re.match()