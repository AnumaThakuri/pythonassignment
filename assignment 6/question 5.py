def string(string):
    length=len(string)
    if length>2:
        if string[-3:]=='ing':
            string=string+'ly'
        else:
            string=string+'ing'
        return string
print(string('ab'))
print(string('abc'))
print(string('string'))