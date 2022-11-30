<script lang="ts">
  import Icon from "lluis/Icon.svelte"

  export let name: string
  export let id: string
  export let icon: string
  export let type = "text"
  export let value: string | boolean | number
  export let formStatus = {}
  let error = null
  $: {
    error = formStatus[id]
  }
</script>

<div class="form-field" class:has-error={error != null}>
  <label class="form-field__label" for={id}>{name}</label>
  <div class="form-field__control" class:has-icon={icon != null}>
    {#if icon}
      <Icon size="small" {icon} />
    {/if}
    {#if type === "text"}
      <input class="input" type="text" name={id} {id} bind:value />
    {/if}
    {#if type === "password"}
      <input class="input" type="password" name={id} {id} bind:value />
    {/if}
  </div>
  {#if error != null}
    <div class="form-field__help">{error}</div>
  {/if}
</div>
