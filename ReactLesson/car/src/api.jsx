import axios from 'axios';

export const searchImages = async (term) => {
    const response = await axios.get('https://api.unsplash.com/search/photos',{
        headers:{
            Authorization: 'Client-ID npMkAmWmf2g3DSe7WpKswPSXlaNUqOELZUphvUdBVa4'
        },
        params:{
            query: term
        },
    });

    return response.data.result;
};