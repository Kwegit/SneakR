<template>
  <div class="bg-grey-900 text-white">
    <header class="py-4 px-6">
      <nav class="flex items-center justify-between">
        <div>
          <!-- Logo ou nom du site -->
        </div>
        <div class="ml-auto">
          <!-- Menu -->
          <ul
            class="flex space-x-4 block text-sm font-medium leading-6 text-gray-900"
          >
            <li><a href="#">Accueil</a></li>
            <li><a href="#">Produits</a></li>
            <li><a href="/Contact">Contact</a></li>
            <li><a href="/Login" class="text-white ml-5">Se connecter</a></li>
          </ul>
        </div>
      </nav>
      <div class="flex justify-center mt-5">
        <Searchbar />
      </div>
    </header>

    <div class="grid grid-cols-4">
      <ProductCard v-for="SneakR in chaussures" :SneakR="SneakR" />
    </div>

    <footer class="py-4 px-6">
      <Pagination />
    </footer>
  </div>
</template>

<script setup>
const client = useSupabaseClient();

const { data: chaussures } = await useAsyncData("chaussures", async () => {
  const { data } = await client
    .from("chaussures")
    .select("['image.small'], name, estimatedMarketValue")
    .order("brand")
    .range(0, 30);
  return data;
});
function previousPage() {
  if (this.currentPage > 1) {
    this.currentPage--;
    this.paginatedChaussures = this.getPaginatedChaussures();
  }
}
function nextPage() {
  if (this.currentPage < this.totalPages) {
    this.currentPage++;
    this.paginatedChaussures = this.getPaginatedChaussures();
  }
}
function getPaginatedChaussures() {
  const perPage = 30; // Ajoutez cette ligne pour définir le nombre d'éléments par page
  const startIndex = (this.currentPage - 1) * perPage;
  const endIndex = this.currentPage * perPage;
  return this.chaussures.slice(startIndex, endIndex);
}
</script>

<style scoped>
@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";
.bg-black {
  background-color: rgb(37, 35, 35);
}

.text-white {
  color: rgb(0, 0, 0);
}
</style>
