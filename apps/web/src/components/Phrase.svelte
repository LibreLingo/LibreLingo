<script lang="ts">
  export let phrase
</script>

{#each phrase as { word, definition }}
  {#if definition}
    <b class="challenge-prompt__phrase challenge-prompt__phrase--underline" data-tooltip="{definition}" title="{definition}">{word}</b>
  {:else}
    <b class="challenge-prompt__phrase">{word}</b>
  {/if}
{/each}
