<template>
  <div class="bg-grey-900 text-white">
    <header class="py-4 px-6">
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

    <div class="grid grid-cols-4">
      <ProductCard v-for="SneakR in chaussures" :SneakR="SneakR" :key="SneakR.id" />
    </div>
    
    <div class="grid grid-cols-4">
      <ProductCard v-for="(SneakR, index) in paginatedChaussures" :key="index" :SneakR="SneakR" />
    </div>

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
</template>

<script>
export default {
  async asyncData({ $supabase }) {
    const { data } = await $supabase.from('chaussures').select("['image.small'], name, estimatedMarketValue").order('brand');
    const perPage = 30;
    const currentPage = 1;
    const totalPages = Math.ceil(data.length / perPage);
    const paginatedChaussures = data.slice((currentPage - 1) * perPage, currentPage * perPage);

    return {
      currentPage,
      totalPages,
      paginatedChaussures
    };
  },
  data() {
    return {
      currentPage: 1,
      totalPages: 0,
      paginatedChaussures: [],
      chaussures: [] // Ajoutez cette ligne pour initialiser la variable chaussures
    };
  },
  methods: {
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.paginatedChaussures = this.getPaginatedChaussures();
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        this.paginatedChaussures = this.getPaginatedChaussures();
      }
    },
    getPaginatedChaussures() {
      const perPage = 30; // Ajoutez cette ligne pour définir le nombre d'éléments par page
      const startIndex = (this.currentPage - 1) * perPage;
      const endIndex = this.currentPage * perPage;
      return this.chaussures.slice(startIndex, endIndex);
    }
  }
};
</script>

<style scoped>
/* ... */
</style>

