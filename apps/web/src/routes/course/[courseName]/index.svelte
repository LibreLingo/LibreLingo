<script lang="ts" context="module">
  export async function preload(page) {
      const { get_course } = await import("../../../course-client")
      const { courseName } = page.params

      return await get_course({ courseName })
  }
</script>

<script lang="ts">
  import SkillCard from "../../../components/SkillCard/index.svelte"
  import NavBar from "../../../components/NavBar.svelte"
  import Footer from "lluis/Footer.svelte"
  import type { ModulesType } from "../../../types/ModulesType"

  export let courseName = null
  export let modules: ModulesType = null
  export let languageName = null
  export let repositoryURL = null
</script>

<svelte:head>
  <title>LibreLingo - learn {languageName} for free</title>
</svelte:head>

<NavBar hasAuth repositoryURL="{repositoryURL}" />

<main class="main-content container-md grid">
  <h1 class="h5 m-bottom-1">{languageName}</h1>
  {#each modules as { title, skills }}
    <h2>{title}</h2>
    <ul class="skill-cards">
      {#each skills as skill}
        <li>
          <SkillCard
            {...{ ...skill }}
            practiceHref="{`/course/${courseName}/skill/${skill.practiceHref}`}"
          />
        </li>
      {/each}
    </ul>
  {/each}
</main>

<Footer />
