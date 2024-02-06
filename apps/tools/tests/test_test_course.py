# pylint: skip-file
import json
import os

from librelingo_json_export.export import export_course
from librelingo_yaml_loader.yaml_loader import load_course
from librelingo_fakes import fakes


def test_exported_test_course_matches_snapshot_1(tmpdir):
    root = os.path.abspath(__file__)
    root = os.path.dirname(root)
    root = os.path.dirname(root)
    root = os.path.dirname(root)
    root = os.path.dirname(root)
    path_to_course = os.path.join(root, "courses", "test-1")
    course = load_course(path_to_course)

    settings = fakes.settings_not_dry_run()
    output_path = str(tmpdir)
    expected_path = os.path.join(root, "apps", "web", "src", "courses", "test-1")

    export_course(output_path, course, settings)
    assert_folders_are_identical(expected_path, output_path)


def assert_folders_are_identical(expected_path, actual_path):
    for dirname, _, files in os.walk(actual_path):
        for filename in files:
            relpath = os.path.join(dirname[len(actual_path) + 1 :], filename)

            if filename.endswith(".json"):
                with open(os.path.join(actual_path, relpath), encoding="utf-8") as fh:
                    actual = json.load(fh)
                with open(os.path.join(expected_path, relpath), encoding="utf-8") as fh:
                    expected = json.load(fh)
                assert actual == expected, relpath
                continue

            if filename.endswith(".md"):
                with open(os.path.join(actual_path, relpath)) as fh:
                    actual = fh.read().strip()
                with open(os.path.join(expected_path, relpath)) as fh:
                    expected = fh.read().strip()
                assert actual == expected, relpath
                continue

            assert False, f"Unhandled file {relpath}"
