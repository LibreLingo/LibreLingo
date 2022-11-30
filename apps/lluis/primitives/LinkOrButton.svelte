<script lang="ts">
  import { createEventDispatcher } from "svelte"

  const dispatch = createEventDispatcher()
  export let href: string | null = null
  export let type: "button" | "submit" = "button"
  export let target: string | undefined = undefined
  export let tabIndex: number | undefined = undefined
  export let disabled = false
  export let label: string | null = null
</script>

{#if href !== null}
  <a {href} {target} tabindex={tabIndex} {...$$restProps} role="button" aria-label={label}>
    <slot />
  </a>
{/if}

{#if href === null}
  <button
    {type}
    tabindex={tabIndex}
    {disabled}
    on:click={() => dispatch("click")}
    aria-label={label}
    {...$$restProps}
  >
    <slot />
  </button>
{/if}
