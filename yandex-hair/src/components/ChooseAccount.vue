<template>
  <div>
    <router-link
        to="/login"
        custom
        v-slot="{ navigate }"
    >
    <button @click="navigate"
            role="link">
      Login
    </button>
    </router-link>
  </div>
  <div>
    <router-link
        to="/register"
        custom
        v-slot="{ navigate }"
    >
      <button @click="navigate"
              role="link">
        Register
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
