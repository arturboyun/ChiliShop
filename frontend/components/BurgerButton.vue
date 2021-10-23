<template>
  <button @click='toggleMenu'>
    <span class='line'></span>
    <span class='line'></span>
    <span class='line'></span>
  </button>
</template>

<script>
export default {
  name: 'BurgerButton',
  methods: {
    toggleMenu() {
      this.$nuxt.$emit('open-menu')
    }
  }
}
</script>

<style lang='scss' scoped>

.burger {
  position: relative;
  background-color: transparent;
  border: none;
  cursor: pointer;
  display: none;
  padding: 0;
  width: 34px;
  height: 25px;

  @media screen and (max-width: 1200px) {
    display: flex;
  }
}

.line {
  position: absolute;
  width: 100%;
  height: 2px;
  background-color: #fff;

  &:nth-child(1) {
    top: 0;
  }

  &:nth-child(2) {
    top: 50%;
    transform: translateY(-50%);
  }

  &:nth-child(3) {
    bottom: 0;
  }
}

</style>
