<template>
    <v-app>
        <v-navigation-drawer app>
            <menucomponent />
        </v-navigation-drawer>

        <v-main>
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