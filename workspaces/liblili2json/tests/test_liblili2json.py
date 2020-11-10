from unittest.mock import patch
from unittest import TestCase
from liblili2json import get_course_data
from liblili2json import get_skill_data
from liblili2json import get_challenges_data
from liblili2json import calculate_number_of_levels
from liblili2json import get_word_challenges
from liblili2json import get_cards_challenge
from liblili2json import get_short_input_challenge
from liblili2json import get_listening_challenge
from . import fakes


def test_get_course_data_return_value():
    """
    Tests the return value of get_course_data with the
    fakes.course1 object
    """
    assert get_course_data(fakes.course1) == {
        "languageName": "my language",
        "languageCode": "de",
        "specialCharacters": ["ä", "ß"],
        "license": {
            "name": {
                "short": "foo",
                "full": "foo bar license",
            },
            "link": None,
        },
        "modules": [
            {
                "title": "Basics",
                "skills": [
                    {
                        "title": "Masculine",
                        "practiceHref": "masculine",
                        "summary": ["lorem ipsum"],
                        "imageSet": ["man1", "man2", "boy1"],
                        'id': 'd7279e4777cd',
                        "levels": 1,
                    },
                    {
                        "title": "Feminine",
                        "practiceHref": "feminine",
                        "imageSet": ["woman1", "woman2", "girl1"],
                        "summary": ["foous", "apfel",  "foous", "apfel", "foous barus"],
                        'id': 'd7279e4777cd',
                        "levels": 2,
                    },
                    {
                        "title": "Neuter",
                        "summary": [],
                        "practiceHref": "neuter",
                        "imageSet": ["foo1", "bar1", "bar2"],
                        'id': 'd7279e4777cd',
                        "levels": 1,
                    },
                ]
            },
            {
                "title": "Phrases",
                "skills": []
            }
        ]
    }


def test_get_course_data_return_value_2():
    """
    Tests the return value of get_course_data with the
    fakes.course2 object
    """
    assert get_course_data(fakes.course2) == {
        "languageName": "another language",
        "languageCode": "tr",
        "specialCharacters": ["ç", "ş"],
        "license": {
            "name": {
                "short":  "lorem",
                "full": "ipsum lorem license"
            },
            "link":  "https://example.com/lipsum_license",
        },
        "modules": [
            {
                "title": "Animals",
                "skills": [
                    {
                        'id': 'd7279e4777cd',
                        "title": "Mammals and birds",
                        "practiceHref": "mammals-and-birds",
                        "summary": ["foous"],
                        "levels": 1,
                    }
                ]
            },
        ]
    }


def test_calculate_number_of_levels():
    examples = [
        {"words": 0, "phrases": 0, "result": 1},
        {"words": 10, "phrases": 0, "result": 2},
        {"words": 0, "phrases": 10, "result": 3},
        {"words": 10, "phrases": 10, "result": 4},
    ]

    for example in examples:
        assert calculate_number_of_levels(
            example["words"], example["phrases"]) == example["result"]


class TestGetSkillData(TestCase):
    def test_empty_skill(self):
        assert get_skill_data(fakes.skills[0], fakes.course1) == {
            "id": "d7279e4777cd",
            "levels": 1,
            "challenges": []
        }

    @patch('liblili2json.calculate_number_of_levels')
    def test_correct_number_of_levels(self, mock):
        FAKE_NUMBER = "fake number"
        mock.return_value = FAKE_NUMBER
        converted_skill = get_skill_data(fakes.emptySkill, fakes.course1)
        assert converted_skill["levels"] == FAKE_NUMBER

    @patch('liblili2json.calculate_number_of_levels')
    def test_calculates_levels_correctly(self, mock):
        get_skill_data(fakes.skills[1], fakes.course1)
        mock.assert_called_with(4, 1)

    @patch('liblili2json.get_challenges_data')
    def test_correct_challenges(self, mock):
        FAKE_CHALLENGES = "fake challenges"
        mock.return_value = FAKE_CHALLENGES
        converted_skill = get_skill_data(fakes.skills[1], fakes.course1)
        assert converted_skill["challenges"] == FAKE_CHALLENGES

    @patch('liblili2json.get_challenges_data')
    def test_formats_challenges_correctly(self, mock):
        get_skill_data(fakes.skills[1], fakes.course1)
        mock.assert_called_with(fakes.skills[1], fakes.course1)


