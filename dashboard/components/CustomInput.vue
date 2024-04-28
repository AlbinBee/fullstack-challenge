<template>
    <form class="py-5 max-w-md mx-auto">
        <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none z-50">
                <svg
                    class="w-4 h-4 text-gray-500 dark:text-gray-400"
                    aria-hidden="true"
                    fill="none"
                    viewBox="0 0 20 20"
                >
                    <path stroke="currentColor" stroke-width="1.5" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                </svg>
            </div>
            <v-select :options="locations" label="name" v-model="selected" placeholder="Search..." @input="doSom" />
        </div>
    </form>
</template>

<script setup>
import 'vue-select/dist/vue-select.css';
import vSelect from 'vue-select';

import { ref, defineEmits, watch } from 'vue';

const selected = ref(null);

const emit = defineEmits(['input-changed']);

const doSom = () => {
    emit('input-changed', selected.value);
};

watch(selected, (newValue) => {
    emit('input-changed', newValue);
});

const locations = [
    { id: 1, name: 'Beijing', temperature: 13, rainfall: 0 },
    { id: 2, name: 'Berlin', temperature: 15, rainfall: 20 },
    { id: 3, name: 'Buenos Aires', temperature: 22, rainfall: 0 },
    { id: 4, name: 'Cairo', temperature: 24, rainfall: 3 },
    { id: 5, name: 'Cape Town', temperature: 24, rainfall: 0 },
    { id: 6, name: 'Istanbul', temperature: 12, rainfall: 0 },
    { id: 7, name: 'London', temperature: 14, rainfall: 20 },
    { id: 8, name: 'Madrid', temperature: 16, rainfall: 0 },
];
</script>

<style scoped>
.custom-input {
    border: none;
    background-color: #313030;
}
:deep(.vs__search::placeholder) {
    color: #cbd5e1;
}
:deep(.vs__dropdown-toggle) {
    background-color: #313030;
}
:deep(.vs__selected) {
    padding-left: 30px;
    color: white;
}
:deep(.vs__search) {
    padding-left: 30px;
    color: white;
}
:deep(.vs__dropdown-menu) {
    color: black;
    padding-top: 2px;
    padding-bottom: 2px;
}
</style>
