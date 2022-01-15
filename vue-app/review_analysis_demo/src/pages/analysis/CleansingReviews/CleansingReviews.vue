<template>
    <v-data-table
        :headers="headers"
        :items="datas"
        :items-per-page="50"
        class="elevation-1"
        :footer-props="{ 'items-per-page-options': [50, 100, 200, -1] }"
    ></v-data-table>
</template>
<script src="./CleansingReviews.js"></script>