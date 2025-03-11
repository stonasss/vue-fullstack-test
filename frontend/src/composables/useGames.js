import { ref } from 'vue';
import axios from 'axios';

export function useGames() {
    const games = ref([]);

    const getGames = async () => {
        try {
            const path = 'http://localhost:5000/games';
            const res = await axios.get(path);
            games.value = res.data.games;
            console.log('Games fetched:', games.value);
        } catch (err) {
            console.error(err)
        }
    };

    const addGame = async (newGame) => {
        try {
            const path = 'http://localhost:5000/games';
            await axios.post(path, newGame);
            console.log('Game added successfully');
            await getGames();
        } catch (err) {
            console.error(err)
        }
    };

    const updateGame = async (id, updatedGame) => {
        try {
            const path = `http://localhost:5000/games/${id}`;
            await axios.put(path, updatedGame);
            console.log('Game updated successfully');
            await getGames();
        } catch (err) {
            console.error(err)
        }
    };

    const deleteGame = async (id) => {
        try {
            const path = `http://localhost:5000/games/${id}`;
            await axios.delete(path);
            console.log('Game deleted successfully');
            await getGames();
        } catch (err) {
            console.error(err)
        }
    };

    return {
        games,
        getGames,
        addGame,
        updateGame,
        deleteGame
    };
}
