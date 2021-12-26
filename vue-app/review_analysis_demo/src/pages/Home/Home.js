import { $CommonJs } from "../../common/common.js";
export default {
    data() {
        return{
        }
    },

    methods: {
        doClick: async function(){
            const response = await this.$apiClient.post("/api/scraping/");
            this.$toasted.success(response.data.message, $CommonJs.getSuccessToastOptions());
        }
    }
};
