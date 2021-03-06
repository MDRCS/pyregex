import re

"""
    Bytecode is an intermediary language. It's the output generated by languages,
    which will be later interpreted by an interpreter. The Java bytecode that is interpreted by JVM
    is probably the best known example.
"""

# RegexObject: It is also known as Pattern Object. It represents a compiled regular expression

RegexObject = re.compile(r'\bfoo\b')
MatchObject = RegexObject.match("foo bar")

print(MatchObject)

"""
    You can always use re.purge to clear the cache but this is a tradeoff with performance.
    Using compiled patterns allows you to have a fine-grained control of the memory consumption
    because you can decide when to purge them.
"""
re.purge()

RegexObject = re.compile(r'\w+')
MatchObject = RegexObject.findall("hello world")

print(MatchObject)

RegexObject = re.compile(r'a*')
MatchObject = RegexObject.findall("aba")  # match -> a // findall -> ['a', '', 'a', '']

print(MatchObject)

# The maxsplit parameter specifies how many splits can be done at maximum and returns the remaining part in the result:

RegexObject = re.compile(r"\W")
MatchObject = RegexObject.split("Beautiful is better than ugly", 3)

print(MatchObject)

# split

RegexObject = re.compile(r"(-)")
MatchObject = RegexObject.split("hello-world")

print(MatchObject)

# replace

RegexObject = re.compile(r"[0-9]+")
MatchObject = RegexObject.sub('-', "hello0-world13")

print(MatchObject)

# also

res = re.sub('00', "--", "hello00000")
print(res)


def normalize_orders(MatchObject):
    print(MatchObject.group(1))
    if MatchObject.group(1) == '-':
        return "A"
    else:
        return "B"


"""
    As mentioned previously, for each matched pattern the normalize_orders function is called.
    So, if the first matched group is a –, then we return an A; in any other case, we return B.
"""

# matchobject -> '([-|A-Z])'
res = re.sub('([-|A-Z])', normalize_orders, '-1234⇢A193⇢ B123')

print(res)

# groups

pattern = re.compile("(\w+) (\w+)")
match = pattern.search("Hello⇢World")

print(match.groups())



