<template>
  <div class='footer'>
    <div class='col'>
      <h3 class='col__title'>Инфо</h3>
      <NuxtLink to='/about'>О нас</NuxtLink>
      <NuxtLink to='/delivery'>Оплата и доставка</NuxtLink>
      <NuxtLink to='/sizes'>Размерная сетка</NuxtLink>
    </div>
    <div class='col'>
      <h3 class='col__title'>Главное Меню</h3>
      <div v-if="categories.length > 0" class="categories">
        <NuxtLink
          v-for='category in categories'
          :to='`/shop/category/${category.slug}`'
          :key='category.id'
        >
          {{ category.name }}
        </NuxtLink>
      </div>
      <p v-else>Категорий нет.</p>
    </div>
    <div class='col'>
      <h3 class='col__title'>Контакты</h3>
      <a href='tel:+380672345959'>+380 (67) 234 59 59</a>
      <div class='social'>
        <a href='https://t.me/chililingerie' rel='noopener noreferrer' target='_blank'>
          <TelegramIcon />
        </a>
        <a href='https://instagram.com/chili_kv?utm_medium=copy_link' rel='noopener noreferrer' target='_blank'>
          <InstagramIcon />
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import TelegramIcon from '~/assets/icons/telegram.svg?inline'
import InstagramIcon from '~/assets/icons/instagram.svg?inline'

export default {
  name: 'Footer',
  components: { TelegramIcon, InstagramIcon },
  props: {
    categories: {
      type: Array,
      required: true
    }
  }
}
</script>

<style lang='scss' scoped>
.footer {
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding: 0 270px;
  margin-top: 45px;
  margin-bottom: 35px;
  background-color: #1c1c1c;

  @media screen and (max-width: 1200px) {
    padding: 0 15px;
  }

  @media screen and (max-width: 720px) {
    flex-direction: column;

    .col {
      margin-bottom: 50px;
    }
  }
}

.col {
  display: flex;
  flex-direction: column;
  width: 232px;
  margin-right: 25px;
  //
  //&:not(:last-child) {
  //  margin-right: 232px;
  //}
  //
  //&:nth-child(2) {
  //  margin-right: 330px;
  //}

  & > *:not(:last-child) {
    margin-bottom: 30px;
  }

  a {
    font-weight: 300;
    cursor: pointer;

    &:hover {
      color: #d94a4a;
    }
  }

  .social {
    :not(:last-child) {
      margin-right: 14px;
    }
  }

  @media screen and (max-width: 1200px) {
    & > *:not(:last-child) {
      margin-bottom: 12px;
    }
  }
}

.categories {
  display: flex;
  flex-direction: column;
}

</style>
