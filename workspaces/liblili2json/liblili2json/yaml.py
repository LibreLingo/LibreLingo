from pathlib import Path
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from liblili2json.types import Course, Language, License, Module, Skill


def load_yaml(path):
    """Helper function for simply loading a YAML file"""
    with open(path) as f:
        return load(f, Loader=Loader)


def convert_language(raw_language):
    """
    Convert a YAML langauge description into a Language() object
    """
    return Language(
        name=raw_language["Name"],
        code=raw_language["IETF BCP 47"],
    )


def load_dictionary():
    return []


def convert_word(raw_word):
    pass


def convert_words(raw_words):
    """
    Converts each YAML word definition into Word() objects
    """
    return list(map(convert_word, raw_words))


def convert_phrases():
    pass


def load_skill(path):
    data = load_yaml(path)
    skill = data["Skill"]
    words = data["New words"]
    phrases = data["Phrases"]

    return Skill(
        name=skill["Name"],
        id=skill["Id"],
        words=convert_words(words),
        phrases=convert_phrases(phrases),
        image_set=skill["Thumbnails"]
    )


def load_skills(path, skills):
    """
    Load each YAML skill specified in the list
    """
    return [load_skill(Path(path) / "skills" / skill) for skill in skills]


def load_module(path):
    """
    Load a YAML module
    """
    data = load_yaml(Path(path) / "module.yaml")
    module = data["Module"]
    skills = data["Skills"]

    return Module(
        title=module["Name"],
        skills=load_skills(path, skills)
    )


def load_modules(path, modules):
    """
    Load each YAML module specifed in the list
    """
    return [load_module(Path(path) / module) for module in modules]


def convert_license(raw_license):
    """
    Creates a License() object based on the data structure
    in the YAML file
    """
    return License(
        name=raw_license["Short name"],
        full_name=raw_license["Name"],
        link=raw_license["Link"],
    )


def load_course(path):
    """
    Load a YAML based course into a Course() object
    """
    data = load_yaml(Path(path) / "course.yaml")
    course = data["Course"]
    modules = data["Modules"]

    return Course(
        target_language=convert_language(course["Language"]),
        source_language=convert_language(course["For speakers of"]),
        license=convert_license(course["License"]),
        dictionary=load_dictionary(path),
        modules=load_modules(path, modules),
        special_characters=course["Special characters"],
    )
