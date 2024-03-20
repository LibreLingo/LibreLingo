<script lang="ts">
  import Button from "lluis/DeprecatedButton.svelte"
  import Translate from "../../Translate.svelte"
  import { t } from 'svelte-i18n'

  export let practiceHref
  export let completed
  export let started
</script>

<div class="container">
  {#if completed}
    <Button style="primary" href={practiceHref}>
      <Translate key="course_page.button_practice">{$t('buttons.practice')}</Translate>
    </Button>
  {:else if started}
    <Button style="primary" href={practiceHref}>
      <Translate key="course_page.button_continue">{$t('buttons.continue_learning')}</Translate>
    </Button>
  {:else}
    <Button style="primary" href={practiceHref}>
      <Translate key="course_page.button_learn">{$t('buttons.learn')}</Translate>
    </Button>
  {/if}
</div>

<style>
  .container {
    display: flex;
    justify-content: center;
  }
</style>
