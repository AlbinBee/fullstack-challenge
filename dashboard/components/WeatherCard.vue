<template>
    <div class="flex items-center justify-between weather-card">
        <div class="flex items-center">
            <img :src="props.weatherIconUrl" alt="weather-condition" />
            <h1 class="ml-4 text-2xl font-semibold">{{ props.weatherDay }}</h1>
        </div>
        <div>
            <div class="w-full mb-1 flex items-center justify-between">
                <p class="text-zinc-400 text-sm">Min.</p>
                <h5 class="text-sm ml-2">{{ props.weatherMin }}°C</h5>
            </div>
            <div class="w-full mb-1 flex items-center justify-between">
                <p class="text-zinc-400 text-sm">Max.</p>
                <h5 class="w-full ml-2 text-sm">{{ props.weatherMax }}°C</h5>
            </div>
            <div class="w-full flex items-center justify-between">
                <p class="text-zinc-400 text-sm">Rain</p>
                <h5 class="w-full ml-2 text-sm">{{ props.rain }}mm</h5>
            </div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

// Declare the 'weatherIconUrl' prop
const props = defineProps({
    weatherIconUrl: String,
    weatherDay: String,
    weatherMin: Number,
    weatherMax: Number,
    rain: Number,
});
</script>

<style scoped>
.weather-card {
    height: 80px;
    margin-bottom: 12px;
    background-color: #323232;
    border-radius: 15px;
    padding: 20px;
}
</style>
