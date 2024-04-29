<template>
    <div>
        <p>Count: {{ count }}</p>
        <button @click="increment">Increment</button>
        <br />
        <button @click="decrement">Decrement</button>
        <sidebar />
    </div>
</template>

<script setup>
import { reactive, ref, computed } from 'vue';
import { useCounterStore } from '@/store';

const counterStore = useCounterStore();
const count = computed(() => counterStore.count);
const increment = counterStore.increment;
const decrement = counterStore.decrement;
</script>

<style scoped></style>
