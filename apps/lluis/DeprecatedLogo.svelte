<script lang="ts">
  export let src: string
  export let alt: string
  export let link: string
</script>

<a href={link} class="logo">
  <img {src} {alt} />
</a>

<style type="text/scss">
  .logo {
    display: block;

    img {
      height: var(--deprecated-navbar-logo-height);
    }
  }
</style>
