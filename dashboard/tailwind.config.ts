import type { Config } from 'tailwindcss';

export default <Partial<Config>>{
    theme: {},
    plugins: [require('flowbite/plugin')],
    content: ['./node_modules/flowbite/**/*.js'],
};
