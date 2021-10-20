<template>
  <div class='info_text'>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'InfoText'
}
</script>

<style scoped>
.info_text {
  background-color: #1c1c1c;
  padding: 30px 40px;
  min-height: 60vh;
}

p {
  font-weight: 300;
  font-size: 18px;
  line-height: 22px;
  letter-spacing: 0.13em;
  margin-bottom: 30px;
}
</style>
