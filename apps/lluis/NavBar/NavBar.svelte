<nav class="navbar" data-test-id="site-navbar">
  <div class="navbar__content container-lg" class:has-middle={$$slots.middle}>
    <slot name="left" />
    {#if $$slots.middle}
      <slot name="middle" />
    {/if}
    <slot name="right" />
  </div>
</nav>

<style>
  .navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 10;
    background-color: var(--navbar-background);
  }
</style>
