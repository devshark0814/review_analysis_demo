<template>
    <v-card class="mx-auto navimenu" width="300" height="100%">
        <v-list>
            <v-list-item @click="clickHome">
                <v-list-item-icon>
                    <v-icon>mdi-view-week</v-icon>
                </v-list-item-icon>

                <v-list-item-title>スクレイピング</v-list-item-title>
            </v-list-item>
            <v-list-item @click="clickAnalysis">
                <v-list-item-icon>
                    <v-icon>mdi-view-week</v-icon>
                </v-list-item-icon>

                <v-list-item-title>分析</v-list-item-title>
            </v-list-item>
            <v-list-item @click="clickWordCloud">
                <v-list-item-icon>
                    <v-icon>mdi-view-week</v-icon>
                </v-list-item-icon>

                <v-list-item-title>ワードクラウド</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-card>
</template>
<script>
export default {
    data() {
        return{
        }
    },

    methods: {
        clickHome() {
            this.$router.push("/home");
        },
        clickAnalysis() {
            this.$router.push("/analysis");
        },
        clickWordCloud() {
            this.$router.push("/wordCloud");
        }
    }
}
</script>
<style>
.navimenu *{
    font-size: 14px;
}
</style>