<template>
    <div class="modal-wrapper p-3 rounded-xl">
        <div @click="$emit('onToggle')" class="flex absolute inset-0 z-0" />
        <div class="w-full max-w-lg p-3 relative mx-auto my-auto rounded-xl">
            <div>
                <div class="flex justify-between items-center modal-header">
                    <div>
                        <h1 class="font-semibold text-2xl">Remove Location</h1>
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
                <div class="my-10 min-w-80 input-wrapper">
                    <h1>Are you sure you want to remove this location?</h1>
                </div>
                <div class="flex justify-center text-center mb-2 space-x-4 md:block">
                    <button @click="$emit('onToggle')" class="text-sm font-bold remove-location-button rounded-lg">
                        Cancel
                    </button>
                    <button
                        @click="$emit('onAccept')"
                        class="bg-red-900 text-sm font-bold remove-location-button rounded-lg"
                    >
                        Remove Location
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup></script>

<style scoped>
.modal-wrapper {
    background-color: #1b1b1d;
}
.remove-location-button {
    padding: 10px 20px;
    cursor: pointer;
}

.remove-location-button:hover {
    opacity: 0.8;
    transition: opacity 0.3s ease;
}

.close-icon-wrapper {
    background-color: #252528;
}

.close-icon:hover {
    cursor: pointer;
    opacity: 0.8;
}
</style>
