<template>
    <v-container class="pa-0">
        <v-row dence>
            <v-col cols="1" class="mt-3">
                <v-btn color="primary" @click="doAnalysis" :loading="loading">分析実行</v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <apexchart ref="chart" type="bar" height="850px" :options="chartOptions" :series="series"></apexchart>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./Analysis.js"></script>