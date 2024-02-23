<nav data-test-id="site-navbar">
  <div>
    <slot name="left" />
    {#if $$slots.middle}
      <slot name="middle" />
    {/if}
    <slot name="right" />
  </div>
</nav>

<div />

<style>
  nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 10;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
    padding-left: 3.5em;
    padding-right: 3.5em;
    background-color: var(--navbar-background);
  }

  nav > * {
    max-width: var(--page-max-width);
    margin: auto;
  }

  div {
    height: var(--navbar-height);
  }
</style>
