import { $CommonJs } from "../../common/common.js";
export default {
    data() {
        return{
            loading: false,
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
