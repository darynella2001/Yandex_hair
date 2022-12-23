<template>
  <div>
    <router-link
        to="/client_home"
        custom
        v-slot="{ navigate }"
    >
    <button @click="navigate"
            role="link">
      Client
    </button>
    </router-link>
  </div>
  <div>
    <router-link
        to="/hairdresser_home"
        custom
        v-slot="{ navigate }"
    >
      <button @click="navigate"
              role="link">
        Hairdresser
      </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "ChooseAccount.vue"
}
</script>

<style scoped>

</style>
