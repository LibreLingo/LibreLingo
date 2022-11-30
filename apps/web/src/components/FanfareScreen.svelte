<script lang="ts">
  import db from "../db/db"
  import savePractice from "../db/skill/savePractice"
  import sound from "../media/sound"
  import hotkeys from "hotkeys-js"
  import { onMount } from "svelte"
  import { goto } from "@sapper/app"
  import Mascot from "./Mascot.svelte"
  import TwitterButton from "./TwitterButton.svelte"
  import Button from "lluis/Button.svelte"

  export let courseURL
  export let skillId
  export let stats

  onMount(async () => {
    sound.fanfare.play()
  })

  onMount(async () => {
    await savePractice(db, { id: skillId, ...stats })
  })

  onMount(() => {
    hotkeys.unbind("enter")
    hotkeys("enter", () => {
      goto(courseURL)
    })
  })
</script>

<main class="main-content main-content--challenge full-width-container">
  <div class="container-md">
    <div class="fanfare-screen">
      <div class="fanfare-screen__mascot">
        <Mascot />
      </div>
      <div class="fanfare-screen__content grid">
        <h2>Lesson completed!</h2>
        <p>
          You've completed
          {stats.correct}
          challenges
        </p>
        <Button style="primary" href="{courseURL}">
          Continue to course page
        </Button>

        <h3 class="m-top-2">Excited about LibreLingo?</h3>
        <TwitterButton />
      </div>
    </div>
  </div>
</main>
