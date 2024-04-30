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
            <v-select
                :options="countries"
                label="country"
                v-model="selected"
                placeholder="Search..."
                @input="inputChanged"
            />
        </div>
    </form>
</template>

<script setup>
import 'vue-select/dist/vue-select.css';
import vSelect from 'vue-select';
import { ref, defineEmits, watch, computed } from 'vue';
import { useStore } from '@/store';

const selected = ref(null);
const counterStore = useStore();

const emit = defineEmits(['input-changed']);

const inputChanged = () => {
    emit('input-changed', selected.value);
};

watch(selected, (newValue) => {
    emit('input-changed', newValue);
});

const countries = computed(() => counterStore.countries);
</script>

<style scoped>
.custom-input {
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
