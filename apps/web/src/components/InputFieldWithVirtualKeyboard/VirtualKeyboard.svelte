<script lang="ts">
  // Manual test: http://localhost:3000/course/test/skill/short-input-test-3?testChallenge=86665e4f61fa
  import Button from "../../../../lluis/Button.svelte"
  import HorizontalScroller from "../../../../lluis/HorizontalScroller.svelte"

  export let characters: Array<string>
  export let handleVirtualKey
</script>

<div class="virtual-keyboard">
  <HorizontalScroller>
    <slot>
      <div class="virtual-keyboard__keys">
        {#each characters as character}
          <Button
            style="key"
            tabIndex={-1}
            size="small"
            on:click={handleVirtualKey(character)}
          >
            {character}
          </Button>
        {/each}
      </div>
    </slot>
  </HorizontalScroller>
</div>
