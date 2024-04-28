<template>
    <div id="app">
        <div v-if="isModalVisible">
            <div @click="$emit('onToggle')" class="flex absolute bg-black inset-0 z-0" />
            <div class="w-full max-w-lg p-3 relative mx-auto my-auto rounded-xl shadow-lg">
                <div>
                    <div class="flex flex-row-reverse">
                        <svg
                            @click="$emit('onToggle')"
                            class="w-6 h-6 close-icon"
                            fill="none"
                            stroke="currentColor"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M6 18L18 6M6 6l12 12"
                            ></path>
                        </svg>
                    </div>
                    <div class="text-center p-3 flex-auto justify-center leading-6">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="w-16 h-16 flex items-center text-purple-500 mx-auto"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                                clip-rule="evenodd"
                            />
                        </svg>
                        <h2 class="text-2xl font-bold py-4">Are you sure?</h2>
                        <p class="text-md text-gray-500 px-8">Do you really want to delete this location?</p>
                    </div>
                    <div class="p-3 mt-2 text-center space-x-4 md:block">
                        <button @click="$emit('onToggle')" class="w-full mb-2 text-sm font-bold remove-location-button">
                            Add Location
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, defineProps } from 'vue';

const props = defineProps({
    isModalOpen: Boolean,
});

const isModalVisible = computed(() => {
    return props.isModalOpen;
});
</script>

<style scoped>
.remove-location-button {
    background-color: #d4e8f8;
    color: #111015;
    border: none;
    padding: 7px 20px;
    border-radius: 7px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.remove-location-button:hover {
    background-color: #a7d0f1;
}

.close-icon {
}

.close-icon:hover {
    cursor: pointer;
    opacity: 0.8;
}
</style>
