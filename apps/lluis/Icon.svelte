<script lang="ts">
  export let size = "medium"
  export let prefix = "fas"
  export let icon: string
</script>

<span class={`icon icon--${size}`}>
  <i class={`${prefix} fa-${icon} ${size === "large" ? "fa-2x" : ""}`} />
</span>

<style>
  .icon {
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
