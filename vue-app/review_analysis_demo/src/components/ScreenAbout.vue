<template>
    <div class="screen-about-box">
        <div class="screen-about-box-title">{{screen_title}}</div>
        <p v-html="screen_description"></p>
    </div>
</template>
<script>
export default {

    props: ['screen_title', 'screen_description'],

    data() {
        return{
        }
    },
}
</script>
<style>
.screen-about-box{
    margin: 1em 0;
    background-color: #fffbf4;
    border: 2px solid #ee7917;
}

.screen-about-box-title{
    font-size: 16px;
    position: absolute;
    margin-top: 0;
    background-color: #ee7917;
    color: #fff;
    font-weight: bold;
    border-radius: 0 0 2px 0;
    padding: 4px 6px;
}

.screen-about-box p{
    margin: 0;
    padding: 3em 1em 1em 1em;
    text-align: left;
}
</style>