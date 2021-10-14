import Vue from 'vue';
import SwiperClass, { Navigation, Pagination } from "swiper";

SwiperClass.use([Navigation, Pagination]);

import VueAwesomeSwiper from 'vue-awesome-swiper';

import 'swiper/swiper-bundle.css'
import 'swiper/components/navigation/navigation.min.css';
// import 'swiper/components/pagination/pagination.min.css';

Vue.use(VueAwesomeSwiper);
