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
  import { t } from 'svelte-i18n'

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
  <div class="section">
    <p class="is-size-1 is-size-2-tablet is-size-4-mobile has-text-centered">
      {$t('short_input_challenge.type')}
      <Phrase phrase="{challenge.phrase}" />
      {$t('short_input_challenge.in')}
      {languageName}!
    </p>
  </div>
  <Columns>
    <Column>
      <InputFieldWithVirtualKeyboard
        specialCharacters="{specialCharacters}"
        languageCode="{languageCode}"
        disabled="{submitted}"
        bind:value="{answer}"
      />
    </Column>
    <Column>
      <div class="card">
        <div class="card-image">
          <figure class="image is-1by1">
            <img
              src="images/{picture}"
              alt=""
              data-test="short text input illustrations"
            />
          </figure>
        </div>
      </div>
    </Column>
  </Columns>

  {#if answer && !submitted}
    <ChallengePanel
      message=""
      buttonText={$t('short_input_challenge.submit')}
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
        message={$t('short_input_challenge.incorrect_solution')}
        messageDetail="{`${$t('short_input_challenge.correct_answer')} ${challenge.formInTargetLanguage[0]}`}"
        buttonText={$t('short_input_challenge.continue')}
        incorrect
        buttonAction="{finishChallenge}"
      />
    {/if}
    {#if correct}
      {#if !spellingSuggestion}
        <ChallengePanel
          message={$t('short_input_challenge.correct_solution')}
          messageDetail=""
          buttonText={$t('short_input_challenge.continue')}
          correct
          buttonAction="{finishChallenge}"
        />
      {/if}

      {#if spellingSuggestion}
        <ChallengePanel
          message={$t('short_input_challenge.you_have_a_typo')}
          messageDetail="{spellingSuggestion}"
          buttonText={$t('short_input_challenge.continue')}
          typo
          buttonAction="{finishChallenge}"
        />
      {/if}
    {/if}
  {/if}
</form>

<style type="text/scss">
  .card {
    max-width: 16em;
    margin: auto;
  }
</style>
