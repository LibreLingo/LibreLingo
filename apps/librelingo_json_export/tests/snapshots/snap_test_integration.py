# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals
from pathlib import Path

from snapshottest import Snapshot  # type: ignore

snapshots = Snapshot()

snapshots["test_loaded_yaml_is_exported_to_correct_json 1"] = {
    str(Path("./output/challenges/hello.json")): {
        "challenges": [
            {
                "formInTargetLanguage": "La femme dit bonjour",
                "group": "921dd5d24167",
                "id": "6ebf41f2ce09",
                "meaningInSourceLanguage": "The woman says hello",
                "priority": 0,
                "type": "options",
            },
            {
                "answer": "La femme dit bonjour",
                "audio": "e0d059affc8ac676af5ad1fb8a9815fe877d19efa55d4298f36d03954b949b51",
                "group": "921dd5d24167",
                "id": "1866c2decb63",
                "meaning": "The woman says hello",
                "priority": 1,
                "type": "listeningExercise",
            },
            {
                "chips": ["La", "femme", "dit", "bonjour", "la", "salut", "L'homme"],
                "formattedSolution": "La femme dit bonjour",
                "group": "921dd5d24167",
                "id": "2e3fc4b0103a",
                "phrase": [
                    {
                        "definition": """la
le""",
                        "word": "The",
                    },
                    {"definition": "femme", "word": "woman"},
                    {"definition": "dit", "word": "says"},
                    {
                        "definition": """bonjour
salut""",
                        "word": "hello",
                    },
                ],
                "priority": 2,
                "solutions": [
                    ["La", "femme", "dit", "bonjour"],
                    ["la", "femme", "dit", "salut"],
                ],
                "translatesToSourceLanguage": False,
                "type": "chips",
            },
            {
                "chips": ["The", "woman", "says", "hello", "man", "hi"],
                "formattedSolution": "The woman says hello",
                "group": "921dd5d24167",
                "id": "038fe486182d",
                "phrase": [
                    {"definition": "the", "word": "La"},
                    {"definition": "woman", "word": "femme"},
                    {"definition": "says", "word": "dit"},
                    {
                        "definition": """hello
hi""",
                        "word": "bonjour",
                    },
                ],
                "priority": 2,
                "solutions": [
                    ["The", "woman", "says", "hello"],
                    ["The", "woman", "says", "hi"],
                ],
                "translatesToSourceLanguage": True,
                "type": "chips",
            },
            {
                "formInTargetLanguage": "L'homme dit bonjour",
                "group": "0f389ca8a0c4",
                "id": "df8dc7b5cf8b",
                "meaningInSourceLanguage": "The man says hello",
                "priority": 0,
                "type": "options",
            },
            {
                "answer": "L'homme dit bonjour",
                "audio": "d20aa20ddd1cbf6386226aa9328a2439d04db13183f1d035622ef5cbb722bac7",
                "group": "0f389ca8a0c4",
                "id": "b7b8863b13ae",
                "meaning": "The man says hello",
                "priority": 1,
                "type": "listeningExercise",
            },
            {
                "chips": ["L'homme", "dit", "bonjour", "La", "femme"],
                "formattedSolution": "L'homme dit bonjour",
                "group": "0f389ca8a0c4",
                "id": "5ebdd684bc01",
                "phrase": [
                    {
                        "definition": """la
le""",
                        "word": "The",
                    },
                    {"definition": "homme", "word": "man"},
                    {"definition": "dit", "word": "says"},
                    {
                        "definition": """bonjour
salut""",
                        "word": "hello",
                    },
                ],
                "priority": 2,
                "solutions": [
                    ["L'homme", "dit", "bonjour"],
                    ["L'homme", "dit", "salut"],
                ],
                "translatesToSourceLanguage": False,
                "type": "chips",
            },
            {
                "chips": ["The", "man", "says", "hello", "hi", "woman"],
                "formattedSolution": "The man says hello",
                "group": "0f389ca8a0c4",
                "id": "2d6b05be7089",
                "phrase": [
                    {"definition": "the man", "word": "L'homme"},
                    {"definition": "says", "word": "dit"},
                    {
                        "definition": """hello
hi""",
                        "word": "bonjour",
                    },
                ],
                "priority": 2,
                "solutions": [
                    ["The", "man", "says", "hello"],
                    ["The", "man", "says", "hi"],
                ],
                "translatesToSourceLanguage": True,
                "type": "chips",
            },
            {
                "formInTargetLanguage": "l'homme",
                "group": "f20e2aa89c50",
                "id": "765f2efca3b5",
                "meaningInSourceLanguage": "the man",
                "pictures": ["man1.jpg", "man2.jpg", "man3.jpg"],
                "priority": 0,
                "type": "cards",
            },
            {
                "formInTargetLanguage": ["l'homme"],
                "group": "f20e2aa89c50",
                "id": "ee2a7de8342b",
                "phrase": [
                    {
                        "definition": """la
le""",
                        "word": "the",
                    },
                    {"definition": "homme", "word": "man"},
                ],
                "pictures": ["man1.jpg", "man2.jpg", "man3.jpg"],
                "priority": 1,
                "type": "shortInput",
            },
            {
                "answer": "l'homme",
                "audio": "9bfce1b18e137b7af51c287726c5dcc914aab05ab1847832e1bfed12adc1cd9f",
                "group": "f20e2aa89c50",
                "id": "dcd103a2e758",
                "meaning": "the man",
                "priority": 1,
                "type": "listeningExercise",
            },
            {
                "formInTargetLanguage": "la femme",
                "group": "1c08a1db48bf",
                "id": "38734148215a",
                "meaningInSourceLanguage": "the woman",
                "pictures": ["man1.jpg", "man2.jpg", "man3.jpg"],
                "priority": 0,
                "type": "cards",
            },
            {
                "formInTargetLanguage": ["la femme", "la dame"],
                "group": "1c08a1db48bf",
                "id": "1f9d7215444b",
                "phrase": [
                    {
                        "definition": """la
le""",
                        "word": "the",
                    },
                    {"definition": "femme", "word": "woman"},
                ],
                "pictures": ["man1.jpg", "man2.jpg", "man3.jpg"],
                "priority": 1,
                "type": "shortInput",
            },
            {
                "answer": "la femme",
                "audio": "cabd9d1b9cae7227bd640f6ec302ea9ce0c551e7f94d23a7ff843ced6846c7da",
                "group": "1c08a1db48bf",
                "id": "0f716658c347",
                "meaning": "the woman",
                "priority": 1,
                "type": "listeningExercise",
            },
        ],
        "id": "379dca1c8ae9",
        "levels": 2,
    },
    str(Path("./output/introduction/hello.md")): """# Lorem Ipsum

## Dolor sit amet

Foo Bar""",
}
