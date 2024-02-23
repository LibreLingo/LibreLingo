<script lang="ts">
  import { stores } from "@sapper/app"
  import NavBar from "lluis/NavBar/NavBar.svelte"
  import Logo from "lluis/Logo.svelte"

  export let dark = false
  let logoURL = dark === true ? "/images/logo.svg" : "/images/logo-dark.svg"

  const { page } = stores()

  const homepageLink = $page?.params?.courseName
    ? `course/${$page.params.courseName}/`
    : "/"
</script>

<NavBar>
  <div slot="left">
    <Logo src={logoURL} alt="LibreLingo" link={homepageLink} />
  </div>
</NavBar>

<style>
  div {
    height: 100%;
  }
</style>
