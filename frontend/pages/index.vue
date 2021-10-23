<template>
  <div class='home'>
    <hero />
    <our-clients />
  </div>
</template>

<script>
import OurClients from '@/components/sections/main/OurClients'
import Hero from '@/components/sections/main/Hero'

export default {
  components: { Hero, OurClients },
  mounted() {
    this.$nuxt.$emit('close-menu')
    this.$nuxt.$emit('close-basket')
  }
}
</script>

<style lang='scss' scoped>
</style>
