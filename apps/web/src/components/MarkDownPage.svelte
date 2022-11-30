<script lang="ts">
  import NavBar from "../components/NavBar.svelte"
  import Content from "lluis/Content.svelte"
  import Footer from "lluis/Footer.svelte"

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

<NavBar hasAuth />

<main class="main-content container-md">
  <h1>{title}</h1>
  <slot />
  <Content>
    {@html readmeHTML}
  </Content>
</main>

<Footer />
