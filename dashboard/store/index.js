import { defineStore } from 'pinia';
import axios from 'axios';

export const useStore = defineStore({
    id: 'counterStore',
    state: () => ({
        count: 0,
        countries: [],
        locations: [],
        loadingCountries: false,
        loadingLocations: false,
    }),
    getters: {},
    actions: {
        async fetchCountries() {
            this.loadingCountries = true;
            await axios
                .get('/countries')
                .then((res) => {
                    this.countries = res.data;
                })
                .catch((err) => {
                    console.log('err: ', err);
                })
                .finally(() => (this.loadingCountries = false));
        },
        async fetchLocations() {
            this.loadingLocations = true;
            await axios
                .get('/locations')
                .then((res) => {
                    this.locations = res.data;
                })
                .catch((err) => {
                    console.log('err: ', err);
                })
                .finally(() => (this.loadingLocations = false));
        },
        async addLocation(query) {
            await axios
                .post('/locations', query)
                .then(() => {
                    this.fetchLocations();
                })
                .catch((err) => {
                    console.log('err: ', err);
                    throw err?.response?.data?.detail;
                });
        },
        async removeLocation(country) {
            await axios
                .delete(`locations/${country}`)
                .then(() => {
                    this.fetchLocations();
                })
                .catch((err) => {
                    console.log('err: ', err);
                    throw err?.response?.data?.detail || 'Could not delete location';
                });
        },
    },
});
