<a name="librelingo_types"></a>
# librelingo\_types

Data types to be used in Python packages for LibreLingo

<a name="librelingo_types.data_types"></a>
# librelingo\_types.data\_types

<a name="librelingo_types.data_types.TextToSpeechSettings"></a>
## TextToSpeechSettings Objects

```python
class TextToSpeechSettings(
    namedtuple(
        "TextToSpeechSettings",
        [
            "provider",
            "voice",
            "engine",
        ],
        defaults=["Polly", "Lupe", "standard"],
    ))
```

Settings about how to use TTS to generate audios

### Usage example:

>>> TextToSpeechSettings(
...     provider="Polly",
...     voice="Aditi",
...     engine="standard"
... )
TextToSpeechSettings(provider='Polly', voice='Aditi', engine='standard')

<a name="librelingo_types.data_types.AudioSettings"></a>
## AudioSettings Objects

```python
class AudioSettings(
    namedtuple(
        "AudioSettings",
        [
            "enabled",
            "text_to_speech_settings_list",
        ],
        defaults=[False, []],
    ))
```

Settings for audio in a course

### Usage example:

>>> AudioSettings(
...     enabled=True,
...     text_to_speech_settings_list=[TextToSpeechSettings()]
... )
AudioSettings(enabled=True, text_to_speech_settings_list=[TextToSpeechSettings(provider='Polly', voice='Lupe', engine='standard')])

<a name="librelingo_types.data_types.HunspellSettings"></a>
## HunspellSettings Objects

```python
class HunspellSettings(
    namedtuple(
        "HunspellSettings",
        [
            "source_language",
            "target_language",
        ],
        defaults=[None, None],
    ))
```

Settings for hunspell spell checking

### Usage example:

>>> HunspellSettings(
...     source_language="en-US",
...     target_language="es-ES",
... )
HunspellSettings(source_language='en-US', target_language='es-ES')

<a name="librelingo_types.data_types.Settings"></a>
## Settings Objects

```python
class Settings(
    namedtuple(
        "Settings",
        ["audio_settings", "hunspell"],
        defaults=[AudioSettings(), HunspellSettings()],
    ))
```

Settings for a course

### Usage example:

>>> Settings()
Settings(audio_settings=AudioSettings(enabled=False, text_to_speech_settings_list=[]), hunspell=HunspellSettings(source_language=None, target_language=None))

<a name="librelingo_types.data_types.Course"></a>
## Course Objects

```python
class Course(
    namedtuple(
        "Course",
        [
            "target_language",
            "source_language",
            "special_characters",
            "modules",
            "license",
            "dictionary",
            "repository_url",
            "course_dir",
            "settings",
        ],
        defaults=[Settings()],
    ))
```

A LibreLingo course

### Usage example:

```python
my_course = Course(
    target_language=Language("English", "en"),
    source_language=Language("Spanish", "es"),
    special_characters=[],
    modules=[module1, module2, module3, module4],
    license=License(
        full_name="Attribution 4.0 International (CC BY 4.0)",
        name="CC BY 4.0",
        link="https://creativecommons.org/licenses/by/4.0/"
    ),
    dictionary=[dict_item1, dict_item2, dict_item3, dict_item4],
    repository_url="https://example.com",
    course_dir="some_language/course",
    settings=Settings()
)
```

<a name="librelingo_types.data_types.Language"></a>
## Language Objects

```python
class Language(namedtuple("Language", ["name", "code"]))
```

Metadata about a language

### Usage example:

>>> Language("English", "en")
Language(name='English', code='en')

<a name="librelingo_types.data_types.License"></a>
## License Objects

```python
class License(
    namedtuple(
        "License",
        [
            "name",
            "full_name",
            "link",
        ],
    ))
```

Metadata about the license of a LibreLingo course

### Usage example:

>>> License(
...     full_name="Attribution 4.0 International (CC BY 4.0)",
...     name="CC BY 4.0",
...     link="https://creativecommons.org/licenses/by/4.0/"
... )
License(name='CC BY 4.0', full_name='Attribution 4.0 International (CC BY 4.0)', link='https://creativecommons.org/licenses/by/4.0/')

