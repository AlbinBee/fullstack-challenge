// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head: {
            title: 'DataCose: Code Challenge',
        },
    },
    vite: {
        define: {
            'process.env.NUXT_ENV_API_URL': JSON.stringify(process.env.NUXT_ENV_API_URL),
            'process.env.NUXT_ENV_JSONPLACEHOLDER': JSON.stringify(process.env.NUXT_ENV_JSONPLACEHOLDER),
        },
    },
    ssr: false,
    devtools: { enabled: true },
    pages: true,
    modules: ['@nuxt/ui', '@pinia/nuxt'],
    plugins: ['@/plugins/axios.js'],
    pinia: {
        storesDirs: ['./stores/**'],
    },
    // axios: {
    //     baseURL: process.env.API_URL,
    // },
});
