"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = ["0"] if not s else []
    count = 1
    for i, char in enumerate(s, 1):
        result.append(char)
        if i % 2 == 1:
            result[-1] = str(count)
            count += 2
        else:
            result[-1] = "-"
    return result
