<template>
    <v-container class="pa-0">
        <v-row dence>
            <v-col cols="1">
                <v-btn color="primary" @click="doAnalysis">分析実行</v-btn>
            </v-col>
        </v-row>
        <v-row dence>
            <v-col>
                <vue-word-cloud
                    style="
                        height: 1000px;
                        width: 1500px;
                    "
                    :words="words"
                    :color="([, weight]) => weight > 10 ? 'DeepPink' : weight > 5 ? 'RoyalBlue' : 'Indigo'"
                    font-family="Roboto"
                />
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./WordCloud.js"></script>