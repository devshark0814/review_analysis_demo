<template>
    <v-app>
        <v-navigation-drawer app>
            <menucomponent />
        </v-navigation-drawer>

        <v-main style="background-color: #f5f5f5;">
            <router-view />
        </v-main>
    </v-app>
</template>
<script>
import menucomponent from './Menu.vue';
export default {
    components: {
        menucomponent
    }
}
</script>