<template>
  <div class="footer">
    <div class="col">
      <h3 class="col__title">Инфо</h3>
      <NuxtLink to="/about">О нас</NuxtLink>
      <NuxtLink to="/delivery">Оплата и доставка</NuxtLink>
      <NuxtLink to="/sizes">Размерная сетка</NuxtLink>
    </div>
    <div class="col">
      <h3 class="col__title">Главное Меню</h3>
      <NuxtLink to="/about">Нижнее бельё</NuxtLink>
      <NuxtLink to="/delivery">Пижамы</NuxtLink>
      <NuxtLink to="/sizes">Халаты</NuxtLink>
      <NuxtLink to="/sizes">Купальники</NuxtLink>
      <NuxtLink to="/sizes">SALE</NuxtLink>
    </div>
    <div class="col">
      <h3 class="col__title">Контакты</h3>
      <a href="tel:+380965342867">+38 096 534 28 67</a>
      <div class="social">
        <a href="https://telegram.org/" target="_blank" rel="noopener noreferrer"><TelegramIcon/></a>
        <a href="https://instagram.com/" target="_blank" rel="noopener noreferrer"><InstagramIcon/></a>
      </div>
    </div>
  </div>
</template>

<script>
import TelegramIcon from '~/assets/icons/telegram.svg?inline';
import InstagramIcon from '~/assets/icons/instagram.svg?inline';

export default {
  name: "Footer",
  components: {TelegramIcon, InstagramIcon}
}
</script>

<style scoped lang="scss">
.footer {
  display: flex;
  width: 100%;
  padding: 0 270px;
  margin-top: 45px;
  margin-bottom: 35px;
  background-color: #1c1c1c;
}

.col {
  display: flex;
  flex-direction: column;

  &:not(:last-child) {
    margin-right: 232px;
  }

  &:nth-child(2) {
    margin-right: 330px;
  }

  & > *:not(:last-child) {
    margin-bottom: 30px;
  }

  a {
    font-weight: 300;
  }

  .social {
    :not(:last-child) {
      margin-right: 14px;
    }
  }
}
</style>
