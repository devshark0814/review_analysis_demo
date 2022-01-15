export default {
    data() {
        return{
            words:[[]],
        }
    },

    mounted: function() {
        this.doAnalysis();
    },

    methods: {
        doAnalysis: async function() {
            const response = await this.$apiClient.get("/api/analysis/rakuten/get_word_cloud");
            this.words = response.data.datas;
        }
    }
};
