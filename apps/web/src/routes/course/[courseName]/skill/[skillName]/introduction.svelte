<script lang="ts" context="module">
  import { _ } from "svelte-i18n"
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
  import Button from "lluis/Button.svelte"
  import MarkDownPage from "../../../../../components/MarkDownPage.svelte"
  import isBrowser from "../../../../../utils/isBrowser"

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
  <MarkDownPage {readmeHTML} {title} description={$_("about.meta.description")}>
    <div class="buttonset m-top-1 m-bottom-2">
      <Button
        style="secondary"
        href={`course/${courseName}`}
        >Go back to the course</Button
      >
      <Button
        style="primary"
        href={`course/${courseName}/skill/${practiceHref}`}
        >Practice {title}</Button
      >
    </div>
  </MarkDownPage>
{/if}
