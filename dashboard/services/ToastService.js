import { ref } from 'vue';

const toastVisible = ref(false);
const toastTitle = ref('');
const toastType = ref('');

const showToast = (title, type) => {
    toastTitle.value = title;
    toastType.value = type;
    toastVisible.value = true;

    setTimeout(() => {
        toastVisible.value = false;
    }, 5000);
};

export { toastVisible, toastTitle, toastType, showToast };
