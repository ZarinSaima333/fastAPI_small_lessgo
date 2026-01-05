def test_equal_or_not_equal():
    assert 3==3
    assert 3!=1

def test_is_instance():
    assert isinstance("this is a string",str)
    assert not isinstance('10',int)

def test_boolean():
    validated= True
    assert validated is True
    assert('hello'=='world') is False

def test_type():
    assert type('Hello' is str)
    assert type('World' is not str)

def test_greater_and_less_than():
    assert 7>3
    assert 4<10

def test_list():
    num_list=[1,2,3,4,5]
    any_list =[False,False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)
'''
✔ all() returns True if all elements are truthy
[1,2,3,4,5] → all non-zero → truthy

assert not any(any_list)
✔ any() returns True if at least one element is True

#Correct use of is

is should be used ONLY for:

None

True

False

Singleton objects

x = None
assert x is None     # ✅ correct

flag = True
assert flag is True  # acceptable
| Value      | Truthiness |
| ---------- | ---------- |
| `1, 2, -5` | ✅ True     |
| `0`        | ❌ False    |
| `"hello"`  | ✅ True     |
| `""`       | ❌ False    |
| `[]`       | ❌ False    |
| `None`     | ❌ False    |
| `False`    | ❌ False    |

'''