<a name="librelingo_types.data_types.Module"></a>
## Module Objects

```python
class Module(
    namedtuple(
        "Module",
        [
            "title",
            "filename",
            "skills",
        ],
    ))
```

A module of a LibreLingo course.

### Usage examples:

```python
my_module = Module(title="Basics", filename="basic/module.yaml", skills=[skill1, skill2])
```

<a name="librelingo_types.data_types.Skill"></a>
## Skill Objects

```python
class Skill(
    namedtuple(
        "Skill",
        [
            "name",
            "filename",
            "id",
            "words",
            "phrases",
            "image_set",
            "dictionary",
            "introduction",
        ],
    ))
```

A skill of a module of a LibreLingo course.

### Notes:

*id*: Needs to be a unique ID. Use uuidv4.

### Usage examples:

```python
my_skill = Skill(
    name="Animals",
    filename="basic/skills/hello.yaml",
    id="3adc78da-ea42-4ecd-9e3d-2e0986a3b914",
    words=[word1, word2, word3],
    phrases=[phrases1, phrases2, phrases3],
    image_set=["cat1", "dog2", "horse1"],
    dictionary=[dict_item_1, dict_item_2, dict_item_3, dict_item_4],
    introduction="My *markdown* text",
)
```

<a name="librelingo_types.data_types.Word"></a>
## Word Objects

```python
class Word(
    namedtuple(
        "Word",
        [
            "in_target_language",
            "in_source_language",
            "pictures",
        ],
    ))
```

A new word taught in a LibreLingo skill.

### Notes:

*in_source_language*: List of accepted forms in the target language of the
course. The first item in the list is the main form. The main form is the
only form that is shown in the course but all forms are accepted as
answers.

*in_target_language*: List of accepted forms in the target language of the
course. The first item in the list is the main form. The main form is the
only form that is shown in the course but all forms are accepted as
answers.

### Usage example:

>>> Word(
...     in_target_language=["perro"],
...     in_source_language=["dog"],
...     pictures=["dog1", "dog2", "dog3"]
... )
Word(in_target_language=['perro'], in_source_language=['dog'], pictures=['dog1', 'dog2', 'dog3'])

<a name="librelingo_types.data_types.Phrase"></a>
## Phrase Objects

```python
class Phrase(
    namedtuple(
        "Phrase",
        [
            "in_target_language",
            "in_source_language",
        ],
    ))
```

A new phrase taught in a LibreLingo skill.

### Notes:

*in_source_language*: List of accepted forms in the target language of the
course. The first item in the list is the main form. The main form is the
only form that is shown in the course but all forms are accepted as
answers.

*in_target_language*: List of accepted forms in the target language of the
course. The first item in the list is the main form. The main form is the
only form that is shown in the course but all forms are accepted as
answers.

### Usage example:

>>> Phrase(
...     in_target_language=["perro", "can"],
...     in_source_language=["dog"],
... )
Phrase(in_target_language=['perro', 'can'], in_source_language=['dog'])

<a name="librelingo_types.data_types.DictionaryItem"></a>
## DictionaryItem Objects

```python
class DictionaryItem(
    namedtuple("DictionaryItem", ["word", "definition", "is_in_target_language"]))
```

A dictionary item for a LibreLingo course. It contains the definition of
a word. The word can be either in the source language or the target
language.

Definition in the source language (Spanish in this case)
>>> DictionaryItem("hablo", "I speak", False)
DictionaryItem(word='hablo', definition='I speak', is_in_target_language=False)

Definition in the target language (English in this case)
>>> DictionaryItem("speak", "hablo", True)
DictionaryItem(word='speak', definition='hablo', is_in_target_language=True)

<a name="librelingo_types.data_types.PhraseIdentity"></a>
## PhraseIdentity Objects

```python
class PhraseIdentity(namedtuple("PhraseIdentity", ["text", "source"]))
```

This is the set of information that identifies a phrase as 'the same'. If any
of these things change, the phrase will be seen as 'new' and re-generated.
