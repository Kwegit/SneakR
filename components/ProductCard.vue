<template>
  <div class="py-6">
    <div class="flex max-w-md bg-white shadow-lg rounded-lg overflow-hidden">
      <img class="w-1/3 bg-cover" :src="SneakR['image.small']" />
    </div>
    <div class="w-2/3 p-4">
      <h1 class="text-gray-900 font-bold text-2xl">{{ SneakR.name }}</h1>
      <p class="mt-2 text-gray-600 text-sm"></p>

      <div class="flex item-center justify-between mt-3">
        <h1 class="text-gray-700 font-bold text-xl">
          {{ SneakR.estimatedMarketValue }}
        </h1>
        <button
          class="px-3 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded"
        >
          Add to Cart
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(["SneakR"]);
</script>
