<template>
  <div class="table">
    <table>
      <tr>
        <th>ID</th>
        <th>ID Родителя</th>
        <th>Имя</th>
        <th>Заголовок</th>
        <th>Slug</th>
        <th>Подкатегорий</th>
        <th>Действия</th>
      </tr>
      <tr v-for="(category, index) in categories" :key="index">
        <td>{{ category.id }}</td>
        <td>{{ category.parent_id || 0 }}</td>
        <td>{{ category.name }}</td>
        <td>{{ category.title }}</td>
        <td>{{ category.slug }}</td>
        <td>{{ category.children.length }}</td>
        <td>
          <div class="actions">
            <it-button type="primary" icon="edit" />
            <it-button type="danger" icon="delete" />
            <router-link
              v-if="category.children.length > 0"
              :to="`/category/${category.slug}/`"
            >
              <it-button type="black" icon="visibility" />
            </router-link>
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  name: 'CategoriesTable',
  props: { categories: { type: Array, required: true } },
  setup(props) {
    return { props };
  },
};
</script>
<style scoped lang="scss"></style>
