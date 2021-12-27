import $axios from "axios";
import Vue from "vue";

const apiClient = $axios.create({
    baseURL: 'http://localhost:3000',
    headers: { 'Content-Type': 'application/json' },
    // timeout: 60000, // milliseconds
});
//共通レスポンス処理
apiClient.interceptors.response.use(
    function (response) {
        // 成功時の処理
        return response;
    },
    function (error) {
        // 失敗時の処理
        switch (error.response.status) {
            case 401:
            // HTTPステータスに応じて処理
            case 403:
            default:
            // 例外処理
            Vue.toasted.error(error,{
                theme: "bubble",
                position: "top-center",
                duration : 5000
            });
        }
    }
);

export default apiClient;