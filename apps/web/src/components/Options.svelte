<script lang="ts">
  import { onMount } from "svelte"
  import hotkeys from "hotkeys-js"
  import Option from "../components/Option.svelte"
  export let options
  export let selectedOption
  export let disabled

  onMount(() => {
      hotkeys.unbind("1,2,3")
      hotkeys("1,2,3", (_, { key }) => {
          if (disabled) return
          selectedOption = parseInt(key) - 1
      })
  })
</script>

<ul class="challenge-options">
  {#each options as { formInTargetLanguage, correct, fake }, i}
    <li
      class:is-fake="{fake && true}"
    >
      <label for="{i.toString()}">
        <input
          type="radio"
          class="challenge-options__input"
          bind:group="{selectedOption}"
          value="{i}"
          name="{i.toString()}"
          id="{i.toString()}"
          disabled="{disabled}"
        />
        <Option
          correct="{correct}"
          active="{selectedOption === i}"
          inactive="{selectedOption !== null && selectedOption !== i}"
          formInTargetLanguage="{formInTargetLanguage}"
        />
      </label>
    </li>
  {/each}
</ul>
