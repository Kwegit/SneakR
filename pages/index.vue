<template>
  <div class="bg-grey-900 text-white">
    <header class="py-4 px-6 ">
      <nav class="flex items-center justify-between">
        <div>
          <!-- Logo ou nom du site -->
        </div>
        <div class="ml-auto">
          <!-- Menu -->
          <ul class="flex space-x-4">
            <li><a href="#">Accueil</a></li>
            <li><a href="#">Produits</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Panier</a></li>
            <li><a href="#" class="text-white ml-4">Se connecter</a></li>
          </ul>
        </div>
      </nav>
      <div class="flex justify-center mt-5">
        <!-- Barre de recherche -->
        <input type="text" placeholder="Rechercher" class="bg-white ml-5 h-11 w-full transform border-b-2 border-light-gray text-xl font-semibold transition hover:border-b-2 hover:border-black focus:border-b-2 focus:border-black focus:outline-none md:ml-12">
      </div>
      <div class="flex justify-end mt-4">
       
        <!-- Login -->
        
      </div>
    </header>

    <main class="py-8 px-6">
      <!-- Contenu du main -->
      <div>
   <ProductCard />
      </div>
   
    </main>

    <footer class="py-4 px-6 ">
      <!-- Contenu du footer -->
    </footer>

  </div>
</template>

<script>
export default {
  name: 'App',
  // Composants, méthodes, etc.
}
</script>

<style scoped>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

/* Styles spécifiques au site vitrine */
.bg-black {
  background-color: rgb(37, 35, 35);
}

.text-white {
  color: rgb(172, 80, 193);
}

/* Autres styles personnalisés */
</style>