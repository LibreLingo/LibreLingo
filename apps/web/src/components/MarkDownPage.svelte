<script lang="ts">
  import NavBar from "../components/DeprecatedNavBar.svelte"
  import Content from "lluis/Content.svelte"

  export let readmeHTML: string
  export let title: string | null
  export let description: string | null = null
</script>

<svelte:head>
  <title>{title}</title>
  {#if description}
    <meta name="description" content="{description}" />
  {/if}
</svelte:head>

<NavBar />

<section class="hero is-primary md-page">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">{title}</h1>
      <div class="section box">
        <slot />
        <Content>
          {@html readmeHTML}
        </Content>
      </div>
    </div>
  </div>
</section>
