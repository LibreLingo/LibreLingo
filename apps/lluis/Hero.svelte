<div class="hero">
  <div class="backdrop">
    <div>
      <img
        src="/images/home-background-shape-back.svg"
        alt=""
        aria-hidden="true"
      />
    </div>
    <div>
      <img
        src="/images/home-background-shape-front.svg"
        alt=""
        aria-hidden="true"
      />
    </div>
  </div>

  <div class="content">
    <slot />
  </div>
</div>

<style>
  .hero {
    position: relative;
  }

  .backdrop {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 500px;
  }

  .backdrop > * {
    position: absolute;
  }

  /* .home-hero__bg-shape-back { */
  /*   img { */
  /*     width: 69%; */
  /*     min-width: 960px; */
  /*     max-width: 1023px; */
  /*   } */
  /* } */
  /* .home-hero__bg-shape-front { */
  /*   margin-top: 2rem; */
  /*   img { */
  /*     width: 72%; */
  /*     min-width: 1000px; */
  /*     max-width: 1068px; */
  /*   } */
  /* } */

  .backdrop {
    position: absolute;
    top: 0;
    left: 0;
  }
</style>
