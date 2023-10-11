from extractor import gen

prompt = """The culprit is Foo. Foo was sitting on the chair closest to the cupcake."""
prompt += "\nSo as explained, the culprit is"
choices = ["Foo", "Bar", "Baz", "Foobar"]
print(gen(prompt, choices))
# Should return Foo, but seems to return the others rather frequently too.

d = {}
for c in choices:
    d[c] = 0

for i in range(0, 100):
    d[gen(prompt, choices)] += 1
print(d)
# {'Foo': 100, 'Bar': 0, 'Baz': 0, 'Foobar': 0}
