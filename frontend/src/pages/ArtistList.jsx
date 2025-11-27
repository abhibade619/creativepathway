import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { artistsAPI } from '../services/api';

function ArtistList() {
    const [artists, setArtists] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedDomain, setSelectedDomain] = useState('');

    useEffect(() => {
        fetchArtists();
    }, [selectedDomain]);

    const fetchArtists = async () => {
        try {
            setLoading(true);
            const response = await artistsAPI.getAll(selectedDomain || null);
            setArtists(response.data);
        } catch (error) {
            console.error('Error fetching artists:', error);
        } finally {
            setLoading(false);
        }
    };

    const domains = [
        'Singer',
        'Rapper',
        'YouTuber',
        'DJ',
        'Producer',
        'Actor',
        'Comedian',
        'Podcaster',
        'Gamer',
        'Dancer',
        'Entrepreneur',
        'Beauty',
        'Educator'
    ];

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <h1 className="text-4xl font-bold mb-8">Explore Artists</h1>

            {/* Filter */}
            <div className="mb-8">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                    Filter by Domain
                </label>
                <select
                    value={selectedDomain}
                    onChange={(e) => setSelectedDomain(e.target.value)}
                    className="border border-gray-300 rounded-lg px-4 py-2 w-full md:w-64"
                >
                    <option value="">All Domains</option>
                    {domains.map((domain) => (
                        <option key={domain} value={domain}>
                            {domain}
                        </option>
                    ))}
                </select>
                {selectedDomain && (
                    <p className="mt-2 text-sm text-gray-600">
                        Showing artists in: <span className="font-semibold">{selectedDomain}</span>
                    </p>
                )}
            </div>

            {/* Artists Grid */}
            {loading ? (
                <div className="text-center py-12">
                    <div className="text-gray-600">Loading artists...</div>
                </div>
            ) : (
                <>
                    <div className="mb-4 text-sm text-gray-600">
                        Found {artists.length} artist{artists.length !== 1 ? 's' : ''}
                    </div>
                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {artists.map((artist) => (
                            <Link
                                key={artist.id}
                                to={`/artists/${artist.id}`}
                                className="bg-white rounded-lg shadow-md hover:shadow-lg transition overflow-hidden"
                            >
                                <div className="h-48 bg-gradient-to-br from-primary-400 to-primary-600 flex items-center justify-center">
                                    <span className="text-white text-6xl font-bold">
                                        {artist.name.charAt(0)}
                                    </span>
                                </div>
                                <div className="p-6">
                                    <h3 className="text-xl font-bold mb-2">{artist.name}</h3>
                                    <p className="text-gray-600 mb-2">{artist.domain}</p>
                                    <div className="flex items-center text-sm text-gray-500 space-x-4">
                                        <span>Started at {artist.start_age}</span>
                                        {artist.first_break_age && (
                                            <span>• Breakthrough at {artist.first_break_age}</span>
                                        )}
                                    </div>
                                </div>
                            </Link>
                        ))}
                    </div>
                </>
            )}

            {!loading && artists.length === 0 && (
                <div className="text-center py-12">
                    <p className="text-gray-600">No artists found.</p>
                </div>
            )}
        </div>
    );
}

export default ArtistList;
