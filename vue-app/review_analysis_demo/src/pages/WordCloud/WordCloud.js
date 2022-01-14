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
            const response = await this.$apiClient.post("/api/analysis/get_rakuten_analysis_word_cloud");
            this.words = response.data.datas;
        }
    }
};
