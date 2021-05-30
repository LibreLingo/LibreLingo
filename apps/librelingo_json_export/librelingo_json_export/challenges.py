import itertools
from .challenge_types import *


def make_challenges_using(callback, data_source, course):
    """
        Calls a callback function with an item (Word or Phrase)
        to create challenges. Each item in the data source will
        be used.
    """
    return list(itertools.chain(
        *map(lambda item: callback(item, course), data_source)))


def challenge_mapper(challenge_types):
    """
        Returns a function that applies challenge types
        to a certain item (Word or Phrase), using the settings
        of the given course.
    """
    def map_challenge_creators(item, course):
        return list(map(lambda f: f(item, course), challenge_types))

    return map_challenge_creators


def _get_phrase_challenges(phrase, course):
    "Generate challenges based on a Phrase"
    return challenge_mapper([
        get_options_challenge,
        get_listening_challenge,
        *(
            [get_chips_challenge, get_reverse_chips_challenge]
            if is_long_enough_to_have_chips(phrase) else [])
    ]
    )(phrase, course)


def _get_word_challenges(word, course):
    "Generate challenges based on a Word"
    return challenge_mapper([
        get_cards_challenge,
        get_short_input_challenge,
        get_listening_challenge]
    )(word, course)


def get_challenges_data(skill, course):
    """
        Generates challenges for a certain Skill
    """
    return sum([
        make_challenges_using(_get_phrase_challenges, skill.phrases, course),
        make_challenges_using(_get_word_challenges, skill.words, course),
    ], start=[])
