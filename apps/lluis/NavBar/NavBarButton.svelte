<script lang="ts">
  import LinkOrButton from "../primitives/LinkOrButton.svelte"
  import { createEventDispatcher } from "svelte"

  const dispatch = createEventDispatcher()
  export let href: string | null = null
  export let target: "_blank" | undefined = undefined
</script>

<div>
  <LinkOrButton href={href} on:click="{() => dispatch('click')}" target={target}>
    <slot />
  </LinkOrButton>
</div>
