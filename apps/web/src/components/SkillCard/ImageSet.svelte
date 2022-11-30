<script lang="ts">
  export let imageSet
  export let completed
  export let stale
</script>

<figure class="image image-set is-96x96" class:is-completed={completed} class:is-stale={stale}>
  <img src="{`images/${imageSet[0]}_tinier.jpg`}" alt="" />
  <img src="{`images/${imageSet[1]}_tinier.jpg`}" alt="" />
  <img src="{`images/${imageSet[2]}_tiny.jpg`}" alt="" />
</figure>
