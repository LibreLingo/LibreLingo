<script lang="ts" context="module">
  export async function preload() {
    try {
      // eslint-disable-next-line @typescript-eslint/no-var-requires
      const fs = require("fs")
      // eslint-disable-next-line @typescript-eslint/no-var-requires
      const util = require("util")
      const readdir = util.promisify(fs.readdir)

      return {
        testSkills: (await readdir("./src/courses/test/challenges")).map(
          (fname: string) => fname.split(".")[0]
        ),
      }
    } catch (error) {
      // do nothing
    }
  }
</script>

<script lang="ts">
  import NavBar from "../components/NavBar.svelte"
  import Content from "lluis/Content.svelte"

  export let testSkills: Array<string> = []
</script>

<svelte:head>
  <title>LibreLingo - Development</title>
</svelte:head>

<NavBar hasAuth />

<main class="main-content container-md">
  <Content>
    <h1>Development tools</h1>
    <h2>Test pages</h2>
    <ul>
      <li><a href="/course/test">Test course</a></li>
      {#each testSkills as testSkill}
        <li>
          <a target="_blank" href="/course/test/skill/{testSkill}">
            Test skill:
            <b>{testSkill}</b>
          </a>
        </li>
      {/each}
      <li>
        <a
          target="_blank"
          href="/course/preview/skill/gist?skillName=helloworld&gistId=2428349a05d81f96b2311c2749ea5c6d"
        >
          Test skill: <b>GitHub Gist preview of a skill</b>
        </a>
      </li>
      <li>
        <a
          target="_blank"
          href="/course/preview/skill/gist/introduction?gistId=2428349a05d81f96b2311c2749ea5c6d"
        >
          Test skill: <b>GitHub Gist preview of a skill introduction</b>
        </a>
      </li>
      <li>
        <a target="_blank" href="/dev-typography">
          <b>Typography</b>
        </a>
      </li>
      <li>
        <a target="_blank" href="/course-tools-legacy/">
          <b>The legacy dev tool</b>
        </a>
      </li>
    </ul>
  </Content>
</main>
