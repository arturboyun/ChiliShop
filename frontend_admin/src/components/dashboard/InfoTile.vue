<template>
  <div class="tile" :style="{ backgroundColor: color }">
    <div class="col">
      <it-icon box class="icon" :name="iconName" />
    </div>
    <div class="col">
      <h2 class="title">{{ title }}</h2>
      <div class="numbers">{{ numbers }} шт.</div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    iconName: { type: String, required: true },
    title: { type: String, required: true },
    color: { type: String, required: true },
    numbers: { type: [String, Number], required: true },
  },
};
</script>
<style scoped lang="scss">
.tile {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 35px;
  border-radius: 12px;
  box-shadow: 0 5px 12px rgba(#000, 0.25);
  transition: all 0.5s ease;
  color: #fff;

  .col {
    display: flex;
    flex-direction: column;
  }

  .icon {
    padding: 0;
    margin-right: 25px;
    font-size: 32px;
  }

  .title {
    font-weight: 500;
    margin-bottom: 8px;
  }

  .numbers {
    font-size: 18px;
    font-weight: 800;
  }

  &:hover {
    transform: translateY(-3px);
  }
}
</style>
