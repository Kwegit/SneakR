<template>
  <div>
    <input type="text" v-model="searchTerm" placeholder="Rechercher" class="bg-white ml-5 h-11 w-full transform border-b-2 border-light-gray text-xl font-semibold transition hover:border-b-2 hover:border-black focus:border-b-2 focus:border-black focus:outline-none md:ml-12">
    <div v-if="searchTerm !== '' && searchResults.length > 0">
      <h2>Résultats de la recherche :</h2>
      <ul>
        <li v-for="result in searchResults" :key="result.id">{{ result.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>


export default {
  setup() {
    const searchTerm = ref('');
    const searchResults = ref([]);

    const supabase  = useSupabaseClient();

    const searchChaussures = async () => {
      const { data, error } = await supabase
        .from('chaussures')
        .select('name')
        .ilike('name', `%${searchTerm.value}%`);

      if (error) {
        console.error(error);
        return;
      }

      searchResults.value = data;
    };

    return {
      searchTerm,
      searchResults,
      searchChaussures
    };
  },
  watch: {
    searchTerm: {
      handler: 'searchChaussures',
      immediate: true
    }
  }
};
</script>

<style scoped>
</style>