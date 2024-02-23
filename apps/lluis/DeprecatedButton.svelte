<script lang="ts">
  import { createEventDispatcher } from "svelte"
  import LinkOrButton from "./primitives/LinkOrButton.svelte"
  import Icon from "lluis/Icon.svelte"
  import Stack from "lluis/Stack.svelte"

  const dispatch = createEventDispatcher()
  export let href: string | null = null
  export let size: "small" | "normal" | "medium" | "large" = "normal"
  export let loading = false
  export let asHref: string | null = null
  export let type: "button" | "submit" = "button"
  export let style: "primary" | "secondary" | "key" = "secondary"
  export let target: string | undefined = undefined
  export let tabIndex: number | undefined = undefined
  export let disabled = false
</script>

<div
  class="lluis-button"
  class:small={size === "small"}
  class:large={size === "large"}
  data-style={style}
>
  <LinkOrButton
    {href}
    on:click={() => dispatch("click")}
    {type}
    {target}
    {tabIndex}
    {disabled}
  >
    {#if loading}
      <span class="spinner">
        <Icon icon="spinner" />
      </span>
    {:else}
      <Stack>
        <div slot="icon-left" />
        <slot />
      </Stack>
    {/if}
  </LinkOrButton>
</div>

{#if asHref != null}
  <a class="hidden-link" href={asHref}>&nbsp;</a>
{/if}

<style type="text/scss">
  @keyframes spinner {
    to {
      transform: rotate(360deg);
    }
  }

  .lluis-button {
    display: inline-block;
    max-width: 100%;
  }

  div > :global(*) {
    display: inline-block;
    border-radius: var(--deprecated-button-radius-small);
    padding: 6px 20px;
    margin: 4px;
    transition-property: filter;
    transition-duration: 0.1s;
    transition-timing-function: ease-in-out;

    :global(.icon) {
      width: unset;
      height: unset;
      margin-right: 8px;
    }

    &:hover,
    &:focus {
      filter: brightness(1.2);
    }

    &:active {
      filter: brightness(0.9);
      transform: scale(0.9);
    }

    &:disabled {
      filter: opacity(0.5) saturate(0);
      pointer-events: none;
    }
  }

  .spinner {
    display: flex;
    width: 16px;
    height: 16px;
    align-items: center;
    justify-content: center;
    animation: spinner 0.6s linear infinite;

    :global(.icon) {
      display: block;
      margin: 0 !important;
    }
  }

  div[data-style="primary"] > :global(*) {
    border: 1px solid var(--deprecated-button-primary-border);
    color: var(
      --deprecated-button-primary-text-color
    ) !important; /* TODO: remove when hero is remoevd */
    background-color: var(
      --deprecated-button-primary-background-color
    ) !important;
  }

  div[data-style="secondary"] > :global(*) {
    border: 1px solid var(--deprecated-button-secondary-border);
    color: var(--deprecated-button-secondary-text-color) !important;
    background-color: var(
      --deprecated-button-secondary-background-color
    ) !important;
  }

  div[data-style="key"] > :global(*) {
    margin: 6px;
    padding: 6px 0;
    text-align: center;
    width: calc(1em + 22px);
    border: 1px solid var(--deprecated-button-key-border);
    color: var(--deprecated-button-key-text-color) !important;
    background-color: var(--deprecated-button-key-background-color) !important;
  }

  .small > :global(*) {
    font-size: 16px;
    padding: 3px 12px;
  }

  .medium > :global(*) {
    font-size: 18px;
    padding: 3px 12px;
  }

  .large > :global(*) {
    font-size: 20px;
    padding: 9px 14px;
  }
</style>
