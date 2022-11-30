<script lang="ts">
  import { onMount } from "svelte"

  import live from "../../db/live"
  import getSkillStats from "../../db/skill/getSkillStats"
  import ContentLeft from "./ContentLeft.svelte"
  import ContentCenter from "./ContentCenter.svelte"

  export let title: string
  export let levels: number
  export let practiceHref: string
  export let introduction: string
  export let id: string
  export let imageSet: string[] = []
  export let summary: string

  let completed = null
  let started = null
  let stale = null
  let progress = null
  let introductionPageHref = introduction
    ? `${practiceHref}/introduction`
    : null
  let backgroundColor = "white"
  let foregroundColor = "black"

  $: {
    backgroundColor = (() => {
      if (stale) return "var(--panel-background-failure)"
      if (completed) return "var(--panel-background-success)"
      return "white"
    })()
  }

  $: {
    foregroundColor = (() => {
      if (completed) return "white"
      if (stale) return "white"
      return "black"
    })()
  }

  onMount(() => {
    live((db) =>
      getSkillStats(db, { id })
        .then((stats) => {
          completed = stats.progress >= levels
          progress = stats.progress
          started = stats.started
          stale = stats.stale && completed
        })
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        .catch(() => {})
    )
  })
</script>

<!-- TODO: Add `has-image` class to `skill-cards__skill-card` if an image exists -->
<a
  class="skill-cards__skill-card"
  data-test="skill card"
  data-started="{started}"
  data-completed="{completed}"
  data-stale="{stale}"
  href="{introductionPageHref || practiceHref}">
  <ContentLeft
    imageSet="{imageSet}"
    stale="{stale}"
    completed="{completed}" />
  <ContentCenter
    progress="{progress}"
    stale="{stale}"
    levels="{levels}"
    title="{title}"
    completed="{completed}"
    started="{started}"
    summary="{summary}" />
</a>
