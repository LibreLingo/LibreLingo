<script lang="ts" context="module">
  import { waitLocale } from "svelte-i18n"
  import isBrowser from "../utils/isBrowser"

  export async function preload() {
    return waitLocale()
  }

  /* Adding var css styels to JSON format */

  const defaultTheme = {
    // Colors
    white: "#fff",
    "color-primary": "#864dcb",
    "color-dark": "red",
    "color-accent": "hsl(36, 80%, 50%)",

    // Text colors
    "text-color-default": "#000",
    "text-color-inverted": "#fff",

    // Font sizes
    "font-size-normal": "16px",
    "font-size-large": "20px",
    "font-size-xlarge": "24px",

    // Spacing
    "spacing-none": "0",
    "spacing-xl": "100px",

    // Button specific styles
    // Primary
    "button-color-primary": "var(--color-primary)",
    "button-border-color-primary": "transparent",
    "button-color-primary-hover": "var(--color-primary-dark)",

    // Accent
    "button-color-accent": "var(--color-accent)",
    "button-border-color-accent": "transparent",

    // Secondary
    "button-color-secondary": "var(--white)",
    "button-border-color-secondary": "var(--button-color-primary)",

    // NavBar specific styles
    "navbar-background": "rgba(255, 255, 255, .85)",
    "navbar-height": "96px",
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
  <div class="pageloader is-active">
    <span class="pageloader__title">Loading LibreLingo...</span>
  </div>
{/if}

<main style={theme}>
  <slot />
</main>
