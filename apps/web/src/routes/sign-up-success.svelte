<script lang="ts">
  // TODO: deal with this ignore comment
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  import db from "../db/db.js"
  import NavBar from "../components/DeprecatedNavBar.svelte"
  import Button from "lluis/DeprecatedButton.svelte"
</script>

<NavBar />

<section class="section">
  <div class="container">
    <h2 class="is-size-2">Registration successful!</h2>
    <p>You can now log in.</p>
    <Button href="/login">Log in</Button>
  </div>
</section>
