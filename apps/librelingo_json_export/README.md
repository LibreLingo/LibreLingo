<a name="librelingo_json_export.export"></a>
# librelingo\_json\_export.export

<a name="librelingo_json_export.export.export_course"></a>
#### export\_course

```python
export_course(export_path: str, course: Course, settings=None)
```

Writes the course to JSON files in the specified path.

### Usage example:

```python
from librelingo_yaml_loader import load_course
from librelingo_json_export.export import export_course

course = load_course("./courses/french-from-english")
export_course("./apps/web/src/courses/french-from-english", course)
```
