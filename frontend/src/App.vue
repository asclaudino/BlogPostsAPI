<template>
  <div id="nav">
    <NavigationBarComponent>

    </NavigationBarComponent>
  </div>
  <router-view />
</template>

<script>

import NavigationBarComponent from "./components/NavigationBarComponent.vue"

export default {
  name: "App",
  components: {
    NavigationBarComponent,
},
};
</script>


<style>
body {
  font-family: "Noto Sans JP", sans-serif;
  font-weight: 300;
}
</style>
