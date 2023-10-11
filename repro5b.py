from extractor import gen_fresh

prompt = """The culprit is Foo. Foo was sitting on the chair closest to the cupcake."""
prompt += "\nSo as explained, the culprit is"
choices = ["Foo", "Bar", "Baz", "Foobar"]
print(gen_fresh(prompt, choices))
# Should return Foo, but seems to return the others rather frequently too.

d = {}
for c in choices:
    d[c] = 0

for i in range(0, 100):
    d[gen_fresh(prompt, choices)] += 1
print(d)
# Much better!
# {'Foo': 94, 'Bar': 0, 'Baz': 0, 'Foobar': 6}
