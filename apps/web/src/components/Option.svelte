<script lang="ts">
  export let active
  export let inactive
  export let correct
  export let formInTargetLanguage
</script>

<div
  class="challenge-options__option"
  class:is-active={active}
  class:is-inactive={inactive}
  data-test="{active ? 'active' : inactive ? 'inactive' : 'neutral'}"
  data-test-correct="{correct}"
>
  {formInTargetLanguage}
</div>
