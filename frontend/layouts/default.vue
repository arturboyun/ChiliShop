<template>
  <div class='layout'>
    <Header :categories='headerCategories' />
    <div class='main-container'>
      <Nuxt />
    </div>
    <Footer :categories='headerCategories' />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import { mapGetters } from 'vuex'

export default {
  components: { Header, Footer },
  data() {
    return {}
  },
  async mounted() {
    await this.$store.dispatch('categories/getCategories', { skip: 0, limit: 999 })
  },
  computed: {
    ...mapGetters('categories', ['headerCategories']),
  }
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
