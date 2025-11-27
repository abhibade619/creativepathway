import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Artists API
export const artistsAPI = {
    getAll: (domain = null) => {
        const params = domain ? { domain } : {};
        return api.get('/artists', { params });
    },
    getById: (id) => api.get(`/artists/${id}`),
    getTimeline: (id) => api.get(`/artists/${id}/timeline`),
    create: (data) => api.post('/artists', data),
};

// Matching API
export const matchingAPI = {
    matchUser: (userProfile) => api.post('/match', { user_profile: userProfile }),
};

// Roadmap API
export const roadmapAPI = {
    generate: (userProfileId, selectedArtistIds) =>
        api.post('/roadmap/generate', {
            user_profile_id: userProfileId,
            selected_artist_ids: selectedArtistIds,
        }),
    getById: (id) => api.get(`/roadmap/${id}`),
};

export default api;
