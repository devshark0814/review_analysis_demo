<template>
    <v-app>
        <v-navigation-drawer app>
            <menucomponent />
        </v-navigation-drawer>

        <v-app-bar app>
        </v-app-bar>

        <v-main>
            <router-view />
        </v-main>

        <v-footer app>
        </v-footer>
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