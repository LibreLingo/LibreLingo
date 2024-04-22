<script lang="ts">
  import Button from "lluis/DeprecatedButton.svelte"
  import Panel from "lluis/Panel.svelte"
  import { t } from 'svelte-i18n'

  export let buttonText
  export let buttonAction = null
  export let correct = false
  export let incorrect = false
  export let typo = false
  export let message
  export let messageDetail = null
  export let submit = null
  export let skipAction = null
  export let skipAllAction = null
  export let skipAllVoice = null

  let background: "default" | "success" | "failure" | "info" = (() => {
      if (correct) {
          return "success"
      }
      if (incorrect) {
          return "failure"
      }
      if (typo) {
          return "info"
      }

      return "default"
  })()
</script>

<Panel background="{background}">
  <div slot="left">
    {#if skipAction}
      <Button on:click="{skipAction}">{$t('challenge_panel.skip')}</Button>
    {/if}
    <Button on:click="{skipAllAction}">{$t('challenge_panel.cancel')}</Button>
    {#if skipAllVoice}
      <Button on:click="{skipAllVoice}">{$t('challenge_panel.cant_listen_now')}</Button>
    {/if}
    {#if message}<b>{message}</b>{/if}
    {#if messageDetail}
      <p>{messageDetail}</p>
    {/if}
  </div>

  <div slot="right">
    {#if buttonAction}
      <Button style="primary" type="submit" on:click="{buttonAction}">
        {buttonText}
      </Button>
    {/if}
    {#if submit}
      <Button style="primary" type="submit">{$t('challenge_panel.submit')}</Button>
    {/if}
  </div>
</Panel>
