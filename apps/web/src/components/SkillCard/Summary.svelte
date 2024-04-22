<script lang="ts">
  import ClampedText from "lluis/ClampedText.svelte"
  import { t } from "svelte-i18n"

  export let summary: Array<string>
  export let stale: boolean
  export let completed: boolean
</script>

<div class:completed class:stale>
  <ClampedText text="{`${$t("summary.learn")} ${summary.join(', ')}`}" />
</div>

<style type="text/scss">
  @import "../../variables";

  .completed,
  .stale {
    color: $white;
  }
</style>
