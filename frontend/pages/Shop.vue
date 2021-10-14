<template>
  <div class="shop">
    <div class="categories">
      <h2 class="title">Категории</h2>
      <ul>
        <li>
          <div class="name">Category</div>
          <ul class="sub_categories">
            <li>
              <div class="name">Category</div>
              <ul class="sub_categories"></ul>
            </li>
          </ul>
        </li>
        <li>
          <div class="name">Category</div>
          <ul class="sub_categories">
            <li>
              <div class="name">Category</div>
              <ul class="sub_categories">
                <li>
                  <div class="name">Category</div>
                  <ul class="sub_categories"></ul>
                </li>
                <li>
                  <div class="name">Category</div>
                  <ul class="sub_categories"></ul>
                </li>
                <li>
                  <div class="name">Category</div>
                  <ul class="sub_categories"></ul>
                </li>
              </ul>
            </li>
            <li>
              <div class="name">Category</div>
              <ul class="sub_categories"></ul>
            </li>
            <li>
              <div class="name">Category</div>
              <ul class="sub_categories"></ul>
            </li>
          </ul>
        </li>
        <li>
          <div class="name">Category</div>
          <ul class="sub_categories">
            <li>
              <div class="name">Category</div>
              <ul class="sub_categories"></ul>
            </li>
          </ul>
        </li>
      </ul>
    </div>

    <div class="products">
      <h1 class="title">НИЖНЕЕ БЕЛЬЁ CHILI</h1>
      <div class="products_grid">
        <div class="product_card">
          <div class="product_image">
            <img alt="" src="~/assets/images/gallery-image-1.png">
          </div>
          <div class="product_info">
            <NuxtLink to="/shop" class="product_name">
              Комлект бюст с чашками и слипы, бежевый
            </NuxtLink>
            <p class="product_price">980<span> ₴</span></p>
          </div>
        </div>
        <div class="product_card">
          <div class="product_image">
            <img alt="" src="~/assets/images/gallery-image-1.png">
          </div>
          <div class="product_info">
            <NuxtLink to="/shop" class="product_name">
              Комлект бюст с чашками и слипы, бежевый
            </NuxtLink>
            <p class="product_price">980<span> ₴</span></p>
          </div>
        </div>
        <div class="product_card">
          <div class="product_image">
            <img alt="" src="~/assets/images/gallery-image-1.png">
          </div>
          <div class="product_info">
            <NuxtLink to="/shop" class="product_name">
              Комлект бюст с чашками и слипы, бежевый
            </NuxtLink>
            <p class="product_price">980<span> ₴</span></p>
          </div>
        </div>
        <div class="product_card">
          <div class="product_image">
            <img alt="" src="~/assets/images/gallery-image-1.png">
          </div>
          <div class="product_info">
            <NuxtLink to="/shop" class="product_name">
              Комлект бюст с чашками и слипы, бежевый
            </NuxtLink>
            <p class="product_price">980<span> ₴</span></p>
          </div>
        </div>
        <div class="product_card">
          <div class="product_image">
            <img alt="" src="~/assets/images/gallery-image-1.png">
          </div>
          <div class="product_info">
            <NuxtLink to="/shop" class="product_name">
              Комлект бюст с чашками и слипы, бежевый
            </NuxtLink>
            <p class="product_price">980<span> ₴</span></p>
          </div>
        </div>
        <div class="product_card">
          <div class="product_image">
            <img alt="" src="~/assets/images/gallery-image-1.png">
          </div>
          <div class="product_info">
            <NuxtLink to="/shop" class="product_name">
              Комлект бюст с чашками и слипы, бежевый
            </NuxtLink>
            <p class="product_price">980<span> ₴</span></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Shop",
  data() {
    return {
      categories: {}
    }
  }
}
</script>

<style lang="scss" scoped>
.shop {
  min-height: 70vh;
  padding: 50px 270px;
  display: flex;
  background-color: #080808;
}

.title {
  font-size: 18px;
  font-weight: 500;
  line-height: 18px;
  color: #ffffff;
  margin-bottom: 31px;
}

.categories {
  width: 20%;
  margin-bottom: 15px;

  .sub_categories > li {
    margin-left: 25px;
  }
}

.products {
  width: 80%;
  padding: 21px 38px;
  background-color: #1c1c1c;
}

.products_grid {
  display: grid;
  grid-gap: 48px 28px;
  grid-template-columns: auto auto auto auto;
}

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
}

.product_name {
  line-height: 14px;
  font-weight: 500;
  font-size: 14px;
}

.product_price {
  font-size: 16px;
  font-weight: 600;
  white-space: nowrap;
}

</style>
