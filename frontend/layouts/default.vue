<template>
  <div class="layout">
    <Header/>
    <div class="main-container">
      <Nuxt />
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";

export default {
  components: {Header, Footer},
  data () {
    return {
    }
  }
}
</script>

<style lang="scss">
.layout {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.main-container {
  padding-top: 100px;
}
</style>
