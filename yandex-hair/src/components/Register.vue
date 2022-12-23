<template>
  <div class="bg-[url('https://images4.alphacoders.com/104/1041628.jpg')]">
    <div class="py-48 overflow-hidden"
    >
      <div class="container mx-auto px-4 h-full">
        <div class="flex content-center items-center justify-center h-full">
          <div class="w-full lg:w-4/12 px-4">
            <div
                class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg from-transparent border-0"
            >
              <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
                <div class="text-2xl text-indigo-900 text-center mb-3 font-bold">
                  <small>Player Registration</small>
                </div>
                <form>
                  <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-indigo-900 text-sm font-bold mb-2"
                        for="grid-password"
                    >Name</label
                    ><input
                      type="name"
                      v-model="form.name"
                      class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                      placeholder="Name"
                      style="transition: all 0.15s ease 0s;"
                  />
                  </div>
                  <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-indigo-900 text-sm font-bold mb-2"
                        for="grid-password"
                    >Surname</label
                    ><input
                      type="surname"
                      v-model="form.surname"
                      class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                      placeholder="Surname"
                      style="transition: all 0.15s ease 0s;"
                  />
                  </div>
                  <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-indigo-900 text-sm font-bold mb-2"
                        for="grid-password"
                    >Email</label
                    ><input
                      type="email"
                      v-model="form.email"
                      class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                      placeholder="Email"
                      style="transition: all 0.15s ease 0s;"
                  />
                  </div>
                  <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-indigo-900 text-sm font-bold mb-2"
                        for="grid-password"
                    >Phone</label
                    ><input
                      type="phone"
                      v-model="form.phone"
                      class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                      placeholder="Phone"
                      style="transition: all 0.15s ease 0s;"
                  />
                  </div>
                  <div>
                    <input type="radio" id="male" name="gender" value="Male">
                    <label for="html">Male</label><br>
                    <input type="radio" id="female" name="gender" value="Female">
                    <label for="css">Female</label><br>
                    <input type="radio" id="child" name="gender" value="Child">
                    <label for="javascript">Child</label>
                  </div>
                  <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-indigo-900 text-sm font-bold mb-2"
                        for="grid-password"
                    >Surname</label
                    ><input
                      type="surname"
                      v-model="form.surname"
                      class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                      placeholder="Surname"
                      style="transition: all 0.15s ease 0s;"
                  />
                  </div>
                  <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-indigo-900 text-sm font-bold mb-2"
                        for="grid-password"
                    >Password</label
                    ><input
                      type="password"
                      v-model="form.password"
                      class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                      placeholder="Password"
                      style="transition: all 0.15s ease 0s;"
                  />
                  </div>
                  <div class="text-center mt-6">
                    <button
                        class="bg-indigo-900 text-white active:bg-gray-700 text-s font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full"
                        type="button"
                        @click="register"
                        style="transition: all 0.15s ease 0s;"
                    >
                      Register
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      form: {
        name: "",
        surname: "",
        email: "",
        phone: "",
        password: "",
        gender: ""
      }
    }
  },
  mounted() {
    console.log(this.$store.state.user)
  },
  methods: {
    register() {
      this.$store.dispatch('register', this.form).then(() => {
        this.$router.push({name:'HomePage'})
      })
    }
  }
}
</script>

<style scoped>

</style>
