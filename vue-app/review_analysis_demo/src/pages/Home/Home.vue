<template>
    <div>
        <v-container>
            <v-row>
                <v-col>
                    <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                    >
                        <v-row>
                            <v-col cols="2">
                            <v-text-field
                                v-model="shohin_id"
                                label="楽天の商品ID"
                                :rules="[v => !!v || '必須']"
                                required
                            >
                            </v-text-field>
                            </v-col>
                            <v-col cols="1">
                            <v-text-field
                                v-model="repeat"
                                label="繰り返し回数"
                                :rules="[v => !!v || '必須']"
                                required
                                type="number"
                            >
                            </v-text-field>
                            </v-col>
                            <v-col cols="1">
                            <v-btn color="primary" @click="doClick" :disabled="!valid" :loading="loading">スクレイピング実行</v-btn>
                            </v-col>
                            <v-spacer />
                        </v-row>
                    </v-form>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-data-table
                        :headers="headers"
                        :items="datas"
                        :items-per-page="50"
                        class="elevation-1"
                        :footer-props="{ 'items-per-page-options': [50, 100, 200, -1] }"
                    ></v-data-table>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>
<script src="./Home.js"></script>
<style src="./Home.css"></style>