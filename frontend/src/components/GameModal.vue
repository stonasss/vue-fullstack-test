<script setup>
const props = defineProps({
    isModalOpen: Boolean,
    isNewGame: Boolean,
    activeGame: Object,
    playedValue: String,
});

const emit = defineEmits(['close-modal', 'submit', 'update:activeGame', 'update:playedValue']);

const closeModal = () => {
    emit('close-modal');
};

const submitForm = () => {
    emit('submit');
};

const updateActiveGame = (field, value) => {
    const updatedGame = { ...props.activeGame, [field]: value };
    emit('update:activeGame', updatedGame);
};

const updatePlayedValue = (value) => {
    emit('update:playedValue', value);
};
</script>

<template>
    <Teleport to="#modal">
        <div class="modal-bg" v-if="isModalOpen" @click.self="closeModal">
            <div class="modal-container">
                <button @click="closeModal" class="close-btn">x</button>
                <h3 v-if="isNewGame">Add New Game</h3>
                <h3 v-else>Update Game</h3>
                <form @submit.prevent="submitForm">
                    <div class="form-group">
                        <label for="title">Title</label>
                        <input
                            type="text"
                            class="form-control"
                            id="title"
                            :value="activeGame.title"
                            @input="(e) => {
                                updateActiveGame('title', e.target.value);
                            }"
                            required
                        />
                    </div>
                    <div class="form-group">
                        <label for="genre">Genre</label>
                        <input
                            type="text"
                            class="form-control"
                            id="genre"
                            :value="activeGame.genre"
                            @input="(e) => {
                                updateActiveGame('genre', e.target.value);
                            }"
                            required
                        />
                    </div>
                    <div class="form-group">
                        <label for="played">Played?</label>
                        <select
                            class="form-control"
                            id="played"
                            :value="playedValue"
                            @change="(e) => {
                                updatePlayedValue(e.target.value);
                            }"
                            required
                        >
                            <option value="true">Yes</option>
                            <option value="false">No</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary">{{ isNewGame ? 'Add Game' : 'Update Game' }}</button>
                </form>
            </div>
        </div>
    </Teleport>
</template>

<style scoped>
.modal-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-container {
    position: relative;
    background: white;
    padding: 50px 100px;
    border-radius: 5px;
    box-shadow: 0px 10px 5px 2px rgba(0, 0, 0, 0.1);
    z-index: 1001;
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