class TestGetChallengesData(TestCase):
    def test_empty_skill(self):
        assert get_challenges_data(fakes.emptySkill, fakes.course1) == []

    @patch('liblili2json.get_phrase_challenges')
    def test_generates_phrase_challenges_correctly(self, mock):
        get_challenges_data(fakes.skillWithPhrase, fakes.course1)
        mock.assert_called_with(fakes.phrase2, fakes.course1)

    @patch('liblili2json.get_phrase_challenges')
    def test_includes_every_phrase(self, mock):
        get_challenges_data(fakes.skillWith3Phrases, fakes.course1)
        assert mock.call_count == 3

    @patch('liblili2json.get_word_challenges')
    def test_generates_word_challenges_correctly(self, mock):
        get_challenges_data(fakes.skillWithWord, fakes.course1)
        mock.assert_called_with(fakes.word1, fakes.course1)

    @patch('liblili2json.get_word_challenges')
    def test_includes_every_word(self, mock):
        get_challenges_data(fakes.skillWith3Words, fakes.course1)
        assert mock.call_count == 3

    @patch('liblili2json.get_word_challenges')
    @patch('liblili2json.get_phrase_challenges')
    def test_returns_correct_challenges(self, mock1, mock2):

        mock1.return_value = [fakes.challenge1, fakes.challenge2]
        mock2.return_value = [fakes.challenge3, fakes.challenge4]
        assert get_challenges_data(fakes.skillWithPhraseAndWord, fakes.course1) == [
            fakes.challenge1, fakes.challenge2, fakes.challenge3, fakes.challenge4]


class TestGetWordChallenges(TestCase):
    @patch('liblili2json.get_cards_challenge')
    def test_includes_cards_challenges(self, mock):
        fake_value = fakes.fake_value()
        mock.return_value = fake_value
        assert get_word_challenges(fakes.word1, fakes.course1)[0] == fake_value

    @patch('liblili2json.get_short_input_challenge')
    def test_includes_short_input_challenges(self, mock):
        fake_value = fakes.fake_value()
        mock.return_value = fake_value
        assert get_word_challenges(fakes.word1, fakes.course1)[1] == fake_value

    @patch('liblili2json.get_listening_challenge')
    def test_includes_listening_challenge(self, mock):
        fake_value = fakes.fake_value()
        mock.return_value = fake_value
        assert get_word_challenges(fakes.word1, fakes.course1)[2] == fake_value


class TestGetCardsChallenge(TestCase):
    def test_returns_correct_value1(self):
        challenge = get_cards_challenge(fakes.word1, fakes.course1)
        assert challenge == {
            'id': '9287bb2f7029',
            "type": "cards",
            "formInTargetLanguage": "foous",
            "meaningInSourceLanguage": "foo",
            "priority": 0,
            'group': 'b95c785ddf3e',
            'pictures': ['foo', 'bar', 'baz']
        }

    def test_returns_correct_value2(self):
        challenge = get_cards_challenge(fakes.word2, fakes.course1)
        assert challenge == {
            'id': '91877ee773d8',
            "type": "cards",
            "formInTargetLanguage": "apfel",
            "meaningInSourceLanguage": "apple",
            "priority": 0,
            'group': 'f2b9d8b7c65a',
            'pictures': ['1', '2', '3']
        }


class TestGetShortInputChallenge(TestCase):
    def test_returns_correct_value1(self):
        challenge = get_short_input_challenge(fakes.word1, fakes.course1)
        assert challenge == {
            'id': '98eca012f981',
            "type": "shortInput",
            "formInTargetLanguage": "foous",
            "phrase": "foo",
            "priority": 1,
            'group': 'b95c785ddf3e',
        }

    def test_returns_correct_value2(self):
        challenge = get_short_input_challenge(fakes.word2, fakes.course1)
        assert challenge == {
            'id': '1a196242f155',
            "type": "shortInput",
            "formInTargetLanguage": "apfel",
            "phrase": "apple",
            "priority": 1,
            'group': 'f2b9d8b7c65a',
        }


class TestListeningChallenge(TestCase):
    def test_returns_correct_value1(self):
        challenge = get_listening_challenge(fakes.word1, fakes.course1)
        assert challenge == {
            'id': '3103322a15da',
            "type": "listeningExercise",
            "answer": "foous",
            "meaning": "foo",
            "priority": 1,
            'group': 'b95c785ddf3e',
            'audio': 'b8975c2df0e621d68c96bf1620389a1ae04bc4514aeff6f7a36131daf51f0c62'
        }

    def test_returns_correct_value2(self):
        challenge = get_listening_challenge(fakes.word2, fakes.course1)
        assert challenge == {
            'id': '9fc6514922a6',
            "type": "listeningExercise",
            "answer": "apfel",
            "meaning": "apple",
            "priority": 1,
            'group': 'f2b9d8b7c65a',
            'audio': '509a5b154ef93cd2abac6b6d673f80ded6cd2319902a8d83f15f98c8aaf1cabb'
        }
