<script lang="ts">
  import type { SizeType } from "./types"

  export let size: null | SizeType = null
  export let centered = false
</script>

<div
  class:col-1={size === "1"}
  class:col-2={size === "2"}
  class:col-3={size === "3"}
  class:col-4={size === "4"}
  class:col-5={size === "5"}
  class:col-6={size === "6"}
  class:col-7={size === "7"}
  class:col-8={size === "8"}
  class:col-9={size === "9"}
  class:col-10={size === "10"}
  class:col-11={size === "11"}
  class:col-centered={centered}
>
  <slot />
</div>
