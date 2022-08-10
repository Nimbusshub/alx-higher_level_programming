# Python - Everything is object

![Background Context](https://github.com/Nimbusshub/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/batman.gif)

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```bash
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

OK. But what about this?

```bash
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

## Files in the Directory

All `.txt` files stores answer to questions relating to classes, objects, instances, mutable and immutable data types, references as well as assignments in **Python**

| Filename              | Description                                                                                                                                                                        |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `19-copy_list.py`     | Function that returns a copy of a list                                                                                                                                             |
| `100-magic_string.py` | Function that returns a string "BestSchool" n times the number of the iteration                                                                                                   |
| `101-locked_class.py` | Class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance is called `first_name` |

## PS

This is a project done during **Full Stack Software Engineering** studies at **ALX_AFRICA**. The objectives of the project is teach **ALX-SE students** about the difference between a class and an object or instance, the difference between immutable object and mutable object, reference, assignments as well as data types in **Python**.
