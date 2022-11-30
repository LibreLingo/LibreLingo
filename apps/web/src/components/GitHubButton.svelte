<script lang="ts" context="module">
  export async function preload() {
      const repo = await fetch("https://api.github.com/repos/LibreLingo/LibreLingo")

      const { stargazers_count } = await repo.json()
      return {
          stargazers_count,
      }
  }
</script>

<script lang="ts">
  import { onMount } from "svelte"
  import isBrowser from "../utils/isBrowser"
  import Icon from "lluis/Icon.svelte"
  import Button from "lluis/Button.svelte"
  import isCypress from "../utils/isCypress"
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const pMemoize = require("p-memoize")

  type WindowWithStars = Window & {
    stars: number
    star_count: number
  }

  export let stars =
    (isBrowser() === true
        ? (window as unknown as WindowWithStars).stars
        : null) || "   "
  export let size: "small" | "medium" = "small"

  onMount(async () => {
      if (isBrowser() === true && isCypress()) {
          stars = 999
          return
      }

      pMemoize(fetch, { maxAge: 5 * 60 * 1000 })(
          "https://api.github.com/repos/LibreLingo/LibreLingo"
      )
          .then((res) => res.json())
          .then(({ stargazers_count }) => {
              stars = stargazers_count
              if (isBrowser() === true) {
                  (window as unknown as WindowWithStars).star_count = stargazers_count
              }
          })
  })
</script>

<Button
  target="_blank"
  size="{size}"
  href="https://github.com/LibreLingo/LibreLingo"
>
  {#if stars}
    <span class="stars">{stars}</span>
    <span class="icon">
      <Icon icon="star" />
    </span>
  {/if}
  GitHub
</Button>
