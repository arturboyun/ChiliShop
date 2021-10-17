<template>
  <div class='product_card'>
    <div class='product_image'>
      <img alt='' :src='image_url'>
    </div>
    <div class='product_info'>
      <NuxtLink class='product_name' to='/shop'>
        {{ title }}
      </NuxtLink>
      <p class='product_price'>{{ price }}<span> ₴</span></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: {
    image_url: {type: String, required: true},
    title: {type: String, required: true},
    price: {type: Number, required: true},
  }
}
</script>

<style scoped lang='scss'>
.product_card {
  display: flex;
  flex-direction: column;
}

.product_image {
  position: relative;
  margin-bottom: 7px;
  cursor: pointer;

  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    width: 100%;
    height: 284px;
    background-color: red;
    transition: .3s ease;
  }

  &:hover {
    &::after {
      opacity: .15;
    }
  }

  img {
    height: 284px;
  }
}

.product_info {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.product_name {
  line-height: 18px;
  font-weight: 500;
  font-size: 14px;
  align-self: flex-start;
}

.product_price {
  font-size: 16px;
  font-weight: 600;
  white-space: nowrap;
}
</style>
