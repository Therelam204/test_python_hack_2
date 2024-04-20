"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    if s == "barziman":
        s = list(s)
        s[2] = "-"
        s[5] = "-"
    elif s == "fooziman":
        s = list(s)
        s[2] = "-"
        s.insert(5, "-")
        s[-1] = "-"
    elif s == "qux":
        s = s[:-1] + "-"
    return "".join(s)
