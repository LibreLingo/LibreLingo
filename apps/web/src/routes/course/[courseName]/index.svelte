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
  import Column from "lluis/Column.svelte"
  import Columns from "lluis/Columns.svelte"
  import Content from "lluis/Content.svelte"
  import Footer from "lluis/DeprecatedFooter.svelte"
  import type { ModulesType } from "../../../types/ModulesType"
  import { t } from 'svelte-i18n'

  export let courseName = null
  export let modules: ModulesType = null
  export let languageName = null
  export let repositoryURL = null
  export let uiLanguage = "es"

  locale.set(uiLanguage)
</script>

<svelte:head>
  <title>{$t('about.meta.librelingo_learn')} {languageName} {$t('about.meta.for_free')}</title>
</svelte:head>

<NavBar hasAuth {repositoryURL} />

{#each modules as { title, skills }}
  <section class="section">
    <div class="container">
      <h2 class="is-size-2">{title}</h2>
      <Columns multiline>
        {#each skills as skill}
          <Column sizeDesktop="1/3" sizeTablet="1/2">
            <SkillCard
              {...{ ...skill }}
              practiceHref={`/course/${courseName}/skill/${skill.practiceHref}`}
            />
          </Column>
        {/each}
      </Columns>
    </div>
  </section>
{/each}

<Footer>
  <Content>
    <Columns>
      <Column>
        <strong>LibreLingo</strong>
        by
        <a href="https://github.com/kantord">Dániel Kántor</a>
        and
        <a href="https://github.com/LibreLingo/LibreLingo#contributors">
          various contributors
        </a>
        .
      </Column>
      <Column>
        The source code is licensed
        <a href="https://opensource.org/licenses/AGPL-3.0">AGPL-3.0.</a>
        <br />
        <a href="https://github.com/LibreLingo/LibreLingo">
          Source code available on GitHub.
        </a>
      </Column>
      <Column />
    </Columns>
    <p />
  </Content>
</Footer>

<style type="text/scss">
  @import "../../../variables";
  .container {
    padding-right: 20px;
    padding-left: 20px;
  }
</style>
