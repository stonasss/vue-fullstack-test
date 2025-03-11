<script setup>
    import { ref } from 'vue';
    import { useAuth } from '@/composables/useAuth';

    const { token, registerUser, loginUser } = useAuth();

    const isRegister = ref(false);
    const newUser = ref({
        username: '',
        password: ''
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        if (isRegister.value) {
            console.log('Adding user:', newUser.value);
            registerUser(newUser.value).then(() => {
                newUser.value = { username: '', password: '' };
            })
        } else {
            console.log('Logging in as:', newUser.value);
            loginUser(newUser.value).then(() => {
                newUser.value = { username: '', password: '' };
            })
        };
    };

    const toggleForm = () => {
        isRegister.value = !isRegister.value;
    }
</script>

<template>
    <div>
        <div class="container">
            <h3>Welcome!</h3>
            <form @submit="handleSubmit">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" v-model="newUser.username"/>
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="text" v-model="newUser.password"/>
                </div>
                <span>
                    <button type="submit" class="btn btn-success" @click="toggleForm">Login</button>
                    <button type="submit" class="btn btn-primary" @click="toggleForm">Register</button>
                </span>
            </form>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    margin: auto;
    align-items: center;
    background: white;
    border-radius: 5px;
    z-index: 1001;

    label {
        padding: 5px;
    }

    input {
        margin: 0 0 10px 0;
    }

    button {
        margin-right: 20px;
    }
}

.form-group {
    width: 100px;
}

.close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 1.2em;
    cursor: pointer;
}
</style>