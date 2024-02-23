<script lang="ts">
  import Button from "lluis/DeprecatedButton.svelte"
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
      <Button on:click="{skipAction}">Skip</Button>
    {/if}
    <Button on:click="{skipAllAction}">Cancel</Button>
    {#if skipAllVoice}
      <Button on:click="{skipAllVoice}">Can't listen now</Button>
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
    {:else if submit}
      <Button style="primary" type="submit">Submit</Button>
    {:else}
      <Button style="primary" type="submit" disabled={true}>Submit</Button>
    {/if}
  </div>
</Panel>
