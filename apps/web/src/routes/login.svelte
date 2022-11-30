<script lang="ts">
  // TODO: deal with this ignore comment
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  import db from "../db/db.js"
  import NavBar from "../components/NavBar.svelte"
  import Button from "lluis/Button.svelte"
  import FormField from "lluis/FormField.svelte"

  let error: string | null = null
  let username = ""
  let password = ""

  type WindowWithLogin = Window & {
    _Login: (username: string, password: string) => Promise<void>
  }

  const handleLogin = async () => {
      try {
          await (window as unknown as WindowWithLogin)._Login(username, password)
      } catch (e) {
          error = e
      }
  }
</script>

<svelte:head>
  <title>Log in - LibreLingo</title>
</svelte:head>

<NavBar hasAuth />

<main class="main-content container-sm grid">
  <h1>Log in</h1>
  <form on:submit|preventDefault="{handleLogin}" class="form grid">
    <FormField
      name="Username"
      id="username"
      bind:value="{username}"
    />

    <FormField
      name="Password"
      id="password"
      type="password"
      bind:value="{password}"
    />

    {#if error !== null}
      <p class="form__error">{error}</p>
    {/if}

    <Button on:click="{handleLogin}" type="submit">Log in</Button>
  </form>
</main>
