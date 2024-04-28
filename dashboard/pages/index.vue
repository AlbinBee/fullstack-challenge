<!-- <template>
    <div class="w-screen h-screen flex items-center justify-center">
        <h1 class="text-6xl">Good luck! 👋</h1>
    </div>
</template> -->

<template>
    <sidebar />
    <!-- <div class="weather-app">
        <div class="m-auto container">
            <sidebar />
            <header class="app-header flex items-center">
                <img :src="images[3]" alt="main-logo" />
                <h1 class="pl-2 text-xl">Weather App</h1>
            </header>
            <div class="table-title">
                <h1 class="text-3xl">Locations</h1>
                <button class="add-location-button">+ Add Location</button>
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
                        <td class="flex align-center items-center weather-link">
                            <div>
                                <img :src="getImg(location)" alt="weather-condition" />
                            </div>
                            <div class="pl-3 location-name">
                                {{ location.name }}
                            </div>
                        </td>
                        <td class="text-zinc-400 text-sm">{{ location.temperature }}°C</td>
                        <td class="text-zinc-400 text-sm">{{ location.rainfall }} mm</td>
                        <td class="flex flex-row-reverse">
                            <img :src="images['delete']" alt="delete" class="delete-icon" />
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div> -->
</template>

<!-- <script src="../path/to/flowbite/dist/flowbite.min.js"></script> -->
<script setup>
// import { filename } from 'pathe/utils';
// import sidebar from '@/components/Sidebar.vue';

// const glob = import.meta.glob('../assets/icons/*.svg', { eager: true });
// const images = Object.fromEntries(Object.entries(glob).map(([key, value]) => [filename(key), value.default]));

// const locations = [
//     { id: 1, name: 'Beijing', temperature: 13, rainfall: 0 },
//     { id: 2, name: 'Berlin', temperature: 15, rainfall: 20 },
//     { id: 3, name: 'Buenos Aires', temperature: 22, rainfall: 0 },
//     { id: 4, name: 'Cairo', temperature: 24, rainfall: 3 },
//     { id: 5, name: 'Cape Town', temperature: 24, rainfall: 0 },
//     { id: 6, name: 'Istanbul', temperature: 12, rainfall: 0 },
//     { id: 7, name: 'London', temperature: 14, rainfall: 20 },
//     { id: 8, name: 'Madrid', temperature: 16, rainfall: 0 },
// ];

// function getImg(location) {
//     if (location.rainfall > 10) return images[2];
//     else if (location.rainfall != 0) return images[5];
//     else if (location.rainfall <= 0 && location.temperature > 13) return images[1];
//     else return images[4];
// }
</script>

<style scoped>
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

.delete-icon:hover {
    cursor: pointer;
    opacity: 0.7;
}
</style>
