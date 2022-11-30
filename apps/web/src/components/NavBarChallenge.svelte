<script lang="typescript">
  import { stores } from '@sapper/app';
  import NavBar from "lluis/NavBar/NavBar.svelte"
  import Icon from "lluis/Icon.svelte"
  import Logo from "lluis/Logo.svelte"
  import Button from "lluis/Button.svelte"
  import NavBarButtonSet from "lluis/NavBar/NavBarButtonSet.svelte"

  const { page } = stores();
  const homepageLink = $page?.params?.courseName
    ? `course/${$page.params.courseName}/`
    : "/";
</script>

<NavBar data-test="navbar">
  <div slot="left" class="navbar__logo navbar__logo--icon">
    <Logo src="/images/logo-icon.svg" alt="LibreLingo" />
  </div>

  <div slot="middle" class="navbar__middle">
    <!-- TODO: Move from ChallengeScreen -->
    <progress class="progress navbar__progress" value="" max=""></progress>
  </div>

  <div slot="right" class="navbar__nav">
    <NavBarButtonSet>
      <Button href={homepageLink} ariaLabel="Cancel" style="linkButton">
        <Icon icon="xmark" size="large" />
      </Button>
    </NavBarButtonSet>
  </div>
</NavBar>
