<script lang="ts">
  import { scale } from "svelte/transition"
  import db from "../db/db"
  import savePractice from "../db/skill/savePractice"
  import sound from "../media/sound"
  import hotkeys from "hotkeys-js"
  import { onMount } from "svelte"
  import { goto } from "@sapper/app"
  import Mascot from "./Mascot.svelte"
  import TwitterButton from "./TwitterButton.svelte"
  import Button from "lluis/DeprecatedButton.svelte"
  import Column from "lluis/Column.svelte"
  import Columns from "lluis/Columns.svelte"
  import Title from "lluis/Title.svelte"
  import { t } from 'svelte-i18n'

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

<section class="hero is-fullheight-with-navbar">
  <div class="hero-body">
    <div class="container" in:scale>
      <Columns>
        <Column size="3/5">
          <div class="mascot">
            <Mascot />
          </div>
        </Column>
        <Column size="2/5">
          <div class="is-centered-mobile">
            <Title size={2} sizeMobile="3" multiline>{$t('fanfare_screen.lesson_completed')}</Title>
            <Title size={2} isSubtitle={true} multiline>
              {$t('fanfare_screen.youve_completed')}
              {stats.correct}
              {$t('fanfare_screen.challenges')}
            </Title>
            <Button size="medium" href={courseURL} style="primary">
              {$t('fanfare_screen.continue_to_course_page')}
            </Button>
            <div class="bottom">
              <Title size={5}>{$t('fanfare_screen.excited_about_librelingo')}</Title>
              <TwitterButton />
            </div>
          </div>
        </Column>
      </Columns>
    </div>
  </div>
</section>

<style type="text/scss">
  @import "../variables";

  @include from($tablet) {
    .bottom {
      position: absolute;
      bottom: 0;
    }
  }

  @include until($tablet) {
    .mascot {
      width: 45%;
      margin: auto;
    }

    .bottom {
      margin-top: 4em;
    }

    .is-centered-mobile {
      text-align: center;
    }
  }
</style>
