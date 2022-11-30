<script lang="ts">
  import { tweened } from "svelte/motion"

  export let value

  const progress = tweened(0)
  $: progress.set(value)
</script>

<progress class="progress" value="{$progress}" max="1">
  {$progress * 100}%
</progress>
