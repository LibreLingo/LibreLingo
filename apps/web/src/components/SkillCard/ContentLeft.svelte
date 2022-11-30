<script lang="ts">
  export let imageSet
  export let stale
  export let completed
</script>

{#if imageSet && imageSet.length}
  <!-- TODO: Update image set -->
  <!-- <div class:is-completed={completed} class:is-stale={stale}>
    <div class="image-set">
      <ImageSet imageSet="{imageSet}" stale="{stale}" completed="{completed}" />
    </div>
  </div> -->
  <div class="skill-card__image" class:is-completed={completed} class:is-stale={stale}>
    <img src="{`images/${imageSet[0]}_tiny.jpg`}" alt="" />
  </div>
{/if}
