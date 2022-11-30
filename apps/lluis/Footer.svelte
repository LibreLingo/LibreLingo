<script lang="typescript">
  import Translate from "../web/src/Translate.svelte"
  import Hidden from "./Hidden.svelte"
  import LicenseLogo from "../web/src/components/LicenseLogo.svelte"
</script>

<div class="main-footer">
  <div class="container-lg main-footer__content">
    <slot />
    <div class="buttonset">
      <a href="about">
        <Translate key="index.about_librelingo">About LibreLingo</Translate>
      </a>
      <a href="https://librelingo.app/docs/">
        <Translate key="index.development_docs_english_only">
          Development docs (English)
        </Translate>
      </a>
      <Hidden>
        <br />
        <a href="/devtools"> Development tools </a>
      </Hidden>
    </div>
    <div>
      <strong>LibreLingo</strong>
      was created by
      <a href="https://github.com/kantord">Dániel Kántor</a>
      and
      <a href="https://github.com/LibreLingo/LibreLingo#contributors"
        >various contributors</a
      >. The <a href="https://github.com/LibreLingo/LibreLingo">source code</a>
      is licensed
      <a href="https://opensource.org/licenses/AGPL-3.0">AGPL-3.0.</a>
    </div>
    <LicenseLogo />
  </div>
</div>
