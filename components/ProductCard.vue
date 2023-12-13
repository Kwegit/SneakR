<template>
  <div class="py-6 flex flex-col pr-4">
    <div class="flex max-w-md bg-white shadow-lg rounded-lg overflow-hidden">
      <img class="bg-cover" :src="SneakR['image.small']" />
    </div>
    <div class="p-4">
      <h1 class="text-gray-900 font-bold text-2xl">
        {{ SneakR.brand }} {{ SneakR.silhouette }}
      </h1>
      <p class="mt-2 text-gray-600 text-sm"></p>

      <div class="flex item-center justify-between mt-3">
        <h1 class="text-gray-700 font-bold text-xl">
          {{ SneakR.estimatedMarketValue }} €
        </h1>
        <button
          @click="addToCollection"
          class="px-3 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded"
        >
          Add to Collection
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(["SneakR"]);
const emits = defineEmits(["addToCollection"]);

const addToCollection = () => {
  emits.addToCollection(props.SneakR);
};
</script>
