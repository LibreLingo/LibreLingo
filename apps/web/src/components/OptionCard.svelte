<script lang="typescript">
  export let active
  export let inactive
  export let number
  export let picture
  export let correct
  export let formInTargetLanguage
</script>

<div
  class="challenge-option-deck__option-card"
  class:is-active={active}
  class:is-inactive={inactive}
  data-test="{active ? 'active' : inactive ? 'inactive' : 'neutral'}"
  data-test-correct="{correct}"
>
  <div class="option-card__image">
    <img
      src="{`images/${picture}`}"
      alt=""
      data-test="{`card-img-${number}`}"
    />
  </div>
  <div class="option-card__text">
    <div
      data-test="{`card-text-${number}`}"
    >
      {formInTargetLanguage}
    </div>
    <small class="option-card__shortcut">
      {number}
    </small>
  </div>
</div>
