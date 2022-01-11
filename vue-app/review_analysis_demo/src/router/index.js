import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/pages/Home/Home.vue'
import Analysis from '@/pages/Analysis/Analysis.vue'
import WordCloud from '@/pages/WordCloud/WordCloud.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/analysis',
      name: 'Analysis',
      component: Analysis
    },
    {
      path: '/wordCloud',
      name: 'WordCloud',
      component: WordCloud
    }
  ]
})
