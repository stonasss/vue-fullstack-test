<script setup>
    import { ref, onMounted, computed } from 'vue'
    import { useGames } from '@/composables/useGames';
    import GameModal from './GameModal.vue';

    const { games, getGames, addGame, updateGame, deleteGame } = useGames();

    const isModalOpen = ref(false)
    const isNewGame = ref(false)
    const newGame = ref({
        title: '',
        genre: '',
        played: false
    });
    const selectedGame = ref({
        _id: '',
        title: '',
        genre: '',
        played: false
    });

    const activeGame = computed(() => {
        return isNewGame.value ? newGame.value : selectedGame.value;
    })

    const playedValue = computed({
        get() {
            return activeGame.value.played ? 'true' : 'false';
        },
        set(value) {
            activeGame.value.played = value === 'true';
        }
    });

    const openUpdateModal = (game) => {
        selectedGame.value = { ...game };
        isNewGame.value = false;
        isModalOpen.value = true;
    };

    const closeModal = () => {
        isModalOpen.value = false;
        selectedGame.value = { _id: '', title: '', genre: '', played: false };
    };

    const handleSubmit = () => {
        if (isNewGame.value) {
            console.log('Adding game:', newGame.value);
            addGame({ ...newGame.value }).then(() => {
                newGame.value = { title: '', genre: '', played: false };
                closeModal();
            });
        } else {
            console.log('Updating game:', selectedGame.value);
            updateGame(selectedGame.value._id, { ...selectedGame.value }).then(() => {
                closeModal();
            });
        }
    };

    const updateActiveGame = (updatedGame) => {
        if (isNewGame.value) {
            newGame.value = { ...newGame.value, ...updatedGame };
        } else {
            selectedGame.value = { ...selectedGame.value, ...updatedGame };
        }
    };


    const updatePlayedValue = (value) => {
        activeGame.value.played = value === 'true';
    };

    onMounted(() => {
        getGames();
    });
</script>

<template>
    <div class="jumbotron vertical-center">
        <div class="container">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css" integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R" crossorigin="anonymous"/>
            <div>
                <h1 class="text-center bg-primary text-white" style="border-radius: 10px;">Games Library</h1>
                <hr><br>

                <button type="button" class="btn btn-success btn-sm" @click="isModalOpen = true; isNewGame = true">
                    Add Game
                </button>
                <hr><br>

                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Genre</th>
                            <th scope="col">Played?</th>
                            <th scope="col">Actions</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="game, index in games" :key="game._id">
                            <td>{{ game.title }}</td>
                            <td>{{ game.genre }}</td>
                            <td>
                                <span v-if="game.played">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <td>
                                <div class="btn-group" role="group">
                                    <button type="button" class="btn btn-info btn-sm" style="margin-right: 10px;" @click="openUpdateModal(game)">Update</button>
                                    <button type="button" class="btn btn-danger btn-sm" @click="deleteGame(game._id)">Delete</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <footer class="bg-primary text-white text-center" style="border-radius: 10px;">Copyright &copy;. All Rights Reserved 2025.</footer>
            </div>

            <GameModal
                :isModalOpen="isModalOpen"
                :isNewGame="isNewGame"
                :activeGame="activeGame"
                :playedValue="playedValue"
                @close-modal="closeModal"
                @submit="handleSubmit"
                @update:activeGame="updateActiveGame"
                @update:playedValue="updatePlayedValue"
            />
        </div>
    </div>
</template>
