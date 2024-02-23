<script lang="ts">
  import { onMount } from "svelte"

  import live from "../../db/live"
  import getSkillStats from "../../db/skill/getSkillStats"
  import Heading from "../../../../lluis/Heading.svelte"

  export let title: string
  export let levels: number
  export let practiceHref: string
  export let introduction: string
  export let id: string
  export let imageSet: string[] = []
  export let summary: string[]

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
      if (stale) return "var(--deprecated-panel-background-failure)"
      if (completed) return "var(--deprecated-panel-background-success)"
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

<!-- <Card -->
<!--   {backgroundColor} -->
<!--   {foregroundColor} -->
<!--   data-test="skill card" -->
<!--   data-started={started} -->
<!--   data-completed={completed} -->
<!--   data-stale={stale} -->
<!-- > -->
<!--   <div slot="icon"> -->
<!--     {#if completed} -->
<!--       {#if stale} -->
<!--         <Icon icon="dumbbell" size="large" /> -->
<!--       {:else} -->
<!--         <Icon icon="check-square" size="large" /> -->
<!--       {/if} -->
<!--     {/if} -->
<!--   </div> -->
<!--   <div slot="content"> -->
<!--     <div class="media"> -->
<!--       <ContentLeft {imageSet} {stale} {completed} /> -->
<!--       <ContentCenter -->
<!--         {progress} -->
<!--         {stale} -->
<!--         {levels} -->
<!--         {title} -->
<!--         {completed} -->
<!--         {started} -->
<!--         {summary} -->
<!--       /> -->
<!--     </div> -->
<!--   </div> -->
<!--   <footer slot="footer"> -->
<!--     <div class="card-footer-item"> -->
<!--       <Buttons -->
<!--         {title} -->
<!--         practiceHref={introductionPageHref || practiceHref} -->
<!--         {started} -->
<!--         {completed} -->
<!--       /> -->
<!--     </div> -->
<!--   </footer> -->
<!-- </Card> -->

<a class="card" href={introductionPageHref || practiceHref}>
  {#if imageSet.length >= 1}
    <div class="image">
      <img src={`images/${imageSet[0]}_tiny.jpg`} alt="" />
    </div>
  {/if}
  <div class="content">
    <Heading level={3}>{title}</Heading>
    <div class="description">{summary.join(", ")}</div>
  </div>
</a>

<style>
  .card {
    width: 460px;
    display: flex;
    color: inherit;
    border: 1px solid #ccc;
    border-radius: 1.5rem;
    padding: 1rem;
    gap: 1rem;
    cursor: pointer;
    transition: all 0.15s;
    align-items: center;
    user-select: none;
  }

  .card:hover {
    border: 1px solid #864dcb;
    box-shadow: 4px 4px 32px rgb(112 86 143 / 8%);
  }

  .card:active {
    transform: scale(0.98);
  }

  .image {
    flex: 0 0 95px;
    height: 95px;
    display: block;
    border-radius: 1.25rem;
    background: red;
    overflow: hidden;
  }

  .image img {
    width: 95px;
  }

  .description {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
    word-wrap: break-word;
  }
</style>
