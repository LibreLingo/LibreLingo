<a name="librelingo_utils"></a>
# librelingo\_utils

librelingo-utils contains utility functions that are meant to make it easier
to create Python software that works with LibreLingo courses.

<a name="librelingo_utils.utils"></a>
# librelingo\_utils.utils

<a name="librelingo_utils.utils.calculate_number_of_levels"></a>
#### calculate\_number\_of\_levels

```python
calculate_number_of_levels(nwords: int, nphrases: int) -> int
```

Calculates how many levels a skill should have

<a name="librelingo_utils.utils.get_words_from_phrase"></a>
#### get\_words\_from\_phrase

```python
get_words_from_phrase(phrase)
```

Splits a phrase into its component words/terms. Note that this respects
grouping with curly braces, i.e. sets of words surrounded by curly braces will not
be split from each other.

<a name="librelingo_utils.utils.remove_control_characters_for_display"></a>
#### remove\_control\_characters\_for\_display

```python
remove_control_characters_for_display(phrase)
```

Removes characters with special LibreLingo functions from a phrase before it
is displayed to the user.
At the moment, this only applies to curly brackets used to group several
words into a single mini-dictionary term.

<a name="librelingo_utils.utils.clean_word"></a>
#### clean\_word

```python
@lru_cache(maxsize=None)
clean_word(word: Word)
```

Remove punctuation and other special characters from a word.

<a name="librelingo_utils.utils.get_dumb_opaque_id"></a>
#### get\_dumb\_opaque\_id

```python
get_dumb_opaque_id(name: str, id_, salt: str = "") -> str
```

Generate a unique, opaque ID based on a name, and id_ and a salt
id

<a name="librelingo_utils.utils.get_opaque_id"></a>
#### get\_opaque\_id

```python
get_opaque_id(obj, salt: str = "") -> str
```

Generate a unique, opaque ID based on a salt and the type of the object
id

<a name="librelingo_utils.utils.audio_id"></a>
#### audio\_id

```python
audio_id(language: Language, text: str) -> str
```

Generate the ID that will identify the audio file of a sentence.

<a name="librelingo_utils.utils.iterate_phrases"></a>
#### iterate\_phrases

```python
iterate_phrases(course: Course)
```

"Flatten" a course into a sequence of phrases

<a name="librelingo_utils.utils.iterate_words"></a>
#### iterate\_words

```python
iterate_words(course: Course)
```

"Flatten" a course into a sequence of words
