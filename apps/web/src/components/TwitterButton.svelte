<script lang="ts">
  import Button from "lluis/DeprecatedButton.svelte"
  import Icon from "lluis/Icon.svelte"
  import { t } from 'svelte-i18n'
</script>

<Button
  target="_blank"
  href="https://twitter.com/intent/tweet?hashtags=LibreLingo%2Copensource&url=https%3A%2F%2Flibrelingo.app&text=LibreLingo%20-%20an%20experiment%20to%20create%20a%20community-owned%20language%20learning%20tool%0A"
>
  <slot name="icon-left">
			<Icon icon="twitter" prefix="fab" size="small" />
  </slot>
  <div>{$t('twitter.button.tweet_about_librelingo')}</div>
</Button>
