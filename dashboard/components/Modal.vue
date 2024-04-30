<template>
    <div class="modal-wrapper p-3 rounded-xl">
        <div @click="$emit('onToggle')" class="flex absolute inset-0 z-0" />
        <div class="w-full max-w-lg p-3 relative mx-auto my-auto rounded-xl">
            <div>
                <div class="flex justify-between items-center modal-header">
                    <div>
                        <h1 class="font-semibold text-2xl">Add Location</h1>
                    </div>
                    <div class="flex flex-row-reverse p-1 close-icon-wrapper rounded-lg">
                        <svg
                            @click="$emit('onToggle')"
                            class="w-6 h-6 close-icon"
                            stroke="currentColor"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path stroke-width="1.5" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </div>
                </div>
                <div class="mt-5 min-w-80 input-wrapper">
                    <custom-input @input-changed="handleChange" :selected="selected" />
                </div>
                <div class="text-center space-x-4 md:block">
                    <button
                        @click="addLocation"
                        class="w-full mb-2 text-sm text-background font-bold add-location-button rounded-lg"
                    >
                        Add Location
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useStore } from '@/store';

const emit = defineEmits(['onToggle']);
const selected = ref(null);

const mainStore = useStore();

const handleChange = (newValue) => {
    selected.value = newValue;
};

const addLocation = () => {
    if (selected.value != null) {
        const request = {
            name: selected.value.country,
            capital: selected.value.capital,
            latitude: selected.value.latitude,
            longitude: selected.value.longitude,
        };

        //TODO: Handle errors to display from a toast
        mainStore.addLocation(request);

        emit('onToggle');
        selected.value = null;
    } else {
        alert('Please choose a location!');
    }
};
</script>

<style scoped>
.modal-wrapper {
    background-color: #1b1b1d;
}
.add-location-button {
    background-color: #d4e8f8;
    /* color: #111015; */
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
text-background .add-location-button:hover {
    background-color: #a7d0f1;
}

.close-icon-wrapper {
    background-color: #252528;
}

.close-icon:hover {
    cursor: pointer;
    opacity: 0.8;
}
</style>
