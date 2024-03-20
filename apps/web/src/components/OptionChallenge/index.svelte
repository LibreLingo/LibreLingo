<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import Options from "../Options.svelte"
  import ChallengePanel from "../ChallengePanel.svelte"
  import { prepareChallenge } from "../../logic"
  import { t } from 'svelte-i18n'

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
  {$t('option_challenge.which_of_these_is')}
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
      buttonText={$t('option_challenge.submit')}
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
        message={$t('option_challenge.correct_solution')}
        buttonText={$t('option_challenge.continue')}
        correct
        buttonAction="{finishChallenge}" />
    {/if}
    {#if !options[selectedOption].correct}
      <ChallengePanel
        message={$t('option_challenge.incorrect_solution')}
        messageDetail="{`${$t('option_challenge.correct_answer')} ${currentChallenge.formInTargetLanguage}`}"
        buttonText={$t('option_challenge.continue')}
        incorrect
        buttonAction="{finishChallenge}" />
    {/if}
  {/if}
</form>
