<template>
    <vue-word-cloud
        style="
            height: 480px;
            width: 640px;
        "
        :words="[['romance', 19], ['horror', 3], ['fantasy', 7], ['adventure', 3]]"
        :color="([, weight]) => weight > 10 ? 'DeepPink' : weight > 5 ? 'RoyalBlue' : 'Indigo'"
        font-family="Roboto"
    />
</template>
<script src="https://unpkg.com/vue"></script>
<script src="https://unpkg.com/vuewordcloud"></script>
<script src="./WordCloud.js"></script>