import { useState, useEffect } from 'react';
import { useLocation, Link } from 'react-router-dom';
import { roadmapAPI } from '../services/api';

function Roadmap() {
    const location = useLocation();
    const [roadmap, setRoadmap] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (location.state?.userProfileId && location.state?.selectedArtistIds) {
            generateRoadmap();
        } else {
            setLoading(false);
        }
    }, []);

    const generateRoadmap = async () => {
        try {
            setLoading(true);
            const response = await roadmapAPI.generate(
                location.state.userProfileId,
                location.state.selectedArtistIds
            );
            setRoadmap(response.data);
        } catch (error) {
            console.error('Error generating roadmap:', error);
        } finally {
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="text-center">
                    <div className="text-gray-600">Generating your personalized roadmap...</div>
                </div>
            </div>
        );
    }

    if (!roadmap) {
        return (
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="text-center">
                    <p className="text-gray-600 mb-4">No roadmap data found.</p>
                    <Link to="/start" className="text-primary-600 hover:underline">
                        Start a new search
                    </Link>
                </div>
            </div>
        );
    }

    return (
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div className="mb-8">
                <h1 className="text-4xl font-bold mb-4">Your 12-Month Creative Roadmap</h1>
                <p className="text-gray-600">
                    A personalized action plan inspired by successful artists who started similar to you.
                </p>
            </div>

            <div className="space-y-6">
                {roadmap.months.map((month) => (
                    <div
                        key={month.month}
                        className={`bg-white rounded-lg shadow-md p-6 ${month.decision_point ? 'border-2 border-yellow-400' : ''
                            }`}
                    >
                        <div className="flex items-start justify-between mb-3">
                            <div className="flex items-center space-x-3">
                                <div className="w-12 h-12 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold">
                                    {month.month}
                                </div>
                                <div>
                                    <h3 className="text-xl font-bold">{month.title}</h3>
                                    {month.inspired_by && (
                                        <p className="text-sm text-gray-500">
                                            Inspired by {month.inspired_by}
                                        </p>
                                    )}
                                </div>
                            </div>
                            {month.decision_point && (
                                <span className="bg-yellow-100 text-yellow-800 px-3 py-1 rounded text-sm font-semibold">
                                    Decision Point
                                </span>
                            )}
                        </div>
                        <p className="text-gray-700">{month.description}</p>

                        {month.decision_point && (
                            <div className="mt-4 bg-yellow-50 border border-yellow-200 rounded p-3">
                                <p className="text-sm text-yellow-800">
                                    💡 This is a key decision point. Evaluate if this step fits your situation and adjust as needed.
                                </p>
                            </div>
                        )}
                    </div>
                ))}
            </div>

            <div className="mt-8 bg-gray-50 rounded-lg p-6">
                <h3 className="font-bold mb-2">Remember:</h3>
                <ul className="list-disc list-inside space-y-1 text-gray-700">
                    <li>This roadmap is a guide, not a rigid plan</li>
                    <li>Adjust timelines based on your progress and circumstances</li>
                    <li>Focus on consistency over perfection</li>
                    <li>Celebrate small wins along the way</li>
                </ul>
            </div>

            <div className="mt-6 text-center">
                <Link
                    to="/artists"
                    className="inline-block bg-primary-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-primary-700 mr-4"
                >
                    Explore More Artists
                </Link>
                <Link
                    to="/start"
                    className="inline-block border-2 border-primary-600 text-primary-600 px-6 py-3 rounded-lg font-semibold hover:bg-primary-50"
                >
                    Create New Roadmap
                </Link>
            </div>
        </div>
    );
}

export default Roadmap;
