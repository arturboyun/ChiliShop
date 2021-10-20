<template>
  <div class='product_card'>
    <NuxtLink class='product_image_link' :to='`/shop/product/${slug}`'>
      <div class='product_image' :style='`background-image: url("${image_url}");`'>
        <div class='cover'><span>Посмотреть</span></div>
      </div>
    </NuxtLink>

    <div class='product_info'>
      <NuxtLink class='product_name' :to='`/shop/product/${slug}`'>
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
    slug: {type: String, required: true},
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
  width: 207px;
  height: 283px;
  position: relative;
  margin-bottom: 7px;
  cursor: pointer;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;

  img {
    height: 284px;
  }

  .cover {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-weight: 500;
    top: 0;
    left: 0;
    opacity: 0;
    width: 100%;
    height: 283px;
    background-color: rgba(red, 0);
    transition: .25s ease;
    z-index: 3;
  }

  .cover:hover {
    background-color: rgba(red, .10);
    opacity: 1;

    span {
      padding: 5px;
      border: 2px solid #fff;
    }
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
