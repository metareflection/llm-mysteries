from extractor import gen

prompt = """The culprit is Foo. Foo was sitting on the chair closest to the cupcake."""
prompt += "\nSo as explained, the culprit is"
choices = ["Foo", "Bar", "Baz", "Foobar"]
answer = gen(prompt, choices)
print(answer)
assert answer == 'Foo'

d = {}
for c in choices:
    d[c] = 0

for i in range(0, 100):
    answer = gen(prompt, choices)
    d[answer] += 1
    print(answer)
print(d)
assert d['Foo'] == 100
