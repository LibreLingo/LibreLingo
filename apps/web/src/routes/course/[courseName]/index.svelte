<script lang="ts" context="module">
  export async function preload(page) {
    const { get_course } = await import("../../../course-client")
    const { courseName } = page.params

    return await get_course({ courseName })
  }
</script>

<script lang="ts">
  import { locale } from "svelte-i18n"
  import SkillCard from "../../../components/SkillCard/index.svelte"
  import NavBar from "../../../components/NavBar.svelte"
  import Footer from "lluis/Footer.svelte"
  import Page from "lluis/Page.svelte"
  import type { ModulesType } from "../../../types/ModulesType"
  import Heading from "../../../../../lluis/Heading.svelte"
  import Stack from "../../../../../lluis/Stack.svelte"

  export let courseName = null
  export let modules: ModulesType = null
  export let languageName = null
  export let uiLanguage = "es"

  locale.set(uiLanguage)
</script>

<svelte:head>
  <title>LibreLingo - learn {languageName} for free</title>
</svelte:head>

<Page>
  <NavBar />
  {#each modules as { title, skills }}
    <section class="section">
      <div class="container">
        <Heading level={2}>{title}</Heading>
        <Stack direction="row" wrap spacing="m">
          {#each skills as skill}
            <SkillCard
              {...{ ...skill }}
              practiceHref={`/course/${courseName}/skill/${skill.practiceHref}`}
            />
          {/each}
        </Stack>
      </div>
    </section>
  {/each}
  <Footer />
</Page>
