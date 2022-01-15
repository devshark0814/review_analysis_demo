export default {
    data() {
        return{
            searchText: '',

            headers:[
                {text: "表層系", value: "表層系", align: "left"},
                {text: "品詞",   value: "品詞",  align: "left"},
                {text: "基本形", value: "基本形",  align: "left"},
            ],
            datas:[]
        }
    },

    methods: {
        clickAnalysis: async function() {
            const response = await this.$apiClient.post("/api/mecab/get_simple_mecab_result", {text: this.searchText});
            this.datas = response.data;
        },

        simpleAnalysis: async function(rowItem) {
            console.log(rowItem);
            this.searchText = rowItem.text;
            await this.clickAnalysis();
        },

        dialogClose() {
            this.searchText = "";
        }
    }
};
