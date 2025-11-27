import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { artistsAPI } from '../services/api';

function ArtistDetail() {
    const { id } = useParams();
    const [artist, setArtist] = useState(null);
    const [timeline, setTimeline] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchArtistData();
    }, [id]);

    const fetchArtistData = async () => {
        try {
            setLoading(true);
            const [artistRes, timelineRes] = await Promise.all([
                artistsAPI.getById(id),
                artistsAPI.getTimeline(id),
            ]);
            setArtist(artistRes.data);
            setTimeline(timelineRes.data);
        } catch (error) {
            console.error('Error fetching artist data:', error);
        } finally {
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="text-center">Loading...</div>
            </div>
        );
    }

    if (!artist) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="text-center">Artist not found</div>
            </div>
        );
    }

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            {/* Artist Header */}
            <div className="bg-white rounded-lg shadow-md p-8 mb-8">
                <div className="flex items-start space-x-6">
                    <div className="w-32 h-32 bg-gradient-to-br from-primary-400 to-primary-600 rounded-full flex items-center justify-center">
                        <span className="text-white text-5xl font-bold">
                            {artist.name.charAt(0)}
                        </span>
                    </div>
                    <div className="flex-1">
                        <h1 className="text-4xl font-bold mb-2">{artist.name}</h1>
                        <p className="text-xl text-gray-600 mb-4">{artist.domain}</p>
                        <p className="text-gray-700 mb-4">{artist.short_bio}</p>
                        <div className="flex flex-wrap gap-4 text-sm">
                            <div className="bg-primary-100 text-primary-800 px-3 py-1 rounded">
                                Started at age {artist.start_age}
                            </div>
                            {artist.first_break_age && (
                                <div className="bg-green-100 text-green-800 px-3 py-1 rounded">
                                    Breakthrough at age {artist.first_break_age}
                                </div>
                            )}
                            {artist.training_type && (
                                <div className="bg-blue-100 text-blue-800 px-3 py-1 rounded">
                                    {artist.training_type}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {/* Career Timeline */}
            <div className="bg-white rounded-lg shadow-md p-8">
                <h2 className="text-2xl font-bold mb-6">Career Timeline</h2>
                <div className="space-y-6">
                    {timeline.map((event, index) => (
                        <div key={event.id} className="flex">
                            <div className="flex flex-col items-center mr-4">
                                <div className="w-12 h-12 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold">
                                    {event.age}
                                </div>
                                {index < timeline.length - 1 && (
                                    <div className="w-0.5 h-full bg-gray-300 mt-2"></div>
                                )}
                            </div>
                            <div className="flex-1 pb-8">
                                <div className="bg-gray-50 rounded-lg p-4">
                                    <div className="flex items-start justify-between mb-2">
                                        <h3 className="text-lg font-semibold">{event.title}</h3>
                                        {event.year && (
                                            <span className="text-sm text-gray-500">{event.year}</span>
                                        )}
                                    </div>
                                    {event.description && (
                                        <p className="text-gray-700 mb-3">{event.description}</p>
                                    )}
                                    <div className="flex flex-wrap gap-2">
                                        {event.event_type && (
                                            <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded">
                                                {event.event_type}
                                            </span>
                                        )}
                                        {event.risk_level && (
                                            <span className={`text-xs px-2 py-1 rounded ${event.risk_level === 'high' ? 'bg-red-100 text-red-800' :
                                                    event.risk_level === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                                                        'bg-green-100 text-green-800'
                                                }`}>
                                                Risk: {event.risk_level}
                                            </span>
                                        )}
                                        {event.outcome && (
                                            <span className={`text-xs px-2 py-1 rounded ${event.outcome === 'positive' ? 'bg-green-100 text-green-800' :
                                                    event.outcome === 'negative' ? 'bg-red-100 text-red-800' :
                                                        'bg-gray-100 text-gray-800'
                                                }`}>
                                                {event.outcome}
                                            </span>
                                        )}
                                    </div>
                                    {event.skills && event.skills.length > 0 && (
                                        <div className="mt-2 flex flex-wrap gap-1">
                                            {event.skills.map((skill, idx) => (
                                                <span key={idx} className="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">
                                                    {skill}
                                                </span>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default ArtistDetail;
