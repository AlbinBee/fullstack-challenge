import { defineStore } from 'pinia';
import axios from 'axios';

export const useStore = defineStore({
    id: 'counterStore',
    state: () => ({
        count: 0,
        countries: [],
        locations: [],
        loading: false,
    }),
    getters: {},
    actions: {
        async fetchCountries() {
            this.loading = true;
            await axios
                .get('/countries')
                .then((res) => {
                    this.countries = res.data;
                })
                .catch((err) => {
                    console.log('err: ', err);
                })
                .finally(() => (this.loading = false));
        },

        async fetchLocations() {
            await axios
                .get('/locations')
                .then((res) => {
                    this.locations = res.data;
                })
                .catch((err) => {
                    console.log('err: ', err);
                });
        },
        async addLocation(query) {
            await axios
                .post('/locations', query)
                .then(() => {
                    this.fetchLocations();
                })
                .catch((err) => {
                    console.log('err: ', err);
                });
        },
        async removeLocation(country) {
            await axios
                .delete(`locations/${country}`)
                .then((res) => {
                    this.fetchLocations();
                })
                .catch((err) => {
                    console.log('err: ', err);
                });
        },
    },
});
