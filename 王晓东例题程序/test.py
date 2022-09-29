data1 = {"name":"a", "age":10, "sexy":"man"}
kwargs = {"a":1, "b":2}
def test(**kwargs):
    print(kwargs)
d = {"a":1, "b":2}
test()