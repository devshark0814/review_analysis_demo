import { $CommonJs } from "../../common/common.js";
export default {
    data() {
        return{
            loading: false,
            valid: false,
            shohin_id: "212142_10126692",           // 対象の商品ID
            repeat: 1,                              // 繰り返し回数

            headers:[
                {text: "日付", align: "right", value: "date" ,width:"10%"},
                {text: "年齢", align: "center", value: "age" ,width:"5%"},
                {text: "性別", align: "center", value: "sex" ,width:"5%"},
                {text: "評価", align: "center", value: "score" ,width:"5%"},
                {text: "レビュー", align: "left", value: "text" ,width:"75%"},
            ],
            datas:[],

            chartOptions: {
                chart: {
                    type: 'bar',
                    id: 'vuechart-example',
                    height: 1000
                },
                plotOptions: {
                    bar: {
                        borderRadius: 4,
                        horizontal: true,
                        barHeight: '80%',
                    }
                },
                dataLabels: {
                    enabled: true
                },
                xaxis: {
                    categories: []
                }
            },
            series: [{
                name: 'series-1',
                data: []
            }]
        }
    },

    methods: {
        doClick: async function(){
            this.loading = true;
            let param = {
                shohin_id: this.shohin_id,
                repeat: this.repeat
            }
            const response = await this.$apiClient.post("/api/scraping/getReviews", param);
            console.log(response);
            this.datas = response.data.datas;
            this.$toasted.success(response.data.message, $CommonJs.getSuccessToastOptions());
            this.loading = false;
        },
        doAnalysis: async function() {
            this.loading = true;
            const response = await this.$apiClient.post("/api/analysis/get_rakuten_analysis");
            console.log(response);
            let yData = response.data.datas.key_arr;
            let xData = response.data.datas.val_arr;

            this.$refs.chart.updateSeries([
                {
                    name: 'sales',
                    data: xData,
                },
            ]);

            this.$refs.chart.updateOptions({
                    xaxis: {
                        categories: yData
                    }
            });


            this.$toasted.success(response.data.message, $CommonJs.getSuccessToastOptions());
            this.loading = false;
        }
    }
};
