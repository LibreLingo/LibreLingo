<script lang="ts">
  // TODO: deal with this ignore comment
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  import db from "../db/db.js"
  import NavBar from "../components/NavBar.svelte"
  import Button from "lluis/Button.svelte"
</script>

<NavBar hasAuth />

<main class="main-content container-sm grid">
  <h1>Registration successful!</h1>
  <p>You can now log in.</p>
  <Button href="/login">Log in</Button>
</main>
