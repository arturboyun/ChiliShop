<template>
  <div class="home">
    <div class="hero">
      <swiper class="swiper" :options="swiperOption">
        <swiper-slide><img src="~/assets/images/hero1.png" alt="asdadsads" class="slide__image"></swiper-slide>
        <swiper-slide><img src="~/assets/images/hero1.png" alt="asdadsads" class="slide__image"></swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
        <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>
        <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
      </swiper>
    </div>
    <our-clients/>
  </div>
</template>

<script>
import Header from "~/components/Header";
import { Swiper, SwiperSlide, directive } from "vue-awesome-swiper";
import OurClients from "~/components/sections/OurClients";

export default {
  components: {OurClients, Header, Swiper, SwiperSlide},
  directives: {
    swiper: directive,
  },
  data() {
    return {
      swiperOption: {
        effect: 'fade',
        slidesPerView: 1,
        observeParents: true,
        loop: true,
        observer: true,
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

<style scoped lang="scss">
.hero {
  width: 100%;
  height: 850px;
}

.swiper {
  position: relative;
  width: 100%;

  .slide__image {
    width: 100%;
    height: 850px;
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
