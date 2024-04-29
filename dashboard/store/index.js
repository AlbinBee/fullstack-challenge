import { defineStore } from 'pinia';

export const useCounterStore = defineStore({
    id: 'counterStore',
    state: () => ({
        // State properties goes here
        count: 0,
    }),
    getters: {
        // Getters goes here
    },
    actions: {
        // Actions goes here
        increment() {
            console.log('INCREASING, COUNT BEFORE: ', this.count);
            this.count.s++;
            console.log('COUNT AFTER: ', this.count);
        },
        decrement() {
            console.log('DECREASING, COUNT BEFORE: ', this.count);
            this.count.s--;
            console.log('COUNT AFTER: ', this.count);
        },
    },
});
