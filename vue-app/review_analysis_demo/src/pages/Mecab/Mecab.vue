<template>
    <v-container>
        <v-row>
            <v-col>
                <screen-about-component
                    screen_title="画面概要"
                    screen_description="
                        一文のみの形態素解析を行うことができます。
                    "
                />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="11">
                <v-text-field
                    v-model="searchText"
                    label="解析したい一文"
                    solo
                ></v-text-field>
            </v-col>
            <v-col cols="1">
                <v-btn color="primary" @click="clickAnalysis">解析</v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-data-table
                    :headers="headers"
                    :items="datas"
                    :items-per-page="100"
                    class="elevation-1"
                    :footer-props="{ 'items-per-page-options': [50, 100, 200, -1] }"
                ></v-data-table>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./Mecab.js"></script>