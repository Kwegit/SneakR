<template>
  <div class="bg-grey-900 text-white ">
    <header class="py-4 px-6 ">
      <nav class="flex items-center justify-between">
        <div>
          <!-- Logo ou nom du site -->
        </div>
        <div class="ml-auto">
          <!-- Menu -->
          <ul class="flex space-x-4 block text-sm font-medium leading-6 text-gray-900">
            <li><a href="#">Accueil</a></li>
            <li><a href="#">Produits</a></li>
            <li><a href="/Contact">Contact</a></li>
            <li><a href="/Login" class="text-white ml-5">Se connecter</a></li>
          </ul>
        </div>
      </nav>
      <div class="flex justify-center mt-5">
        <!-- Barre de recherche -->
        <input type="text" placeholder="Rechercher" class="bg-white ml-5 h-11 w-full transform border-b-2 border-light-gray text-xl font-semibold transition hover:border-b-2 hover:border-black focus:border-b-2 focus:border-black focus:outline-none md:ml-12">
      </div>
    </header>

      <div class="grid grid-cols-4  ">
        <ProductCard v-for="SneakR in chaussures" :SneakR="SneakR" />
      </div>
    

    <footer class="py-4 px-6 ">
     <div class="grid grid-cols-4">
      <ProductCard v-for="(SneakR, index) in paginatedChaussures" :key="index" :SneakR="SneakR" />
    </div>

    <div class="flex justify-center mt-5">
      <!-- Pagination -->
      <nav>
        <ul class="flex space-x-2">
          <li>
            <button @click="previousPage" :disabled="currentPage === 1">Previous</button>
          </li>
          <li>
            <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
          </li>
        </ul>
      </nav>
    </div>
    </footer>
  </div>
</template>

<script setup>
const client = useSupabaseClient()

const { data: chaussures } = await useAsyncData("chaussures", async () => {
  const { data } = await client.from("chaussures").select("['image.small'], name, estimatedMarketValue").order("brand").range(0, 30);
  return data;
});



</script>

<style scoped>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
.bg-black {
  background-color: rgb(37, 35, 35);
}

.text-white {
  color: rgb(172, 80, 193);
}
</style>
