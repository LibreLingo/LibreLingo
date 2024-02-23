<script lang="ts">
  // TODO: deal with this ignore comment
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  import db from "../db/db.js"
  import NavBar from "../components/DeprecatedNavBar.svelte"
  import Button from "lluis/DeprecatedButton.svelte"
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

<NavBar />

<section class="section">
  <div class="container">
    <form on:submit|preventDefault="{handleLogin}">
      <h2 class="is-size-2">Log in</h2>

      <FormField
        name="Username"
        icon="user"
        id="username"
        bind:value="{username}"
      />

      <FormField
        name="Password"
        icon="lock"
        id="password"
        type="password"
        bind:value="{password}"
      />

      {#if error !== null}
        <p class="help is-danger">{error}</p>
      {/if}

      <Button on:click="{handleLogin}" type="submit">Log in</Button>
    </form>
  </div>
</section>
