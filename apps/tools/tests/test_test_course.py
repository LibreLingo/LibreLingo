import collections
import json
import os

from librelingo_json_export.export import export_course
from librelingo_yaml_loader.yaml_loader import load_course

Settings = collections.namedtuple(
    "Settings",
    [
        "dry_run",
    ],
)


def test_course(tmpdir):
    root = os.path.abspath(__file__)
    root = os.path.dirname(root)
    root = os.path.dirname(root)
    root = os.path.dirname(root)
    root = os.path.dirname(root)
    print(root)

    path_to_course = os.path.join(root, "courses", "test")
    course = load_course(path_to_course)

    settings = Settings(
        dry_run=False,
    )
    output_path = str(tmpdir)
    expected_path = os.path.join(root, "apps", "web", "src", "courses", "test")
    print(output_path)

    export_course(output_path, course, settings)
    for dirname, _, files in os.walk(output_path):
        for filename in files:
            relpath = os.path.join(dirname[len(output_path) + 1 :], filename)

            if filename.endswith(".json"):
                with open(os.path.join(output_path, relpath)) as fh:
                    actual = json.load(fh)
                with open(os.path.join(expected_path, relpath)) as fh:
                    expected = json.load(fh)
                assert actual == expected, relpath
                continue

            if filename.endswith(".md"):
                with open(os.path.join(output_path, relpath)) as fh:
                    actual = fh.read()
                with open(os.path.join(expected_path, relpath)) as fh:
                    expected = fh.read()
                assert actual == expected, relpath
                continue

            assert False, f"Unhandled file {relpath}"
