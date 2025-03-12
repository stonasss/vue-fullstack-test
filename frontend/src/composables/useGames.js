import { ref } from 'vue';
import axios from 'axios';

export function useGames() {
    const games = ref([]);

    const api = axios.create({
        baseURL: 'http://localhost:5000'
    });

    api.interceptors.request.use((config) => {
        const token = localStorage.getItem('token')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config
    })

    const getGames = async () => {
        try {
            const res = await api.get('/games');
            games.value = res.data.games;
            console.log('Games fetched:', games.value);
        } catch (err) {
            console.error(err)
        }
    };

    const addGame = async (newGame) => {
        try {
            await api.post('/games', newGame);
            console.log('Game added successfully');
            await getGames();
        } catch (err) {
            console.error(err)
        }
    };

    const updateGame = async (id, updatedGame) => {
        try {
            await api.put(`/games/${id}`, updatedGame);
            console.log('Game updated successfully');
            await getGames();
        } catch (err) {
            console.error(err)
        }
    };

    const deleteGame = async (id) => {
        try {
            await api.delete(`/games/${id}`);
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
