<template>
    <div class="w-screen h-screen flex items-center justify-center">
        <!-- Start Of Route -->
        <div class="weather-app">
            <div class="m-auto container">
                <header class="app-header flex items-center">
                    <img :src="images[3]" alt="main-logo" />
                    <h1 class="pl-2 text-xl">Weather App</h1>
                </header>
                <div class="table-title">
                    <h1 class="text-3xl">Locations</h1>
                    <button @click="isModalOpen = true" class="text-sm font-bold add-location-button">
                        + Add Location
                    </button>
                </div>
                <table class="location-table">
                    <thead class="rounded-2xl">
                        <tr class="location-table-header">
                            <th>Location</th>
                            <th>Temperature</th>
                            <th>Rainfall</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody class="location-table-body">
                        <tr class="table-row" v-for="location in locations" :key="location.id">
                            <td @click="toggleSlideover(location)" class="flex align-center items-center weather-link">
                                <div>
                                    <img :src="getImg(location)" alt="weather-condition" />
                                </div>
                                <div class="ml-4 location-name">
                                    {{ location.name }}
                                </div>
                            </td>
                            <td class="text-zinc-300 text-sm">{{ location.temperature }}°C</td>
                            <td class="text-zinc-300 text-sm">{{ location.rainfall }} mm</td>
                            <td class="flex flex-row-reverse">
                                <img :src="images['delete']" alt="delete" class="delete-icon" />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <!-- End Of Route -->
        <div id="slideover-container" class="w-full h-full fixed inset-0 invisible">
            <div
                @click="toggleSlideover"
                id="slideover-bg"
                class="w-full h-full duration-500 ease-out transition-all inset-0 absolute bg-black opacity-0"
            ></div>
            <div
                id="slideover"
                class="w-96 h-full absolute right-0 duration-300 ease-out transition-all translate-x-full"
            >
                <div class="mt-2 p-5 sidebar-content">
                    <div @click="toggleSlideover" class="absolute cursor-pointer right-0 mr-5">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M6 18L18 6M6 6l12 12"
                            ></path>
                        </svg>
                    </div>
                    <div>
                        <h1 class="text-xl">{{ currentLocation?.name }}, Country</h1>
                        <p class="mt-5 text-zinc-400 text-sm">This Week</p>
                        <div class="mt-2 weather-card-wrapper">
                            <weather-card
                                :weatherIconUrl="images[1]"
                                weatherDay="Sunday"
                                :weatherMin="15"
                                :weatherMax="18"
                            />
                            <weather-card
                                :weatherIconUrl="images[4]"
                                weatherDay="Monday"
                                :weatherMin="15"
                                :weatherMax="18"
                            />
                            <weather-card
                                :weatherIconUrl="images[5]"
                                weatherDay="Tuesday"
                                :weatherMin="15"
                                :weatherMax="18"
                            />
                            <weather-card
                                :weatherIconUrl="images[4]"
                                weatherDay="Wednesday"
                                :weatherMin="15"
                                :weatherMax="18"
                            />
                            <weather-card
                                :weatherIconUrl="images[1]"
                                weatherDay="Thursday"
                                :weatherMin="15"
                                :weatherMax="18"
                            />
                            <weather-card
                                :weatherIconUrl="images[3]"
                                weatherDay="Friday"
                                :weatherMin="15"
                                :weatherMax="18"
                            />
                            <weather-card
                                :weatherIconUrl="images[1]"
                                weatherDay="Saturday"
                                :weatherMin="15"
                                :weatherMax="18"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div
            v-if="isModalOpen"
            class="sidebar-wrapper-bg bg-black opacity-85 h-screen w-screen top-0 overflow-y-auto fixed z-[111]"
            @click="toggleModel()"
        />

        <modal class="bg-white modal" @onToggle="toggleModel" :isModalOpen="isModalOpen" />
    </div>
</template>

<script setup>
import { filename } from 'pathe/utils';
import { ref } from 'vue';
import Modal from './Modal.vue';
import LocationModal from './LocationModal.vue';

const glob = import.meta.glob('../assets/icons/*.svg', { eager: true });
const images = Object.fromEntries(Object.entries(glob).map(([key, value]) => [filename(key), value.default]));

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

const currentLocation = ref(null);
const isModalOpen = ref(false);

const toggleModel = () => {
    console.log('ADASDASDASD');
    isModalOpen.value = !isModalOpen.value;
};

function toggleSlideover(location) {
    document.getElementById('slideover-container').classList.toggle('invisible');
    document.getElementById('slideover-bg').classList.toggle('opacity-0');
    document.getElementById('slideover-bg').classList.toggle('opacity-70');
    document.getElementById('slideover').classList.toggle('translate-x-full');

    if (location.id != null) {
        currentLocation.value = location;
    } else {
        currentLocation.value = null;
    }
}

function getImg(location) {
    if (location.rainfall > 10) return images[2];
    else if (location.rainfall != 0) return images[5];
    else if (location.rainfall <= 0 && location.temperature > 13) return images[1];
    else return images[4];
}
</script>

<style scoped>
/* Sidebar Style */
#slideover {
    background-color: #1b1b1d;
}

.weather-app {
    height: 100vh;
    width: 100%;
    background-color: #111015;
    color: #ffffff;
    font-family: Arial, sans-serif;
    padding: 20px;
}

.app-header {
    margin-bottom: 3rem;
}

.table-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.add-location-button {
    background-color: #d4e8f8;
    color: #111015;
    border: none;
    padding: 7px 20px;
    border-radius: 7px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.add-location-button:hover {
    background-color: #a7d0f1;
}

.location-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
}
/* 
.location-item {
    background-color: #2d3748;
    padding: 20px;
    border-radius: 4px;
} */

.location-name {
    /* font-size: 18px; */
    color: #d4e8f8;
}

.temperature,
.rainfall {
    font-size: 14px;
    margin-top: 5px;
}

.location-table {
    width: 100%;
    border-collapse: collapse;
    border-radius: 50px;
    margin-top: 20px;
}

.weather-link:hover {
    cursor: pointer;
}

.location-table th {
    font-weight: 300;
}

.location-table th,
.location-table td {
    padding: 10px 30px;
    text-align: left;
    border-bottom: 0.5px solid #353535;
}

/* .location-table td {
    background-color: #1b1b1d;
} */

.table-row:hover {
    /* opacity: 0.1; */
    /* cursor: pointer; */
    background-color: #252528;
}

.location-table th {
    background-color: #323232;
    color: #ffffff;
}

.location-table tbody tr {
    background-color: #1b1b1d;
}

.delete-icon {
    width: 20px !important;
}

.delete-icon:hover {
    cursor: pointer;
    opacity: 0.7;
}

.modal {
    position: fixed;
    top: calc(50% - 200px);
    left: calc(50% - 250px);
    z-index: 99999;
}
</style>
