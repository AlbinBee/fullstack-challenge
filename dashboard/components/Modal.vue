<template>
    <div v-if="isModalVisible" class="modal-wrapper p-3">
        <!-- <div class="modal-wrapper p-3"> -->
        <div @click="$emit('onToggle')" class="flex absolute inset-0 z-0" />
        <div class="w-full max-w-lg p-3 relative mx-auto my-auto rounded-xl">
            <div>
                <div class="flex justify-between items-center modal-header">
                    <div>
                        <h1 class="font-semibold text-2xl">Add Location</h1>
                    </div>
                    <div class="flex flex-row-reverse close-icon-wrapper">
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
                    <button @click="addLocation" class="w-full mb-2 text-sm font-bold remove-location-button">
                        Add Location
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, defineProps } from 'vue';

const emit = defineEmits(['onToggle']);
const selected = ref(null);
const props = defineProps({
    isModalOpen: Boolean,
});

const isModalVisible = computed(() => {
    return props.isModalOpen;
});

const addLocation = () => {
    if (selected.value != null) {
        alert(`added location: ${selected.value.name}`);
        emit('onToggle');
    } else {
        alert('Please choose a location!');
    }
};

const handleChange = (newValue) => {
    selected.value = newValue;
};
</script>

<style scoped>
.modal-wrapper {
    border-radius: 10px;
    background-color: #1b1b1d;
}
.remove-location-button {
    background-color: #d4e8f8;
    color: #111015;
    border: none;
    padding: 10px 20px;
    border-radius: 7px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.remove-location-button:hover {
    background-color: #a7d0f1;
}

.close-icon-wrapper {
    border-radius: 5px;
    padding: 3px;
    background-color: #252528;
}

.close-icon:hover {
    cursor: pointer;
    opacity: 0.8;
}
</style>
