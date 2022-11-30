<script lang="typescript">
  export let state: "default" | "success" | "failure" | "info" = "default"
</script>

<div class="container-md panel" data-state={state}>
  <div class="panel__content">
    <slot name="left" />
    <slot name="right" />
  </div>
</div>
