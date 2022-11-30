<script lang="ts">
  export let status
  export let error

  const dev = process.env.NODE_ENV === "development"
</script>

<svelte:head>
  <title>{status}</title>
</svelte:head>

<main class="main-content flex-j-center">
  <div class="container-md">
    <h1>{status}</h1>
    <p>{error.message}</p>
    {#if dev && error.stack}
      <pre>{error.stack}</pre>
    {/if}
    <p class="m-top-1">
      —<br>
      <a href="/">LibreLingo Home</a>
    </p>
  </div>
</main>
