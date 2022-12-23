import { createStore } from 'vuex'


export const store = createStore({
    state() {
        return {
            user: undefined
        }
    },

    actions:{
        register({commit}, data) {
            fetch('http://localhost:8080/signup/', {
                // headers: {
                //     // 'X-Access-Token': 'f7947a928f5d3e8f518f10d1e30d056e859f8d2b87eecfae04b3cab112a92cd9',
                //     'Content-Type': 'application/json',
                // },
                method: 'POST',
                body: JSON.stringify({data})
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not OK');
                    }
                    return response.json()
                })
                .then(info => {
                    commit('registerUser', info)
                    console.log('Success:', info);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        }
    },

    mutations: {
        registerUser(state, data) {
            state.user = data
        }
    }
})
