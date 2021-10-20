<template>
  <div class='about info_container'>
    <info-items />
    <info-text>
      <p>
        . Chili – украинский бренд белья для стильных и уверенных в себе девушек, которые привыкли добиваться своих
        целей
        и не идти на компромиссы.
      </p>
      <p>
        Высокое качество всех наших изделий, выполненных на одном из лучших текстильных производств в Украине, в
        сочетании с уникальными дизайнами дает непревзойдённую комбинацию комфорта, технологичности и красоты для нашего
        белья.
      </p>
      <p>Белье Chili – это авторский микс удобного и, одновременно, соблазнительного нижнего белья.</p>
      <p>
        Не отказывайте себе в удовольствии иметь не только комфортные и практичные вещи, но и не менее стильные и
        привлекательные. А с Chili это очень легко.
      </p>
    </info-text>
  </div>
</template>

<script>
import InfoItems from '@/components/sections/info/InfoItems'
import InfoText from '@/components/sections/info/InfoText'

export default {
  name: 'About',
  components: { InfoText, InfoItems }
}
</script>

<style scoped>
.about {
}
</style>
