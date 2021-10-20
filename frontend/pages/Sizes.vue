<template>
  <div class='sizes info_container'>
    <info-items />
    <info-text>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aspernatur deserunt, eos est excepturi
        facilis fugit iure maxime molestiae nostrum officia provident repellat sed ut vel? Neque nihil officia sit.
      </p>
    </info-text>
  </div>
</template>

<script>
import InfoItems from '@/components/sections/info/InfoItems'
import InfoText from '@/components/sections/info/InfoText'

export default {
  name: 'Sizes',
  components: { InfoText, InfoItems }
}
</script>

<style scoped>

</style>
