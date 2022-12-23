import { createWebHistory, createRouter } from "vue-router";
import HomePageClient from "../components/HomePageClient.vue";
import HomePageHairdresser from "../components/HomePageHairdresser.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import Home from "../components/Home.vue";
import HelloWorld from "../components/HelloWorld.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
        children: [
            {
                path: "/client_home",
                name: "Client Home",
                component: HomePageClient,
                children: [
                    // {
                    //     path: ":id",
                    //     name: "quiz" ,
                    //     component: QuizElement,
                    // },
                    // {
                    //     path: "",
                    //     name: "all_quizzes" ,
                    //     component: QuizWindow,
                    // },
                ]
            },
            {
                path: "/hairdresser_home",
                name: "HomePageHairdresser",
                component: HomePageHairdresser,
            },
            {
                path: "/login",
                name: "Login",
                component: Login,
            },
            {
                path: "/register",
                name: "Register",
                component: Register,
            },
            // {
            //     path: "/hello",
            //     name: "HelloWorld",
            //     component: HelloWorld,
            // }
        ]
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
