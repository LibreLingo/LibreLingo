<script lang="ts" context="module">
  import NavBar from "../components/NavBar.svelte"
  import Content from "lluis/Content.svelte"
  import Stack from "lluis/Stack.svelte"
  import Button from "../../../lluis/Button.svelte"

  const buttonStyles = ["primary", "secondary", "accent", "key", "linkButton"]
  const buttonSizes = ["small", "medium", "large"]
  const buttonSelectors = [null, "active", "hover"]
</script>

<svelte:head>
  <title>Fonts Visual Guide - LibreLingo</title>
</svelte:head>

<NavBar hasAuth />

<main class="main-content container-md">
  <Content>
    <h1>Fonts Visual Guide</h1>
    <hr>
    <h2>Sizes</h2>
    <div class="h1">Title 1</div>
    <div class="h2">Title 2</div>
    <div class="h3">Title 3</div>
    <div class="h4">Title 4</div>
    <div class="h5">Title 5</div>
    <div class="h6">Title 6</div>
    <hr>
    <h2>Buttons</h2>
    {#each buttonStyles as buttonStyle}
      <h3>{buttonStyle} style</h3>
      {#each buttonSelectors as buttonSelector}
      <h4>{buttonSelector || "normal"}</h4>
      <Stack>
        {#each buttonSizes as buttonSize}
          <Stack>
            <Button size={buttonSize} style={buttonStyle}>Click me</Button>
          </Stack>
          <Stack>
            <Button loading size={buttonSize} style={buttonStyle}>Click me</Button>
          </Stack>
        {/each}
          </Stack>
      {/each}
    {/each}
  </Content>
</main>
