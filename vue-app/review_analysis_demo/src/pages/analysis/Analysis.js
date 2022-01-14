import { $CommonJs } from "../../common/common.js";
export default {
    data() {
        return{
            loading: false,
            chartOptions: {
                chart: {
                    type: 'bar',
                    id: 'vuechart-example',
                    height: '500px'
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
                    categories: [],
                    labels: {
                        style: {
                            colors: [],
                            fontSize: '16px',
                        },
                    }
                },
                yaxis: {
                    labels: {
                        style: {
                            colors: [],
                            fontSize: '16px',
                        },
                    }
                },
                colors: ["#00FF00"]
            },
            seriesMeishi: [{
                name: 'series-1',
                data: []
            }],
            seriesDoushi: [{
                name: 'series-1',
                data: []
            }],
            seriesKeiyoushi: [{
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
            let meishi_yData = response.data.datas.meishi_y_arr;
            let meishi_xData = response.data.datas.meishi_x_arr;

            let doushi_yData = response.data.datas.doushi_y_arr;
            let doushi_xData = response.data.datas.doushi_x_arr;

            let keiyoushi_yData = response.data.datas.keiyoushi_y_arr;
            let keiyoushi_xData = response.data.datas.keiyoushi_x_arr;

            this.$refs.chart_meishi.updateSeries([
                {
                    name: '出現回数',
                    data: meishi_xData,
                },
            ]);
            this.$refs.chart_doushi.updateSeries([
                {
                    name: '出現回数',
                    data: doushi_xData,
                },
            ]);
            this.$refs.chart_keiyoushi.updateSeries([
                {
                    name: '出現回数',
                    data: keiyoushi_xData,
                },
            ]);

            this.$refs.chart_meishi.updateOptions({
                title: {
                    text: '名詞の出現回数',
                    align: 'center',
                    floating: true
                },
                xaxis: {
                    categories: meishi_yData,
                },
                colors: ["#007bff"]
            });
            this.$refs.chart_doushi.updateOptions({
                title: {
                    text: '動詞の出現回数',
                    align: 'center',
                    floating: true
                },
                xaxis: {
                    categories: doushi_yData,
                },
                colors: ["#fd7e14"]
            });
            this.$refs.chart_keiyoushi.updateOptions({
                title: {
                    text: '形容詞の出現回数',
                    align: 'center',
                    floating: true
                },
                xaxis: {
                    categories: keiyoushi_yData,
                },
                colors: ["#20c997"]
            });


            this.$toasted.success(response.data.message, $CommonJs.getSuccessToastOptions());
            this.loading = false;
        }
    }
};
