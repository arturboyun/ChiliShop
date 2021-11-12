<template>
  <div class="categories">
    <h1 class="title">Категории</h1>
    <it-button class="create-category-btn" type="primary" round
      >Создать Категорию</it-button
    >
    <Table />
  </div>
</template>

<script>
import Table from '../components/items/Table';
export default {
  components: { Table },
};
</script>

<style lang="scss" scoped>
.categories {
  width: 100%;
  .title {
    margin-bottom: 25px;
  }

  .create-category-btn {
    margin-bottom: 15px;
  }
}
</style>
