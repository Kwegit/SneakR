<template>
 <div class="home">
    <header class="flex justify-between items-center py-4 px-6 bg-gray-900">
      <!-- Barre de recherche -->
      <input type="text" placeholder="Rechercher" class="px-4 py-2 rounded-lg bg-gray-800 text-white focus:outline-none focus:bg-gray-700">

      <!-- Panier -->
      <div class="relative">
        <button class="flex items-center text-white">
          <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24">
            <!-- Icône du panier -->
          </svg>
          <span class="ml-1">Panier</span>
        </button>
        <!-- Afficher le nombre d'articles dans le panier -->
        <span class="absolute top-0 right-0 bg-red-500 text-white rounded-full px-2 py-1 text-xs">3</span>
      </div>
    </header>

    <h1 class="text-3xl font-bold text-white mt-8 mb-4">Bienvenue sur notre site de sneakers !</h1>

    <div class="product-list">
      <!-- Ici, vous afficherez les produits -->
    </div>
  </div>
</template>

<script>

</script>

<style scoped>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

.home {
  background-color: black;
  color: mauve;
}

/* .product-list {
    /* Add your styles for the product list here */


</style>
