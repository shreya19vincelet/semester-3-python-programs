import re 
text=input("enter the desired string ")
words=re.findall(r"[A-Z][a-z]+",text)
print(words)
parts=re.split(r"but",text)
print(parts)
def double(m):
    return(str(int(m.group())*2))
doubled=re.sub(r"\d+",double,text)
print(doubled)
