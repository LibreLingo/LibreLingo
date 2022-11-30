<script>
  import Icon from "./Icon.svelte"
</script>

<span class="spinner">
  <Icon icon="spinner" ref="icon" />
</span>

<style>
  .spinner {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    animation: spinner 0.6s linear infinite;
  }

  :global([ref="icon"]) {
    display: block;
    margin: 0 !important;
  }
</style>
