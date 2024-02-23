<script lang="ts">
  type StackAlign =
    | "normal"
    | "stretch"
    | "center"
    | "start"
    | "end"
    | "flex-start"
    | "flex-end"
    | "baseline"
    | "first baseline"
    | "last baseline"
    | "safe center"
    | "unsafe center"
    | "inherit"
    | "initial"
    | "revert"
    | "revert-layer"
    | "unset"

  type StackJustify =
    | "center"
    | "start"
    | "end"
    | "flex-start"
    | "flex-end"
    | "left"
    | "right"
    | "normal"
    | "space-between"
    | "space-around"
    | "space-evenly"
    | "stretch"
    | "safe center"
    | "unsafe center"
    | "inherit"
    | "initial"
    | "revert"
    | "revert-layer"
    | "unset"

  type SpacingSize = "none" | "xs" | "s" | "m" | "l" | "xl"
  type StackDirection = "row" | "column"

  export let direction: StackDirection = "row"
  export let directionDesktop: StackDirection | null = null
  export let directionTablet: StackDirection | null = null
  export let align: StackAlign = "normal"
  export let justify: StackJustify = "normal"
  export let spacing: SpacingSize | null = null
  export let wrap: boolean | null = null
  export let shrink = 1
  export let fullHeight = false

  $: compiledStyle = (() => {
    let variables: [string, string][] = []

    if (spacing) {
      variables.push(["spacing", `var(--spacing-${spacing})`])
    }

    if (direction !== "row") {
      variables.push(["direction-mobile", direction])
    }

    if (directionTablet) {
      variables.push(["direction-tablet", directionTablet])
    }

    if (directionDesktop) {
      variables.push(["direction-desktop", directionDesktop])
    }

    if (fullHeight) {
      variables.push(["height", "100%"])
    }

    if (align !== "normal") {
      variables.push(["align", align])
    }

    if (justify !== "normal") {
      variables.push(["justify", justify])
    }

    if (shrink !== 1) {
      variables.push(["shrink", `${shrink}`])
    }

    if (wrap) {
      variables.push(["wrap", "wrap"])
    }

    return variables
      .map(([name, value]) => `--stack-${name}:${value}`)
      .join(";")
  })()
</script>

<div style={compiledStyle}>
  <slot />
</div>

<style>
  div {
    --stack-spacing: 0;
    --stack-shrink: 1;
    --stack-align: normal;
    --stack-justify: normal;
    --stack-height: auto;
    --stack-direction-mobile: row;
    --stack-direction-tablet: var(--stack-direction-mobile);
    --stack-direction-desktop: var(--stack-direction-tablet);

    display: flex;
    gap: var(--stack-spacing);
    align-items: var(--stack-align);
    justify-content: var(--stack-justify);
    flex-shrink: var(--stack-shrink);
    height: var(--stack-height);
    flex-direction: var(--stack-direction-mobile);
    flex-wrap: var(--stack-wrap);
  }

  @media screen and (min-width: 577px) {
    div {
      flex-direction: var(--stack-direction-tablet);
    }
  }

  @media screen and (min-width: 993px) {
    div {
      flex-direction: var(--stack-direction-desktop);
    }
  }
</style>
