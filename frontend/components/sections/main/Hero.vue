<template>

  <div class='hero'>
    <swiper :options='swiperOption' class='swiper'>
      <!-- <swiper-slide><img alt='slide image' class='slide__image' src='~/assets/images/slide 1.png'></swiper-slide> -->
      <!-- <swiper-slide><img alt='slide image' class='slide__image' src='~/assets/images/slide 2.png'></swiper-slide> -->
      <swiper-slide><div :style="{ backgroundImage: 'url(' + require('@/assets/images/slide_1.png') + ')' }" class='slide__image'> </div></swiper-slide>
      <swiper-slide><div :style="{ backgroundImage: 'url(' + require('@/assets/images/slide_2.png') + ')' }" class='slide__image'> </div></swiper-slide>
      
      <div slot='pagination' class='swiper-pagination'></div>
      <div slot='button-prev' class='swiper-button-prev swiper-button-white'></div>
      <div slot='button-next' class='swiper-button-next swiper-button-white'></div>
    </swiper>
  </div>
</template>

<script>
import { directive, Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
  name: 'Hero',
  components: { Swiper, SwiperSlide },
  directives: {
    swiper: directive
  },
  data() {
    return {
      swiperOption: {
        effect: 'fade',
        slidesPerView: 1,
        loop: true,
        observer: true,
        observeParents: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      }
    }
  }
}
</script>

<style lang='scss' scoped>
.hero {
  width: 100%;
  height: 700px;

  @media screen and (max-width: 1440px) {
    height: 600px;
  }

  @media screen and (max-width: 1366px) {
    height: 550px;
  }

  @media screen and (max-width: 1080px) {
    height: 450px;
  }

  @media screen and (max-width: 885px) {
    height: 320px;
  }

  @media screen and (max-width: 640px) {
    height: 250px;
  }

  @media screen and (max-width: 480px) {
    height: 200px;
  }

  @media screen and (max-width: 400px) {
    height: 150px;
  }
}

.swiper {
  position: relative;
  width: 100%;

  .slide__image {
    width: 100%;
    height: 700px;
    // height: 80vh;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    @media screen and (max-width: 1440px) {
      height: 600px;
    }

    @media screen and (max-width: 1366px) {
      height: 550px;
    }

    @media screen and (max-width: 1080px) {
      height: 450px;
    }

    @media screen and (max-width: 885px) {
      height: 320px;
    }

    @media screen and (max-width: 640px) {
      height: 250px;
    }

    @media screen and (max-width: 480px) {
      height: 200px;
    }

    @media screen and (max-width: 400px) {
      height: 150px;
    }
  }

  .swiper-pagination-bullet {
    background-color: blue;
    display: inline-block;
    width: 2rem;
    height: 2rem;
  }
}

.swiper-button-prev::after {
  font-size: 18px !important;
}

.swiper-button-next::after {
  font-size: 18px !important;
}

@media screen and (max-width: 860px) {
  .swiper-button-prev::after {
    font-size: 0px !important;
  }

  .swiper-button-next::after {
    font-size: 0px !important;
  }
}

.swiper-pagination::v-deep {
  .swiper-pagination-bullet {
    width: 15px;
    height: 15px;
    opacity: 1;
    border: white solid 1px;
    background-color: transparent;
  }

  .swiper-pagination-bullet-active {
    background-color: rgba(#c4c4c4, .25);
  }
}
</style>
