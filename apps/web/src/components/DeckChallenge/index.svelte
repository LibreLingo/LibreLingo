<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import OptionDeck from "./OptionDeck.svelte"
  import ChallengePanel from "../ChallengePanel.svelte"
  import { prepareChallenge } from "../../logic"

  export let currentChallenge
  export let alternativeChallenges
  export let resolveChallenge
  export let registerResult
  export let skipChallenge
  export let skipAllChallenges

  let selectedOption = null
  let submitted = false

  $: options = prepareChallenge({
      currentChallenge,
      alternativeChallenges,
      typeToSelect: "cards",
      hasFakeOption: true,
  })

  $: finishChallenge = () => {
      selectedOption = null
      submitted = false
      resolveChallenge()
  }

  $: submitChallenge = () => {
      registerResult(options[selectedOption].correct)
      submitted = true
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

<h1 class="challenge-prompt">
  Which of these is
  <b class="challenge-prompt__phrase" data-test="meaning-in-source-language">{currentChallenge.meaningInSourceLanguage}</b>?
</h1>

<form on:submit|preventDefault="{submitChallenge}">
  <OptionDeck {options} bind:selectedOption disabled="{submitted}" />

  {#if selectedOption === null && !submitted}
    <ChallengePanel
      message="{null}"
      buttonText="{null}"
      skipAction="{skipChallenge}"
      skipAllAction="{skipAllChallenges}" />
  {/if}

  {#if !submitted && selectedOption !== null}
    <ChallengePanel
      message=""
      buttonText="Submit"
      submit
      skipAction="{skipChallenge}"
      skipAllAction="{skipAllChallenges}" />
  {/if}

  {#if submitted}
    {#if options[selectedOption].correct}
      <ChallengePanel
        message="Correct!"
        buttonText="Continue"
        correct
        buttonAction="{finishChallenge}" />
    {/if}
    {#if !options[selectedOption].correct}
      <ChallengePanel
        message="Incorrect!"
        buttonText="Continue"
        incorrect
        buttonAction="{finishChallenge}" />
    {/if}
  {/if}
</form>
