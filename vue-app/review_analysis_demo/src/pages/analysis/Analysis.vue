<template>
    <v-container>
        <v-row>
            <v-col cols="1">
                <v-btn color="primary" @click="doAnalysis" :loading="loading">分析実行</v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <apexchart ref="chart" type="bar" :options="chartOptions" :series="series"></apexchart>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./Analysis.js"></script>