import glob
import json
import os

from librelingo_json_export.export import export_course
from librelingo_yaml_loader import load_course


def read_json_file(path):
    with open(path) as file_path:
        return json.load(file_path)


def test_loaded_yaml_is_exported_to_correct_json(file_system, snapshot):
    fixture_path = os.path.join(os.path.dirname(__file__), "fixtures", "fake_course")
    file_system.add_real_directory(fixture_path)
    file_system.create_dir("output")
    course = load_course(fixture_path)
    export_course("./output", course)
    files = glob.glob("./output/**/*")
    data = {
        fname: read_json_file(fname) if fname.endswith(".json") else open(fname).read()
        for fname in files
    }

    file_system.pause()  # Write snapshots to the real fs, not the fake
    snapshot.assert_match(data)
