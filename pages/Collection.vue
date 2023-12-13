// In pages/favorites.vue
<template>
  <div>
    <Header />
    <div class="flex flex-wrap justify-center">
      <div class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4 p-6 flex flex-col">
        <ProductCard @add-to-Collection="" v-for="sneakr in favorites" :key="sneakr.id" :SneakR="sneakr" @addToCollection="addToCollection" />
      </div>
    </div>
  </div>
</template>

<script setup>

</script>
