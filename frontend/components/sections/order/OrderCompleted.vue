<template>
  <div class='order_completed'>
    <div class='title'>Статус заказа</div>
    <div class='text'>Ваш заказ успешно создан. После отправки заказа вам придет смс с номером вашей ТТН.</div>
  </div>
</template>

<script>
export default {
  name: 'OrderCompleted',
  mounted() {
    setTimeout(() => {
      this.$router.push({
        path: '/'
      })
    }, 15000)
  }
}
</script>

<style lang='scss' scoped>
.order_completed {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;

  .title,
  .text {
    font-weight: 500;
    font-size: 24px;
    line-height: 29px;
    letter-spacing: 0.13em;
    color: #fff;
  }

  .text {
    width: 532px;
  }
}
</style>
