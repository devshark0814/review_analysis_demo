<template>
    <v-container class="pa-0">
        <v-row dence>
            <v-col cols="1" class="mt-3">
                <v-btn color="primary" @click="doAnalysis" :loading="loading">分析実行</v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
                <div>
                    <span>名詞のグラフ</span>
                    <apexchart ref="chart_meishi" type="bar" height="600px" width="800px" :options="chartOptions" :series="seriesMeishi"></apexchart>
                </div>
            </v-col>
            <v-col cols="6">
                <span>動詞のグラフ</span>
                <apexchart ref="chart_doushi" type="bar" height="600px" width="800px" :options="chartOptions" :series="seriesDoushi"></apexchart>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
                <span>形容詞のグラフ</span>
                <apexchart ref="chart_keiyoushi" type="bar" height="600px" width="800px" :options="chartOptions" :series="seriesKeiyoushi"></apexchart>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./Analysis.js"></script>