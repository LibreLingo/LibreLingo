<script lang="ts">
  export let shadow = true
  export let glow = false

  let imageURL =
    shadow === true
        ? "images/mascot-jetpack.svg"
        : "images/mascot-jetpack-noshadow.svg"
</script>

<img
  data-test="mascot-jetpack"
  src="{imageURL}"
  alt="LibreLingo Mascot"
  class="mascot"
  class:mascot--glow={glow}
/>
