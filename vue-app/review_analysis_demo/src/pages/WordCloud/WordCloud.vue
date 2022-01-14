<template>
    <div style="height:100%">
        <!-- <v-btn color="primary" @click="doAnalysis">分析実行</v-btn> -->
        <v-container
            fill-height
            overflow-hidden
            id="container_word_cloud"
        >
            <div class="parent_box">
                <div class="child_box">
                    <vue-word-cloud
                        :words="words"
                        :color="([, weight]) => weight > 10 ? 'DeepPink' : weight > 5 ? 'RoyalBlue' : 'Indigo'"
                        font-family="游ゴシック"
                        :animation-duration="5000"
                        animation-easing="ease"
                        :animation-overlap="5"
                        :font-size-ratio="1/3"
                        :spacing="0.4"
                    />
                </div>
            </div>
        </v-container>
    </div>
</template>
<script src="./WordCloud.js"></script>
<style>
#container_word_cloud .parent_box {
    height: 100%;
    position: relative;
    width: 100%;
}
#container_word_cloud .parent_box .child_box {
    bottom: 0;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
    transition-duration: 1s;
}
</style>