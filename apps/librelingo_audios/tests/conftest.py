import json
import subprocess
from types import SimpleNamespace

import pytest


def _mock_hash_for_text(text):
    if text == "lorem ipsum":
        return "7dc37637ce2395ed74d4f6ae0f63e0885536356c8910914d3af8afe05694cab2"

    if text == "foous barus":
        return "0804b0ba52a7fa507998b7f18d6514876195f12dab6cbe7876b924524a1583f6"

    if text == "apfel":
        return "f38b5ac2a5e36c336eed306d56ed517bfd78a728321be0b87db5def8ff8abc3d"

    if text == "foous":
        return "3f981d854531e9f376ae06cb8449a6e997972d3c1b598f9a00b481ef307a469d"

    if text == "an unnecessary phrase":
        return "oldid"

    raise RuntimeError(f"Missing hash mock for '{text}'")


def _mock_audio_file_for_text(text):
    return f"{_mock_hash_for_text(text)}.mp3"


@pytest.fixture
def mock_index_entry():
    return lambda text: {
        "id": _mock_hash_for_text(text),
        "text": text,
        "source": "TTS",
        "license": "foo bar license",
        "ttsProvider": "Polly",
        "ttsVoice": "Lupe",
        "ttsEngine": "standard",
    }


@pytest.fixture
def terminal(tmp_path, capsys):
    def assert_output_matches(set_of_messages):
        assert set(set_of_messages) == {
            line for line in capsys.readouterr().out.split("\n") if line != ""
        }

    return SimpleNamespace(
        assert_output_matches=assert_output_matches,
        # pylint: disable=line-too-long
        message=SimpleNamespace(
            **{
                "generating": lambda text: f"Generating {tmp_path / _mock_audio_file_for_text(text)} using Lupe standard",
                "would_generate": lambda text: f"Would generate {tmp_path / _mock_audio_file_for_text(text)} using Lupe standard",
                "deleting": lambda text: f"Deleting {tmp_path / _mock_audio_file_for_text(text)}",
            }
        ),
    )


@pytest.fixture
def aws_cli(mocker, tmp_path):
    subprocess_run = mocker.patch("subprocess.run")

    def assert_call_count(count):
        assert subprocess_run.call_count == count

    def assert_audio_generated_for(text):
        subprocess_run.assert_any_call(
            [
                "aws",
                "polly",
                "synthesize-speech",
                "--output-format",
                "mp3",
                "--voice-id",
                "Lupe",
                "--engine",
                "standard",
                "--text",
                text,
                tmp_path / _mock_audio_file_for_text(text),
            ],
            stdout=subprocess.DEVNULL,
        )

    return SimpleNamespace(
        **{
            "assert_call_count": assert_call_count,
            "assert_audio_generated_for": assert_audio_generated_for,
        }
    )


@pytest.fixture
def write_mock_audio_file_for_text(tmp_path):
    def write_file(text):
        with open(tmp_path / _mock_audio_file_for_text(text), "w") as f:
            f.write(f"this is a fake audio file for {text}")

    return write_file


@pytest.fixture
def index_file(tmp_path):
    def assert_entries_match(expected_entries):
        with open(tmp_path / "test.json", "r") as f:
            entries = json.loads(f.read())
            assert entries == expected_entries

    def assert_exists():
        assert list(tmp_path.iterdir()) == [tmp_path / "test.json"]

    def assert_does_not_exist():
        assert not list(tmp_path.iterdir())

    def set_entries(entries):
        with open(tmp_path / "test.json", "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, indent=4)

    return SimpleNamespace(
        **{
            "assert_entries_match": assert_entries_match,
            "assert_exists": assert_exists,
            "assert_does_not_exist": assert_does_not_exist,
            "set_entries": set_entries,
        }
    )
