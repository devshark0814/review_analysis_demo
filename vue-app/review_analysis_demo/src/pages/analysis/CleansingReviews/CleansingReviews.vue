<template>
    <div>
        <v-data-table
            :headers="headers"
            :items="datas"
            :items-per-page="100"
            class="elevation-1"
            :footer-props="{ 'items-per-page-options': [50, 100, 200, -1] }"
            @click:row="clickRow"
        ></v-data-table>
        <v-dialog
            v-model="dialog"
            width="1000"
            persistent
            eager
        >
            <v-card>
                <v-card-title class="text-h5 grey lighten-2">
                シンプル解析
                </v-card-title>

                <v-card-text>
                    <com-mecab ref="mecab" />
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        color="primary"
                        text
                        @click="clickDialogCloseBtn"
                    >
                        close
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
<script src="./CleansingReviews.js"></script>