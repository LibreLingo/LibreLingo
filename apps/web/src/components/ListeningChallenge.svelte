<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import levenshtein from "js-levenshtein"
  import ChallengePanel from "./ChallengePanel.svelte"
  import Icon from "lluis/Icon.svelte"
  import InputFieldWithVirtualKeyboard from "./InputFieldWithVirtualKeyboard/index.svelte"
  import { playAudio } from "../media/sound"
  import Button from "lluis/Button.svelte"

  export let challenge
  export let registerResult
  export let resolveChallenge
  export let languageCode
  export let specialCharacters
  export let skipChallenge
  export let skipAllChallenges
  export let skipAllVoice

  let answer = ""
  let submitted = false
  let correct = null
  let spellingSuggestion = ""

  $: submitChallenge = () => {
      if (!answer) return
      if (submitted) return
      const form = challenge.answer
      correct = false

      if (
          levenshtein(
              answer
                  .toLowerCase()
                  .replace(/^\s+|\s+$/g, "")
                  .replace(/\s+/g, " "),
              form.toLowerCase()
          ) <= 1
      ) {
          correct = true
          spellingSuggestion =
        form
            .replace(/^\s+|\s+$/g, "")
            .replace(/\s+/g, " ")
            .toLowerCase() === answer.toLowerCase()
            ? ""
            : `Correct spelling: ${form}`
      }

      registerResult(correct)
      submitted = true
  }

  $: finishChallenge = () => {
      answer = null
      submitted = false
      resolveChallenge()
  }

  const playChallengeVoice = () => playAudio("voice", challenge.audio)

  onMount(() => {
      playChallengeVoice()
      hotkeys.unbind("enter")
      hotkeys("enter", () => {
          if (submitted) {
              finishChallenge()
          } else {
              submitChallenge()
          }
      })
  })
</script>

<form on:submit|preventDefault="{submitChallenge}">
  <h1 class="challenge-prompt">Type what you hear</h1>

  <div class="challenge-listening">
    <div class="challenge-listening__button-and-input">
      <Button style="primary" on:click="{playChallengeVoice}">
        <Icon icon="volume-up" />
      </Button>
      <InputFieldWithVirtualKeyboard
        specialCharacters="{specialCharacters}"
        languageCode="{languageCode}"
        disabled="{submitted}"
        bind:value="{answer}"
      />
    </div>

    {#if answer && !submitted}
      <ChallengePanel
        message=""
        buttonText="Submit"
        submit
        skipAction="{skipChallenge}"
        skipAllAction="{skipAllChallenges}"
        skipAllVoice="{skipAllVoice}"
      />
    {/if}

    {#if answer === "" && !submitted}
      <ChallengePanel
        message="{null}"
        buttonText="{null}"
        skipAction="{skipChallenge}"
        skipAllAction="{skipAllChallenges}"
        skipAllVoice="{skipAllVoice}"
      />
    {/if}

    {#if submitted}
      {#if !correct}
        <ChallengePanel
          message="Incorrect!"
          messageDetail="{`Correct answer: ${challenge.answer}`}"
          buttonText="Continue"
          incorrect
          buttonAction="{finishChallenge}"
        />
      {/if}

      {#if correct}
        {#if !spellingSuggestion}
          <ChallengePanel
            message="Correct!"
            messageDetail="{`Meaning: "${challenge.meaning}"`}"
            buttonText="Continue"
            correct
            buttonAction="{finishChallenge}"
          />
        {/if}

        {#if spellingSuggestion}
          <ChallengePanel
            message="You have a typo!"
            messageDetail="{spellingSuggestion ||
              `Meaning: "${challenge.meaning}"`}"
            buttonText="Continue"
            typo
            buttonAction="{finishChallenge}"
          />
        {/if}
      {/if}
    {/if}
  </div>
</form>
