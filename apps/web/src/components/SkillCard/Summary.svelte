<script lang="ts">
  import ClampedText from "lluis/ClampedText.svelte"

  export let summary: Array<string>
  export let stale: boolean
  export let completed: boolean
</script>

<div class="skill-card__summary" class:is-completed={completed} class:is-stale={stale}>
  <ClampedText text="{`Learn: ${summary.join(', ')}`}" />
</div>
