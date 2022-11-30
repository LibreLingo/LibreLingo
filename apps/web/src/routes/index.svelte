<script lang="ts">
  import Mascot from "../components/Mascot.svelte"
  import Button from "lluis/Button.svelte"
  import Hidden from "lluis/Hidden.svelte"
  import Footer from "lluis/Footer.svelte"
  import Hero from "lluis/Hero.svelte"
  import Stack from "lluis/Stack.svelte"
  import { _ } from "svelte-i18n"
  import Translate from "../Translate.svelte"
  import NavBar from "../components/NavBar.svelte"
</script>

<svelte:head>
  <title>{$_("meta.title")}</title>
  <meta name="description" content={$_("index.meta.description")} />
</svelte:head>

<NavBar hasAuth />

<main class="main-content">
  <Hero>
    <Stack>
      <Mascot shadow={false} glow={true} />
      <Stack direction="column" spacing="xl">
        <h1>
          <Translate key="index.subtitle">
            A community-driven <b class="text-highlight"
              >language-learning platform</b
            >
          </Translate>
        </h1>
        <Stack>
          <Button
            style="primary"
            size="large"
            href="course/spanish-from-english"
          >
            <Translate key="index.start_spanish_course">
              Start learning Spanish
            </Translate>
          </Button>
        </Stack>
      </Stack>
    </Stack>
    <!-- <div> -->
    <!--   <div> -->
    <!--     <div> -->
    <!--       <Mascot shadow={false} glow={true} /> -->
    <!--     </div> -->
    <!--     <h1> -->
    <!--       <Translate key="index.subtitle"> -->
    <!--         A community-driven <b class="text-highlight" -->
    <!--           >language-learning platform</b -->
    <!--         > -->
    <!--       </Translate> -->
    <!--     </h1> -->
    <!--   </div> -->
    <!--   <div> -->
    <!--     <div> -->
    <!--       <Button -->
    <!--         style="primary" -->
    <!--         size="large" -->
    <!--         href="course/spanish-from-english" -->
    <!--       > -->
    <!--         <Translate key="index.start_spanish_course"> -->
    <!--           Start learning Spanish -->
    <!--         </Translate> -->
    <!--       </Button> -->
    <!--       <Hidden> -->
    <!--         <Button style="primary" href="course/german-from-english"> -->
    <!--           Start learning German -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/french-from-english"> -->
    <!--           Start learning French -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/bangla-from-english"> -->
    <!--           Start learning Bangla -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/parsig-from-english"> -->
    <!--           Start learning Middle Persian -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/basque-from-english"> -->
    <!--           Start learning Basque -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/ladino-from-english"> -->
    <!--           Start learning Ladino (for English speakers) -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/ladino-from-hebrew"> -->
    <!--           Start learning Ladino (for Hebrew speakers) -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/ladino-from-spanish"> -->
    <!--           Start learning Ladino (for Spanish speakers) -->
    <!--         </Button> -->

    <!--         <Button style="primary" href="course/houma-from-english"> -->
    <!--           Start learning Houma (for English speakers) -->
    <!--         </Button> -->
    <!--       </Hidden> -->
    <!--     </div> -->
    <!--   </div> -->
    <!-- </div> -->
  </Hero>
</main>
<Footer />
