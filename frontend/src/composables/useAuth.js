import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export function useAuth() {
    const token = ref(localStorage.getItem('token') || null);
    const router = useRouter();

    const api = axios.create({
        baseURL: 'http://localhost:5000'
    });

    const registerUser = async (newUser) => {
        try {
            await api.post('/register', newUser);
            console.log('User registered successfully');
        } catch (err) {
            console.error(err)
        }
    };

    const loginUser = async (logIn) => {
        try {
            const res = await api.post('/login', logIn);
            token.value = res.data.token
            console.log(res.data)
            localStorage.setItem('token', token.value);
            console.log('User logged in, welcome back!');
            router.push('/games');
        } catch (err) {
            console.error(err)
        }
    };

    return {
        token,
        registerUser,
        loginUser
    }
}