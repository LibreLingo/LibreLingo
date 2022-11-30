<script lang="ts">
  import Button from "lluis/Button.svelte"
  import Panel from "lluis/Panel.svelte"

  export let buttonText
  export let buttonAction = null
  export let correct = false
  export let incorrect = false
  export let typo = false
  export let message
  export let messageDetail = null
  export let submit = null
  export let skipAction = null
  export let skipAllVoice = null

  let state: "default" | "success" | "failure" | "info" = (() => {
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

<Panel state="{state}">
  <div slot="left" class="panel__left">
    <div class="buttonset">
      {#if skipAction}
        <Button on:click="{skipAction}" style="secondary">Skip</Button>
      {/if}
      {#if skipAllVoice}
        <Button on:click="{skipAllVoice}" style="secondary">Can't listen now</Button>
      {/if}
      <div class="panel__message">
        {#if message}
          <b>{message}</b>
        {/if}
        {#if messageDetail}
          <div>{messageDetail}</div>
        {/if}
      </div>
    </div>
  </div>

  <div slot="right" class="panel__right">
    {#if buttonAction}
      <Button style="primary" type="submit" on:click="{buttonAction}">
        {buttonText}
      </Button>
    {/if}
    {#if submit}
      <Button style="primary" type="submit">Submit</Button>
    {/if}
  </div>
</Panel>
