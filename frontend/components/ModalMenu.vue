<template>
  <div class='menu-wrapper' v-if='show' @click.stop='hideModal'>
    <div class='side-menu' @click.stop>
      <NuxtLink to='/' class='logo_link'>
        <img alt='chili logo' class='logo' src='@/assets/images/logo.png'>
      </NuxtLink>

      <p class='text'>CHILI LINGERIE</p>

      <div class='catalog'>
        <h3 class='catalog__title'>Каталог</h3>
        <ul class='catalog__categories' v-if="categories.length > 0">
          <category-recursive
            v-for='category in categories'
            :key='category.id'
            :category='category'
            class='category'
          />
        </ul>
        <ul v-else class="catalog__categories">
          <li style="padding-left: 12px;">Категорий нет.</li>
        </ul>
      </div>

      <a class='phone' href='tel:+380965342867'>+380 96 534 2867</a>

      <div class='social'>
        <a href='https://telegram.org/' rel='noopener noreferrer' target='_blank'>
          <TelegramIcon />
        </a>
        <a href='https://instagram.com/' rel='noopener noreferrer' target='_blank'>
          <InstagramIcon />
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import toggleMixin from '@/mixins/toggleMixin'
import CategoryRecursive from '@/components/sections/shop/CategoryRecursive'
import TelegramIcon from 'assets/icons/telegram.svg?inline'
import InstagramIcon from 'assets/icons/instagram.svg?inline'

export default {
  name: 'ModalMenu',
  components: { CategoryRecursive, TelegramIcon, InstagramIcon },
  mixins: [toggleMixin],
  props: {
    categories: {
      type: Array,
      required: true
    }
  },
}
</script>

<style scoped lang='scss'>
.menu-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(#000, .35);
  z-index: 1001;
  cursor: pointer;

  font-weight: 300;
  font-size: 18px;
  line-height: 22px;
  letter-spacing: 0.13em;
}

.side-menu {
  display: flex;
  flex-direction: column;
  min-width: 335px;
  max-width: 30%;
  height: 100vh;
  background-color: #000;
  cursor: default;
  padding: 0 24px;
  overflow: hidden;
}

.logo_link {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
}

p.text {
  text-transform: uppercase;
  margin-bottom: 23px;
}

.catalog {
  display: flex;
  flex-direction: column;
  margin-bottom: 23px;

  &__title {
    font-weight: 500;
    text-transform: uppercase;
    margin-bottom: 20px;
  }

  &__categories {
    .category {
      //margin-top: 23px;
      line-height: 35px;
    }
  }
}

.phone {
  margin-bottom: 25px;
}

.social {
  svg {
    width: 30px;
    height: 30px;
  }
  :not(:last-child) {
    margin-right: 14px;
  }
}
</style>
