<template>
    <div class="w-screen h-screen flex items-center justify-center">
        <!-- Add a Loader here -->
        <loader v-if="loading" />
        <!-- Start Of Table -->
        <div class="p-5 w-full h-full bg-background weather-app" v-else>
            <div class="m-auto container">
                <header class="mb-20 flex items-center">
                    <img :src="images[3]" alt="main-logo" />
                    <h1 class="pl-2 text-xl">Weather App</h1>
                </header>
                <div class="flex justify-between items-center mb-5">
                    <h1 class="text-3xl">Locations</h1>
                    <button @click="isModalOpen = true" class="text-sm font-bold text-background add-location-button">
                        + Add Location
                    </button>
                </div>
                <div class="pt-5" v-if="locations.length == 0 && !loading">
                    <h1 class="flex justify-center align-center items-center text-2xl text-zinc-400">
                        No Locations were found!
                    </h1>
                    <h5
                        class="flex justify-center align-center items-center text-blue-300 cursor-pointer"
                        @click="isModalOpen = true"
                    >
                        Click here to add one...
                    </h5>
                </div>
                <table class="w-full location-table" v-else>
                    <thead class="rounded-2xl">
                        <tr class="location-table-header">
                            <th class="rounded-tl">Location</th>
                            <th>Temperature</th>
                            <th>Rainfall</th>
                            <th class="rounded-tr"></th>
                        </tr>
                    </thead>
                    <tbody class="location-table-body">
                        <tr class="table-row" v-for="location in locations" :key="location.id">
                            <td @click="toggleSlideover(location)" class="flex align-center items-center weather-link">
                                <div>
                                    <img
                                        :src="getImageIdFromWmoCode(location.current.weather_code)"
                                        alt="weather-condition"
                                    />
                                </div>
                                <div class="ml-4 location-name">
                                    {{ location.name }}
                                </div>
                            </td>
                            <td class="text-zinc-300 text-sm">{{ location.current.temperature_2m }}°C</td>
                            <td class="text-zinc-300 text-sm">{{ location.current.rain }} mm</td>
                            <td class="flex flex-row-reverse">
                                <img
                                    :src="images['delete']"
                                    alt="delete"
                                    class="w-5 delete-icon"
                                    @click="toggleRemoveModal(location)"
                                />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <!-- End Of Table -->
        <!-- Start of Sidebar -->
        <transition name="fade" class="z-50">
            <div
                :class="{ invisible: !isSlideoverVisible }"
                id="slideover-container"
                class="w-full h-full fixed inset-0"
            >
                <div
                    @click="toggleSlideover"
                    :class="{ 'opacity-0': !isSlideoverVisible, 'opacity-70': isSlideoverVisible }"
                    id="slideover-bg"
                    class="w-full h-full duration-300 ease-out transition-all inset-0 absolute bg-black"
                />
                <div
                    id="slideover"
                    :class="{ 'translate-x-full': !isSlideoverVisible }"
                    class="w-96 h-full absolute right-0 duration-300 ease-out transition-all sidebar-content"
                >
                    <div class="mt-2 p-5">
                        <div @click="toggleSlideover" class="absolute cursor-pointer right-0 mr-5">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M6 18L18 6M6 6l12 12"
                                />
                            </svg>
                        </div>
                        <div>
                            <h1 class="text-xl">{{ currentLocation?.capital }}, {{ currentLocation?.name }}</h1>
                            <p class="mt-5 text-zinc-400 text-sm">This Week</p>
                            <div
                                class="mt-2 weather-card-wrapper"
                                v-for="(item, index) in currentLocation?.daily?.time"
                                :key="index"
                            >
                                <weather-card
                                    :weatherIconUrl="getImageIdFromWmoCode(currentLocation?.daily.weather_code[index])"
                                    :weatherDay="getDayName(item)"
                                    :weatherMin="currentLocation?.daily.temperature_2m_min[index]"
                                    :weatherMax="currentLocation?.daily.temperature_2m_max[index]"
                                    :rain="currentLocation?.daily.rain_sum[index]"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
        <!-- End of Sidebar -->
        <!-- Start of Backdrop -->
        <transition name="fade">
            <div
                v-if="isModalOpen || isDeleteModalOpen || currentLocation != null"
                class="bg-black opacity-70 h-screen w-screen top-0 overflow-y-auto fixed"
                @click="closeModals()"
            />
        </transition>
        <!-- End of Backdrop -->
        <!-- Start of Modals -->
        <transition name="fade">
            <modal v-if="isModalOpen" class="z-50 modal" @onToggle="toggleModal" :isModalOpen="isModalOpen" />
        </transition>
        <transition name="fade">
            <delete-modal
                v-if="isDeleteModalOpen"
                class="z-50 modal"
                @onToggle="toggleRemoveModal"
                @onAccept="removeLocation"
            />
        </transition>
        <!-- End of Modals -->
        <!-- Start of Toaster -->
        <transition name="slide">
            <toast :title="toastTitle" :type="toastType" :visible="toastVisible" @onClose="closeToast" />
        </transition>
        <!-- End of Toaster -->
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { filename } from 'pathe/utils';
import { useStore } from '@/store';
import Modal from '@/components/Modal.vue';
import Loader from '@/components/Loader.vue';
import DeleteModal from '@/components/DeleteModal.vue';
import { toastVisible, toastTitle, toastType, showToast } from '@/services/ToastService.js';

