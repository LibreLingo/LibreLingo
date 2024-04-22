<script lang="ts" context="module">
  import { get_skill_introduction } from "../../../../../course-client"

  export async function preload(page) {
    const { courseName, skillName } = page.params

    if (courseName === "preview") {
      const gistId = page.query.gistId
      const skillNameFromQuery = page.query.skillName

      return {
        loading: true,
        preview: {
          type: skillName,
          gistId,
          skillName: skillNameFromQuery,
        },
      }
    }

    return {
      ...(await get_skill_introduction({ courseName, skillName })),
      loading: false,
      preview: null,
    }
  }
</script>

<script lang="ts">
  import Button from "lluis/DeprecatedButton.svelte"
  import MarkDownPage from "../../../../../components/MarkDownPage.svelte"
  import isBrowser from "../../../../../utils/isBrowser"
  import { t } from "svelte-i18n"

  export let preview = null
  export let loading = true
  export let readmeHTML: string
  export let title: string
  export let practiceHref: string
  export let courseName: string

  // Fetching preview data
  if (preview !== null) {
    let gistParams = preview.gistId
    if (isBrowser()) {
      const urlSearchParams = new URLSearchParams(window.location.search)
      gistParams = Object.fromEntries(urlSearchParams.entries())
    }

    const { skillName, gistId } = gistParams

    get_skill_introduction({ courseName: "preview", skillName, gistId }).then(
      (skillData) => {
        title = skillData.title
        readmeHTML = skillData.readmeHTML
        practiceHref = skillData.practiceHref
        loading = false
      }
    )
  }
</script>

{#if !loading}
  <MarkDownPage {readmeHTML} {title} description={$t("about.meta.description")}>
    <div>
      <Button
        style="secondary"
        href={`course/${courseName}`}
        >{$t("about.meta.go_back_to_the_course")}</Button
      >
      <Button
        style="primary"
        href={`course/${courseName}/skill/${practiceHref}`}
        >{$t("about.meta.practice")} {title}</Button
      >
    </div>
  </MarkDownPage>
{/if}

<style>
  div {
    margin-bottom: var(--spacing-large);
  }
</style>
