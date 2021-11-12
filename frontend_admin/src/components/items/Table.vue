<template>
  <div class="table">
    <table>
      <tr>
        <th>ID</th>
        <th>Имя</th>
        <th>Заголовок</th>
        <th>Slug</th>
        <th>Родитель</th>
        <th>Действия</th>
      </tr>
      <tr>
        <td>1</td>
        <td>Title</td>
        <td>Slug</td>
        <td>Slug</td>
        <td>Slug</td>
        <td>
          <div class="actions">
            <it-button type="primary" icon="edit" />
            <it-button type="danger" icon="delete" />
          </div>
        </td>
      </tr>
      <tr>
        <td>2</td>
        <td>Title</td>
        <td>Slug</td>
        <td>Slug</td>
        <td>Slug</td>
        <td>
          <div class="actions">
            <it-button type="primary" icon="edit" />
            <it-button type="danger" icon="delete" />
          </div>
        </td>
      </tr>
      <tr>
        <td>3</td>
        <td>Title</td>
        <td>Slug</td>
        <td>Slug</td>
        <td>Slug</td>
        <td>
          <div class="actions">
            <it-button type="primary" icon="edit" />
            <it-button type="danger" icon="delete" />
          </div>
        </td>
      </tr>
      <tr>
        <td>4</td>
        <td>Title</td>
        <td>asdasdasd</td>
        <td>asdadsads</td>
        <td>adssad</td>
        <td>
          <div class="actions">
            <it-button type="primary" icon="edit" />
            <it-button type="danger" icon="delete" />
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Table',
};
</script>

<style scoped lang="scss">
.table {
  overflow-x: auto;
  padding: 25px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 3px 5px rgba(#000, 0.2);

  table {
    border-collapse: collapse;
    width: 100%;
  }
  th,
  td {
    text-align: left;
    padding: 12px 8px;
  }

  tr:not(:last-child) {
    border-bottom: 1px solid rgba(#3a3a3a, 0.2);
  }

  .actions {
    display: flex;

    & > *:not(:last-child) {
      margin-right: 15px;
    }
  }
}
</style>
