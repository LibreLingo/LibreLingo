<script lang="ts" context="module">
  import NavBar from "../components/DeprecatedNavBar.svelte"
  import Title from "lluis/Title.svelte"
  import DeprecatedButton from "../../../lluis/DeprecatedButton.svelte"
  import Button from "lluis/Button.svelte"
</script>

<svelte:head>
  <title>Fonts Visual Guide - LibreLingo</title>
</svelte:head>

<NavBar />
<section class="section">
  <div class="container">
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-8">
        <div class="tile is-parent is-vertical">
          <Title size={2} align="centered">Fonts Visual Guide</Title>
          <article class="tile is-child notification is-primary p-4">
            <Title size={3} textWeight="semibold">Types of headings</Title>
            <Title>Title</Title>
            <Title isSubtitle={true}>Subtitle</Title>
          </article>
          <article class="tile is-child notification is-primary p-4">
            <Title size={3} textWeight="semibold">Sizes</Title>
            <Title size={1}>Title 1</Title>
            <Title size={2}>Title 2</Title>
            <Title size={3}>Title 3</Title>
            <Title size={4}>Title 4</Title>
            <Title size={5}>Title 5</Title>
            <Title size={6}>Title 6</Title>
          </article>
          <div>
            <DeprecatedButton>Click me</DeprecatedButton>
          </div>
          <div>
            <DeprecatedButton size="small">Click me</DeprecatedButton>
          </div>
          <div>
            <DeprecatedButton size="large">Click me</DeprecatedButton>
          </div>
          <div>
            <DeprecatedButton size="small" style="primary"
              >Click me</DeprecatedButton
            >
          </div>
          <div>
            <DeprecatedButton size="large" style="primary"
              >Click me</DeprecatedButton
            >
          </div>
          <div>
            <DeprecatedButton loading style="primary">Click me</DeprecatedButton
            >
          </div>
          <div>
            <Button>Click me</Button>
          </div>
          <div>
            <Button size="small">Click me</Button>
          </div>
          <div>
            <Button size="large">Click me</Button>
          </div>
          <div>
            <Button size="small" style="primary">Click me</Button>
          </div>
          <div>
            <Button size="large" style="primary">Click me</Button>
          </div>
          <div>
            <Button loading style="primary">Click me</Button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");
  body {
    font-family: "Open Sans", sans-serif;
  }
</style>
