<script>
  import Title from "lluis/Title.svelte"
  import NavBar from "../../components/NavBar.svelte"
  import courses from "../../../../../config/courses.json"
  import { t } from 'svelte-i18n'
</script>

<NavBar />

<Title size={2}>{$t('dev.developer_tools')}</Title>
<Title size={3}>{$t('dev.courses')}</Title>

<table>
  <thead>
    <td>{$t('dev.course_name')}</td>
    <td>{$t('dev.devtools')}</td>
    <td>{$t('dev.repo')}</td>
  </thead>
  {#each courses as course}
    <tr>
      <td>
        <a href={`/course/${course.paths.jsonFolder}`}>
          {course.paths.jsonFolder}
        </a>
      </td>
      {#if course.devtoolsEnabled}
        <td>
          <a href={`course-tools-legacy/${course.paths.jsonFolder}/`}>
            dev tools
          </a>
        </td>
      {:else}
        <td />
      {/if}
      <td>
        <a href={course.repositoryURL} target="_blank" rel="noreferrer">
          {new URL(course.repositoryURL).hostname.replace("www.", "")}</a
        >
      </td>
    </tr>
  {/each}
</table>

<style>
  td {
    padding: 4px 16px;
  }

  thead {
    font-weight: bold;
  }
</style>
