<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import shuffle from "lodash.shuffle"
  import ChallengePanel from "./ChallengePanel.svelte"
  import Phrase from "./Phrase.svelte"
  import InputFieldWithVirtualKeyboard from "./InputFieldWithVirtualKeyboard/index.svelte"
  import Column from "lluis/Column.svelte"
  import Columns from "lluis/Columns.svelte"
  import evaluateAnswer from "@librelingo/answer-corrector/src/index"

  export let challenge
  export let registerResult
  export let resolveChallenge
  export let languageName
  export let languageCode
  export let specialCharacters
  export let skipChallenge
  export let skipAllChallenges

  let answer = ""
  let submitted = false
  let correct = null
  let spellingSuggestion = ""
  let picture = shuffle(challenge.pictures)[0]

  $: submitChallenge = () => {
      if (!answer) return
      if (submitted) return

      const validationResults = evaluateAnswer({
          validAnswers: challenge.formInTargetLanguage,
          answer: answer,
      })

      correct = validationResults.correct
      spellingSuggestion = validationResults.suggestion

      registerResult(correct)
      submitted = true
  }

  $: finishChallenge = () => {
      answer = null
      submitted = false
      resolveChallenge()
  }

  onMount(() => {
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
  <h1 class="challenge-prompt">
    Type
    <Phrase phrase="{challenge.phrase}" />
    in
    {languageName}!
  </h1>

  <div class="challenge-short-input">
    <Columns>
      <Column size="8">
        <InputFieldWithVirtualKeyboard
          specialCharacters="{specialCharacters}"
          languageCode="{languageCode}"
          disabled="{submitted}"
          bind:value="{answer}"
        />
      </Column>
      <Column size="4">
        <div class="challenge-short-input__image">
          <img
            src="images/{picture}"
            alt=""
            data-test="short text input illustrations"
          />
        </div>
      </Column>
    </Columns>
  </div>

  {#if answer && !submitted}
    <ChallengePanel
      message=""
      buttonText="Submit"
      submit
      skipAction="{skipChallenge}"
      skipAllAction="{skipAllChallenges}"
    />
  {/if}

  {#if answer === "" && !submitted}
    <ChallengePanel
      message="{null}"
      buttonText="{null}"
      skipAction="{skipChallenge}"
      skipAllAction="{skipAllChallenges}"
    />
  {/if}

  {#if submitted}
    {#if !correct}
      <ChallengePanel
        message="Incorrect!"
        messageDetail="{`Correct answer: ${challenge.formInTargetLanguage[0]}`}"
        buttonText="Continue"
        incorrect
        buttonAction="{finishChallenge}"
      />
    {/if}
    {#if correct}
      {#if !spellingSuggestion}
        <ChallengePanel
          message="Correct!"
          messageDetail=""
          buttonText="Continue"
          correct
          buttonAction="{finishChallenge}"
        />
      {/if}

      {#if spellingSuggestion}
        <ChallengePanel
          message="You have a typo!"
          messageDetail="{spellingSuggestion}"
          buttonText="Continue"
          typo
          buttonAction="{finishChallenge}"
        />
      {/if}
    {/if}
  {/if}
</form>
