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
  components: { Hero, OurClients }
}
</script>

<style lang='scss' scoped>
</style>
