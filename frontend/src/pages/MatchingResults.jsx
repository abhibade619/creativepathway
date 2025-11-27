import { useLocation, useNavigate, Link } from 'react-router-dom';

function MatchingResults() {
    const location = useLocation();
    const navigate = useNavigate();
    const matchData = location.state?.matchData;

    if (!matchData) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="text-center">
                    <p className="text-gray-600 mb-4">No matching data found.</p>
                    <Link to="/start" className="text-primary-600 hover:underline">
                        Start a new search
                    </Link>
                </div>
            </div>
        );
    }

    const { matches, user_profile_id } = matchData;

    const handleGenerateRoadmap = () => {
        const selectedArtistIds = matches.slice(0, 3).map(m => m.artist.id);
        navigate('/roadmap', {
            state: {
                userProfileId: user_profile_id,
                selectedArtistIds
            }
        });
    };

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <h1 className="text-4xl font-bold mb-4">Your Matches</h1>
            <p className="text-gray-600 mb-8">
                We found {matches.length} artists with similar starting points to yours.
            </p>

            <div className="space-y-6">
                {matches.map((match, index) => (
                    <div key={match.artist.id} className="bg-white rounded-lg shadow-md p-6">
                        <div className="flex items-start justify-between mb-4">
                            <div className="flex items-start space-x-4">
                                <div className="w-20 h-20 bg-gradient-to-br from-primary-400 to-primary-600 rounded-full flex items-center justify-center flex-shrink-0">
                                    <span className="text-white text-3xl font-bold">
                                        {match.artist.name.charAt(0)}
                                    </span>
                                </div>
                                <div>
                                    <h2 className="text-2xl font-bold mb-1">{match.artist.name}</h2>
                                    <p className="text-gray-600 mb-2">{match.artist.domain}</p>
                                    <div className="flex items-center space-x-2">
                                        <span className="bg-primary-100 text-primary-800 px-3 py-1 rounded text-sm font-semibold">
                                            {Math.round(match.similarity_score)}% Match
                                        </span>
                                        <span className="text-sm text-gray-500">
                                            #{index + 1} Best Match
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <Link
                                to={`/artists/${match.artist.id}`}
                                className="text-primary-600 hover:text-primary-700 font-medium"
                            >
                                View Full Timeline →
                            </Link>
                        </div>

                        {/* Match Reasons */}
                        <div className="mb-4">
                            <h3 className="font-semibold mb-2">Why this match:</h3>
                            <ul className="list-disc list-inside space-y-1 text-gray-700">
                                {match.match_reasons.map((reason, idx) => (
                                    <li key={idx}>{reason}</li>
                                ))}
                            </ul>
                        </div>

                        {/* Events at User's Age */}
                        {match.events_at_user_age && match.events_at_user_age.length > 0 && (
                            <div className="bg-gray-50 rounded-lg p-4">
                                <h3 className="font-semibold mb-3">What they were doing around your age:</h3>
                                <div className="space-y-3">
                                    {match.events_at_user_age.map((event) => (
                                        <div key={event.id} className="border-l-4 border-primary-600 pl-4">
                                            <div className="flex items-center space-x-2 mb-1">
                                                <span className="font-semibold">Age {event.age}:</span>
                                                <span>{event.title}</span>
                                            </div>
                                            {event.description && (
                                                <p className="text-sm text-gray-600">{event.description}</p>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}
                    </div>
                ))}
            </div>

            {/* Generate Roadmap CTA */}
            <div className="mt-8 bg-primary-50 border-2 border-primary-200 rounded-lg p-6 text-center">
                <h3 className="text-xl font-bold mb-2">Ready for Your Personalized Roadmap?</h3>
                <p className="text-gray-700 mb-4">
                    Get a 12-month action plan inspired by these artists' early career moves.
                </p>
                <button
                    onClick={handleGenerateRoadmap}
                    className="bg-primary-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-primary-700"
                >
                    Generate My Roadmap
                </button>
            </div>
        </div>
    );
}

export default MatchingResults;
