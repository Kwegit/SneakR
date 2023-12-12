<template>
  <div class="bg-grey-900">
    <Header />
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
      <ProductCard v-for="SneakR in chaussures" :SneakR="SneakR" />
    </div>

    <footer class="py-8 px-10">
<UPagination size="md" v-model="current_pagination" :page-count="28" :max="8" :total="49214" show-last show-first />
    </footer>
  </div>
</template>

<script setup lang="ts">

const client = useSupabaseClient();
const current_pagination = ref(1);
const sneakersPerPage = 28;

const { data: chaussures } = await useAsyncData("chaussures", async () => {
  const { data } = await client
    .from("chaussures")
    .select("['image.small'], name, estimatedMarketValue")
    .order("brand")
    .range(0, 30);
  return data;
});

watch(current_pagination, async () => {
  const { data: chaussures } = await useAsyncData("chaussures", async () => {
    const { data } = await client
      .from("chaussures")
      .select("*")
      .range(current_pagination.value * sneakersPerPage - sneakersPerPage, current_pagination.value * sneakersPerPage - 1);
    window.scrollTo(0, 0);
    return data;
  });
});


</script>

<style scoped>
@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";
.bg-black {
  background-color: rgb(37, 35, 35);
}
</style>
