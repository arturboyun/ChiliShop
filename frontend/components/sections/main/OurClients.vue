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
}

.title {
  font-size: 36px;
  line-height: 36px;
  font-weight: 500;
  margin: 0;
  color: #fff;
  text-transform: uppercase;
}

.logo {
  margin-bottom: 8px;
}

.gallery {
  display: grid;
  grid-gap: 94px 91px;
  grid-template-columns: auto auto auto;
  margin-bottom: 74px;

  &__image {

  }
}
</style>
