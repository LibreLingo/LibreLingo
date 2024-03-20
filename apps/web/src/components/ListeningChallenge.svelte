<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import levenshtein from "js-levenshtein"
  import ChallengePanel from "./ChallengePanel.svelte"
  import Icon from "lluis/Icon.svelte"
  import InputFieldWithVirtualKeyboard from "./InputFieldWithVirtualKeyboard/index.svelte"
  import { playAudio } from "../media/sound"
  import Button from "lluis/DeprecatedButton.svelte"
  import Column from "lluis/Column.svelte"
  import Columns from "lluis/Columns.svelte"
  import { t } from 'svelte-i18n'

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
  <div class="section">
    <p class="is-size-1 is-size-2-tablet is-size-4-mobile has-text-centered">
      {$t('listening_challenge.type_what_you_hear')}
    </p>
  </div>

  <Columns>
    <Column size="1">
      <Button size="large" style="primary" on:click="{playChallengeVoice}">
        <Icon icon="volume-up" />
      </Button>
    </Column>
    <Column>
      <InputFieldWithVirtualKeyboard
        specialCharacters="{specialCharacters}"
        languageCode="{languageCode}"
        disabled="{submitted}"
        bind:value="{answer}"
      />
    </Column>
  </Columns>

  {#if answer && !submitted}
    <ChallengePanel
      message=""
      buttonText={$t('listening_challenge.submit')}
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
        message={$t('listening_challenge.incorrect_solution')}
        messageDetail="{`${$t('listening_challenge.correct_answer')} ${challenge.answer}`}"
        buttonText={$t('listening_challenge.continue')}
        incorrect
        buttonAction="{finishChallenge}"
      />
    {/if}

    {#if correct}
      {#if !spellingSuggestion}
        <ChallengePanel
          message={$t('listening_challenge.correct_solution')}
          messageDetail="{`${$t('listening_challenge.meaning')} "${challenge.meaning}"`}"
          buttonText={$t('listening_challenge.continue')}
          correct
          buttonAction="{finishChallenge}"
        />
      {/if}

      {#if spellingSuggestion}
        <ChallengePanel
          message={$t('listening_challenge.you_have_a_typo')}
          messageDetail="{spellingSuggestion ||
            `${$t('listening_challenge.meaning')} "${challenge.meaning}"`}"
          buttonText={$t('listening_challenge.continue')}
          typo
          buttonAction="{finishChallenge}"
        />
      {/if}
    {/if}
  {/if}
</form>
