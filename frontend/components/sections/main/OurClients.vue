<template>
  <div class="our_clients">
    <h2 class="title">Наши клиенты</h2>
    <img alt="chili logo" class="logo" src="~/assets/images/logo.png">
    <div class="gallery">
      <img src="~/assets/images/gallery-image-1.png" alt="none" class="gallery__image">
      <img src="~/assets/images/gallery-image-1.png" alt="none" class="gallery__image">
      <img src="~/assets/images/gallery-image-1.png" alt="none" class="gallery__image">
      <img src="~/assets/images/gallery-image-1.png" alt="none" class="gallery__image">
      <img src="~/assets/images/gallery-image-1.png" alt="none" class="gallery__image">
      <img src="~/assets/images/gallery-image-1.png" alt="none" class="gallery__image">
    </div>
  </div>
</template>

<script>
export default {
  name: "OurClients"
}
</script>

<style lang="scss" scoped>
.our_clients {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 60px 270px 0;
  background-color: #000000;

  @media screen and (max-width: 1200px) {
    padding: 0 15px;
    .title {
      font-size: 14px;
    }
    .logo {
      width: 84px;
      height: 56px;
    }
  }
}

.title {
  font-size: 36px;
  line-height: 36px;
  font-weight: 500;
  margin: 0;
  color: #fff;
  text-transform: uppercase;
  white-space: nowrap;
}

.logo {
  margin-bottom: 8px;
}

.gallery {
  display: grid;
  grid-gap: 94px 91px;
  grid-template-columns: 271px 271px 271px;
  margin-bottom: 74px;

  @media screen and (max-width: 1200px) {
    grid-gap: 34px 34px;
    grid-template-columns: auto auto;
  }

  &__image {

  }
}
</style>
