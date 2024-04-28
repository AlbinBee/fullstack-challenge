<template>
    <div>
        <sidebar />
    </div>
</template>

<script setup>
const isOpen = ref(false);

const onToggle = () => {
    isOpen.value = !isOpen.value;
};
</script>

<style scoped></style>
