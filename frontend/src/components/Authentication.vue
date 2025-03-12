<script setup>
    import { ref } from 'vue';
    import { useAuth } from '@/composables/useAuth';

    const { registerUser, loginUser } = useAuth();

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
                    <label for="username"></label>
                    <input type="text" v-model="newUser.username" placeholder="Username"/>
                </div>
                <div class="form-group">
                    <label for="password"></label>
                    <input type="password" v-model="newUser.password" placeholder="Password"/>
                </div>
                <span>
                    <button type="submit" class="btn btn-primary">{{ isRegister ? 'Register' : 'Login' }}</button>
                    <button type="button" class="btn btn-success" @click="toggleForm">Switch to {{ isRegister ? 'Login' : 'Register' }}</button>
                </span>
            </form>
        </div>
    </div>
</template>

<style scoped>
.container {
    position: relative;
    display: flex;
    flex-direction: column;
    margin: auto;
    align-items: center;
    background: white;
    border-radius: 5px;
    z-index: 1001;

    h3 {
        margin-top: 30px;
    }

    input {
        position: absolute;
        left: 43%;
        height: 25px;
        width: 180px;
        margin: 5px;
    }

    span {
        position: absolute;
        top: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: auto;
    }

    button {
        margin-top: 15px;
        width: 200px;
    }
}

.form-group {
    width: 200px;
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