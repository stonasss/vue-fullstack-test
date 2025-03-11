import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export function useAuth() {
    const token = ref(null);
    const router = useRouter();

    const registerUser = async (newUser) => {
        try {
            const path = 'http://localhost:5000/register';
            await axios.post(path, newUser);
            console.log('User registered successfully');
        } catch (err) {
            console.error(err)
        }
    };

    const loginUser = async (logIn) => {
        try {
            const path = 'http://localhost:5000/login';
            const res = await axios.post(path, logIn);
            token.value = res.data.token
            console.log(res.data)
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