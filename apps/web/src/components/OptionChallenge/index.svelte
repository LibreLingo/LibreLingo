<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import Options from "../Options.svelte"
  import ChallengePanel from "../ChallengePanel.svelte"
  import { prepareChallenge } from "../../logic"
    import { playAudio } from "../../media/sound"

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
      typeToSelect: "options",
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

  $: if (selectedOption != null) {
    playAudio('voice', options[selectedOption].audio);
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

<p class="is-size-1 is-size-2-tablet is-size-4-mobile has-text-centered">
  Which of these is
  <strong data-test="meaning-in-source-language">
    {currentChallenge.meaningInSourceLanguage}
  </strong>
  ?
</p>

<form on:submit|preventDefault="{submitChallenge}">
  <Options {options} bind:selectedOption disabled="{submitted}" />

  {#if !submitted && selectedOption !== null}
    <ChallengePanel
      message=""
      buttonText="Submit"
      submit
      skipAction="{skipChallenge}"
      skipAllAction="{skipAllChallenges}" />
  {/if}

  {#if !submitted && selectedOption === null}
    <ChallengePanel message="" buttonText="" skipAction="{skipChallenge}" skipAllAction="{skipAllChallenges}" />
  {/if}

  {#if submitted}
    {#if options[selectedOption].correct}
      <ChallengePanel
        message="Correct solution!"
        buttonText="Continue"
        correct
        buttonAction="{finishChallenge}" />
    {/if}
    {#if !options[selectedOption].correct}
      <ChallengePanel
        message="Incorrect solution!"
        messageDetail="{`Correct answer: ${currentChallenge.formInTargetLanguage}`}"
        buttonText="Continue"
        incorrect
        buttonAction="{finishChallenge}" />
    {/if}
  {/if}
</form>
