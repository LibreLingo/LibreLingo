<script lang="ts" context="module">
  import { waitLocale } from "svelte-i18n"
  import isBrowser from "../utils/isBrowser"

  export async function preload() {
    // See documentation: https://github.com/kaisermann/svelte-i18n/blob/main/docs/Methods.md#waitlocale
    return waitLocale()
  }

  /* Adding var css styels to JSON format */

  const defaultTheme = {
    // Colors
    white: "#fff",
    "color-primary": "#864dcb",
    "color-dark": "red",
    "color-accent": "hsl(36, 80%, 50%)",
    "deprecatedp-color-blue": "#325f74", // deprecated

    // Text colors
    "text-color-default": "#000",
    "text-color-inverted": "#fff",

    // Font sizes
    "font-size-normal": "calc(var(--spacing-base) * 4)", // 14/16
    "font-size-large": "calc(var(--spacing-base) * 6)", // 21/24
    "font-size-xlarge": "calc(var(--spacing-base) * 8)", // 28/32
    "font-size-xxlarge": "calc(var(--spacing-base) * 10)", // 35/40

    // Spacing
    "spacing-none": "0",
    "spacing-xs": "calc(var(--spacing-base) * 2)", // 7/8
    "spacing-s": "calc(var(--spacing-base) * 4)", // 14/16
    "spacing-m": "calc(var(--spacing-base) * 8)", // 28/32
    "spacing-l": "calc(var(--spacing-base) * 10)", // 35/40
    "spacing-xl": "calc(var(--spacing-base) * 20)", // 70/80

    // Responsive design
    "page-max-width": "1920px",
    "page-padding": "16px",
    "hero-max-width": "960px",

    // Button specific styles
    // Primary
    "button-color-primary": "var(--color-primary)",
    "button-border-color-primary": "transparent",
    "button-color-primary-hover": "var(--color-primary)",

    // Accent
    "button-color-accent": "var(--color-accent)",
    "button-border-color-accent": "transparent",

    // Secondary
    "button-color-secondary": "var(--white)",
    "button-border-color-secondary": "var(--button-color-primary)",

    // NavBar specific styles
    "navbar-background": "rgb(255, 255, 255)",
    "navbar-height": "96px",

    // DEPRECATED variables
    // these should be deleted when they are no longer used
    "deprecated-spacing-small": "8px",
    "deprecated-spacing-medium": "12px",
    "deprecated-spacing-large":
      "calc(var(--deprecated-spacing-small) + var(--deprecated-spacing-medium))",
    "deprecated-color-blue": "#325f74",
    "deprecated-color-white": "#faf4f0",
    "animation-short": ".1s",
    "deprecated-button-primary-background-color": "#325f74",
    "deprecated-button-primary-text-color": "#fff",
    "deprecated-button-primary-border": "transparent",
    "deprecated-button-secondary-background-color": "#f5f5f5",
    "deprecated-button-secondary-text-color": "#111",
    "deprecated-button-secondary-border": "#b5b5b5",
    "deprecated-button-key-background-color": "#f5f5f5",
    "deprecated-button-key-text-color": "#111",
    "deprecated-button-key-border": "#b5b5b5",
    "deprecated-button-radius-small":
      "calc(var(--deprecated-spacing-small) / 2)",
    "deprecated-navbar-background": "var(--deprecated-color-blue)", // deprecated
    "deprecated-navbar-text-color": "var(--deprecated-color-white)",
    "deprecated-navbar-highlight-color": " rgba(255, 255, 255, .1)",
    "deprecated-navbar-height": "52px",
    "deprecated-navbar-padding-vertical": "var(--deprecated-spacing-small)",
    "deprecated-navbar-padding-horizontal": "var(--deprecated-spacing-medium)",
    "deprecated-navbar-logo-height":
      "calc(var(--deprecated-navbar-height) - 2 * var(--deprecated-spacing-small))",
    "deprecated-panel-background": "white",
    "deprecated-panel-background-success": "#84b83f",
    "deprecated-panel-background-failure": "#ab2149",
    "deprecated-panel-background-info": "#fcb141",
  }
  let theme
  theme = Object.entries(defaultTheme)
    .map(([key, value]) => `--${key}:${value}`)
    .join(";")
</script>

<svelte:head>
  <meta name="twitter:card" content="summary_large_image" />
  <meta
    name="twitter:description"
    content="an experiment to create a community-owned language-learning
    platform"
  />
  <meta name="twitter:title" content="LibreLingo" />

  <meta
    name="twitter:image"
    content="https://librelingo.app/images/social_cover_1.png"
  />
  <meta name="twitter:creator" content="@cacophonism" />

  <meta property="og:title" content="LibreLingo" />
  <meta
    property="og:description"
    content="an experiment to create a community-driven language-learning
    platform"
  />
  <meta
    property="og:image"
    content="https://librelingo.app/images/social_cover_1.png"
  />
</svelte:head>

{#if isBrowser() !== true}
  <div class="pageloader is-active"><span class="title">LibreLingo</span></div>
{/if}

<main style={theme}>
  <slot />
</main>

<style>
  :root {
    --spacing-base: 3.5px;
  }

  @media (min-width: 993px) {
    :root {
      --spacing-base: 4px;
    }
  }

  html {
    box-sizing: border-box;
    font-size: 16px;
  }
</style>