const mainStore = useStore();
const loading = computed(() => mainStore.loadingCountries || mainStore.loadingLocations);
const locations = computed(() => mainStore.locations);

const isSlideoverVisible = ref(false);
const currentLocation = ref(null);
const isModalOpen = ref(false);
const isDeleteModalOpen = ref(false);

mainStore.fetchCountries();
mainStore.fetchLocations();

const glob = import.meta.glob('../assets/icons/*.svg', { eager: true });
const images = Object.fromEntries(Object.entries(glob).map(([key, value]) => [filename(key), value.default]));

const toggleModal = () => {
    isModalOpen.value = !isModalOpen.value;
};

const toggleRemoveModal = (location) => {
    isDeleteModalOpen.value = !isDeleteModalOpen.value;

    if (isDeleteModalOpen.value) {
        currentLocation.value = location;
    } else {
        currentLocation.value = null;
    }
};

const removeLocation = () => {
    mainStore
        .removeLocation(currentLocation.value.name)
        .then(() => {
            showToast('Successfully removed location', 'success');
        })
        .catch((err) => {
            showToast(`Failed removing location: ${err}`, 'danger');
        });
    closeModals();
};

const closeModals = () => {
    isModalOpen.value = false;
    isDeleteModalOpen.value = false;
    currentLocation.value = null;
};

const getDayName = (dateString) => {
    if (dateString == null) return;

    const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const date = new Date(dateString);
    const dayIndex = date.getDay();

    return daysOfWeek[dayIndex];
};

const closeToast = () => {
    toastVisible.value = false;
};

const toggleSlideover = (location) => {
    isSlideoverVisible.value = !isSlideoverVisible.value;

    if (isSlideoverVisible.value == false) {
        currentLocation.value = null;
    }

    if (location.name != null) {
        currentLocation.value = location;
    } else {
        currentLocation.value = null;
    }
};

//based on https://open-meteo.com/en/docs
const getImageIdFromWmoCode = (wmoCode) => {
    if (wmoCode === 0) return images[1]; // Sunny
    if (wmoCode >= 1 && wmoCode <= 3) return images[3]; // Mainly clear, partly cloudy, overcast
    if (wmoCode === 45 || wmoCode === 48) return images[4]; // Fog and depositing rime fog
    if (wmoCode >= 51 && wmoCode <= 57) return images[5]; // Drizzle and freezing drizzle
    if (wmoCode >= 61 && wmoCode <= 67) return images[5]; // Rain and freezing rain
    // if (wmoCode >= 71 && wmoCode <= 77) return null; // Snow fall and snow grains
    if (wmoCode >= 80 && wmoCode <= 82) return images[5]; // Rain showers
    // if (wmoCode === 85 || wmoCode === 86) return null; // Snow showers
    if (wmoCode >= 95 && wmoCode <= 99) return images[2]; // Thunderstorm
    return images[4];
};
</script>
<style scoped>
#slideover {
    background-color: #1b1b1d;
}

.weather-app {
    /* background-color: red; */
    font-family: Arial, sans-serif;
}

.add-location-button {
    background-color: #d4e8f8;
    /* color: #111015; */
    padding: 7px 20px;
    border-radius: 7px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.add-location-button:hover {
    background-color: #a7d0f1;
}

.sidebar-content {
    overflow-x: scroll;
}

.location-name {
    color: #d4e8f8;
}

.weather-link:hover {
    cursor: pointer;
}

.location-table th {
    font-weight: 300;
    background-color: #323232;
    color: #ffffff;
}

.location-table th,
.location-table td {
    padding: 10px 30px;
    text-align: left;
    border-bottom: 0.5px solid #353535;
}

.table-row:hover {
    background-color: #252528;
}

.location-table tbody tr {
    background-color: #1b1b1d;
}

.delete-icon:hover {
    cursor: pointer;
    opacity: 0.7;
}

.modal {
    position: fixed;
    top: calc(50% - 200px);
    left: calc(50% - 250px);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
