def comma(n):

    n.insert(-1,'and')

    return str(n).strip('[]').replace("'",'')
#convert a list of items into a string with commas and 'and' before the last item

n = [1,2,3,4,5]

print(comma(n))

