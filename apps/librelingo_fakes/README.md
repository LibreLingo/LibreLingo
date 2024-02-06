<a name="librelingo_fakes"></a>
# librelingo\_fakes

<a name="librelingo_fakes.fakes"></a>
# librelingo\_fakes.fakes

This package contains fake data for testing LibreLingo-related packages.

The fake data is returned using the types from [librelingo-types](https://pypi.org/project/librelingo-types/).

## Usage
```python

from librelingo_fakes import fakes

fakes.course1  # This is a Course() object
fakes.course2  # This is another Course() object
fakes.courseEmpty  # This is an empty course
```

For the full list of fakes, use the autocomplete or check out the [this file](https://github.com/LibreLingo/LibreLingo/blob/main/apps/librelingo_fakes/librelingo_fakes/fakes.py).

### Customizing fakes

You can use `fakes.customize` to change some attributes on a fake object.
If you want to change the modules on `fakes.course1`, you'd do it like this:

```python
fake_course = fakes.customize(fakes.course1, modules=[
    fake_module_1, fake_module_2
])
```

<a name="librelingo_fakes.fakes.number"></a>
#### number

```python
number(max_value=10000)
```

Returns a 'random' non-negative integer.
It is NOT cryptographically-secure.
