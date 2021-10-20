<template>
  <div class='info_items'>
    <h3 class='title'>Инфо</h3>
    <NuxtLink to='/about'>О нас</NuxtLink>
    <NuxtLink to='/delivery'>Оплата и доставка</NuxtLink>
    <NuxtLink to='/sizes'>Размерная сетка</NuxtLink>
  </div>
</template>

<script>
export default {
  name: 'InfoItems'
}
</script>

<style scoped lang='scss'>
.info_items {
  display: flex;
  flex-direction: column;
  margin-right: 51px;
}
.title {
  font-weight: 500;
  font-size: 24px;
  line-height: 29px;
  letter-spacing: 0.13em;
  text-decoration-line: underline;
  text-transform: uppercase;
  color: #fff;
  margin-top: 30px;
  margin-bottom: 30px;
  white-space: nowrap;
}

a:not(:last-child) {
  margin-bottom: 19px;
  white-space: nowrap;
}
</style>
