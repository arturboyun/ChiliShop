<template>
  <div class='layout'>
    <basket-modal :show='basketIsOpen' @update:show='hideBasket'/>

    <Header :categories='this.headerCategories' @open-basket='showBasket'/>

    <div class='main-container'>
      <Nuxt/>
    </div>

    <Footer :categories='this.headerCategories' />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import { mapGetters, mapState } from 'vuex'
import BasketModal from '@/components/sections/shop/BasketModal'

export default {
  components: { BasketModal, Header, Footer },
  data() {
    return {
      basketIsOpen: false,
    }
  },
  async fetch() {
    await this.$store.dispatch('categories/getCategories', { skip: 0, limit: 999 })
  },
  created() {
    this.$nuxt.$on('open-basket', () => {
      this.showBasket()
    })
    this.$nuxt.$on('close-basket', () => {
      this.hideBasket()
    })
  },
  computed: {
    ...mapGetters('categories', ['headerCategories']),
  },
  methods: {
    showBasket() {
      this.basketIsOpen = true;
    },
    hideBasket() {
      this.basketIsOpen = false;
    },
  },
}
</script>

<style lang='scss'>
.layout {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.main-container {
  padding-top: 100px;
}
</style>
