import mecab from '@/pages/Mecab/Mecab.vue';
export default {
    components : {
        "com-mecab" : mecab
    },

    data() {
        return{
            headers:[
                {text: "日付", value: "date",          align: "left",  width:"5%"},
                {text: "性別", value: "sex",           align: "left",  width:"2%"},
                {text: "年代", value: "age",           align: "right", width:"2%"},
                {text: "評価", value: "score",         align: "right", width:"1%"},
                {text: "原文", value: "text",          align: "left",  width:"45%"},
                {text: "校正", value: "remake_text",   align: "left",  width:"45%"},
            ],
            datas:[],

            dialog: false,
        }
    },

    created() {
        // this.init();
    },

    methods: {
        search: async function() {
            const response = await this.$apiClient.get("/api/analysis/rakuten/get_cleansing_reviews");
            this.datas = response.data;
        },

        clickRow(rowItem) {
            this.dialog = true;
            this.$refs.mecab.simpleAnalysis(rowItem);
        },

        clickDialogCloseBtn() {
            this.dialog = false;
            this.$refs.mecab.dialogClose();
        }
    }
};
