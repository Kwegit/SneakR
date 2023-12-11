<template>
  <div>
    <div class="grid grid-cols-4">
      <ProductCard v-for="product in paginatedChaussures" :key="product.id" :product="product" />
    </div>

    <div class="flex justify-center mt-5">
      <button @click="previousPage" :disabled="currentPage === 1" class="px-3 py-2 bg-gray-300 text-gray-700 rounded-l-md">Previous</button>
      <button @click="nextPage" :disabled="currentPage === totalPages" class="px-3 py-2 bg-gray-300 text-gray-700 rounded-r-md">Next</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPage: 1,
      perPage: 30, // Nombre d'éléments par page
      chaussures: [], // Vos données de chaussures
      paginatedChaussures: [] // Chaussures paginées à afficher
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.chaussures.length / this.perPage);
    }
  },
  mounted() {
    this.paginatedChaussures = this.getPaginatedChaussures();
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
      const startIndex = (this.currentPage - 1) * this.perPage;
      const endIndex = this.currentPage * this.perPage;
      return this.chaussures.slice(startIndex, endIndex);
    }
  }
};
</script>

<style scoped>
/* ... */
</style>