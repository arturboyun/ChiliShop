<template>

  <div class='hero'>
    <swiper :options='swiperOption' class='swiper'>
      <swiper-slide><img alt='asdadsads' class='slide__image' src='~/assets/images/hero1.png'></swiper-slide>
      <swiper-slide><img alt='asdadsads' class='slide__image' src='~/assets/images/hero1.png'></swiper-slide>
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
  height: 850px;

  @media screen and (max-width: 1200px) {
    height: 600px;
  }

  @media screen and (max-width: 900px) {
    height: 400px;
  }

  @media screen and (max-width: 600px) {
    height: 200px;
  }
}

.swiper {
  position: relative;
  width: 100%;

  .slide__image {
    width: 100%;
    height: 850px;

    @media screen and (max-width: 1200px) {
      height: 600px;
    }

    @media screen and (max-width: 900px) {
      height: 400px;
    }

    @media screen and (max-width: 600px) {
      height: 200px;
    }
  }

  .swiper-pagination-bullet {
    background-color: blue;
    display: inline-block;
    width: 2rem;
    height: 2rem;
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
