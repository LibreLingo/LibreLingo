<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import shuffle from "lodash.shuffle"
  import OptionCard from "./OptionCard.svelte"
  export let options
  export let selectedOption
  export let disabled

  // determines which keys correspond to which card
  // skips a number for the fake item (i. e. invisible on desktop)
  let keymap = options.reduce(
      (acc, item) => [...acc, (acc.slice(-1)[0] || 0) + (item.fake ? 2 : 1)],
      []
  )

  onMount(() => {
      hotkeys.unbind("1,2,3")
      hotkeys("1,2,3", (_, { key }) => {
          if (disabled) return
          selectedOption = keymap[parseInt(key) - 1] - 1
      })
  })
</script>

<ul class="challenge-option-deck">
  {#each options as { pictures, formInTargetLanguage, correct, fake }, i}
    <li
      class:is-fake="{fake && true}"
      class:is-real="{!(fake && true)}"
    >
      <label
        for="{i.toString()}"
      >
        <input
          type="radio"
          class="challenge-option-deck__input"
          bind:group="{selectedOption}"
          value="{i}"
          name="{i.toString()}"
          id="{i.toString()}"
          disabled="{disabled}"
        />
        <OptionCard
          correct="{correct}"
          active="{selectedOption === i}"
          inactive="{selectedOption !== null && selectedOption !== i}"
          picture="{shuffle(pictures)[0]}"
          number="{i + 1 - (keymap[i] - i) + 1}"
          formInTargetLanguage="{formInTargetLanguage}"
        />
      </label>
    </li>
  {/each}
</ul>
