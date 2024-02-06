#!/usr/bin/env python

import re
import sys

from librelingo_yaml_loader.yaml_loader import load_course

reports = {}


def collect(key, module, skill, search_word, expressions):
    for expression in expressions:
        for word in re.split(r"[ .,]", expression):
            if search_word == word.lower():
                if key not in reports:
                    reports[key] = []
                reports[key].append(f"{module.title}/{skill.name} {expression}")
                break


def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} COURSE_DIR WORD")
    course_path, original_search_word = sys.argv[1], sys.argv[2]
    search_word = original_search_word.lower()
    course = load_course(course_path)
    for module in course.modules:
        for skill in module.skills:
            # Word(
            #   in_target_language=['el chapeo', 'el chapeyo'],
            #   in_source_language=['the hat'],
            #   pictures=['hat1', 'hat2', 'hat3']
            # )
            for word in skill.words:
                collect(
                    "target_word", module, skill, search_word, word.in_target_language
                )
                collect(
                    "source_word", module, skill, search_word, word.in_source_language
                )

            # left: a string           'hat'
            # right: tuple of strings  ('kazado', 'kazada')
            # target_to_source: boolean
            for left, right, target_to_source in skill.dictionary:
                # print(left, right, target_to_source)
                if target_to_source:
                    collect("target_dictionary", module, skill, search_word, [left])
                    collect(
                        "source_dictionary", module, skill, search_word, list(right)
                    )
                else:
                    collect("source_dictionary", module, skill, search_word, [left])
                    collect(
                        "target_dictionary", module, skill, search_word, list(right)
                    )

            # Phrase(in_target_language=['mi livro'], in_source_language=['my book'])
            for phrase in skill.phrases:
                collect(
                    "target_phrase",
                    module,
                    skill,
                    search_word,
                    phrase.in_target_language,
                )
                collect(
                    "source_phrase",
                    module,
                    skill,
                    search_word,
                    phrase.in_source_language,
                )
    # print(reports)
    for key in [
        "source_phrase",
        "source_dictionary",
        "source_word",
        "target_phrase",
        "target_dictionary",
        "target_word",
    ]:
        if key in reports:
            print(f"-- {key} --")
            for found in reports[key]:
                print(found)


if __name__ == "__main__":
    main()
