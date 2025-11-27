import { Link } from 'react-router-dom';

function Home() {
    return (
        <div className="min-h-screen">
            {/* Hero Section */}
            <div className="bg-gradient-to-r from-primary-600 to-primary-800 text-white">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
                    <div className="text-center">
                        <h1 className="text-5xl font-bold mb-6">
                            Find Your Creative Path
                        </h1>
                        <p className="text-xl mb-8 max-w-3xl mx-auto">
                            Discover how successful artists started their journey and get personalized guidance
                            based on your age, goals, and available time.
                        </p>
                        <Link
                            to="/start"
                            className="inline-block bg-white text-primary-600 hover:bg-gray-100 px-8 py-3 rounded-lg text-lg font-semibold transition"
                        >
                            Get Started
                        </Link>
                    </div>
                </div>
            </div>

            {/* Features Section */}
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
                <div className="grid md:grid-cols-3 gap-8">
                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <div className="text-primary-600 text-4xl mb-4">🎯</div>
                        <h3 className="text-xl font-bold mb-2">Find Similar Artists</h3>
                        <p className="text-gray-600">
                            Match with artists who started at your age and faced similar challenges.
                        </p>
                    </div>
                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <div className="text-primary-600 text-4xl mb-4">📅</div>
                        <h3 className="text-xl font-bold mb-2">See Their Timeline</h3>
                        <p className="text-gray-600">
                            Explore detailed career timelines showing what they did at each stage.
                        </p>
                    </div>
                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <div className="text-primary-600 text-4xl mb-4">🗺️</div>
                        <h3 className="text-xl font-bold mb-2">Get Your Roadmap</h3>
                        <p className="text-gray-600">
                            Receive a personalized 12-month action plan inspired by successful creators.
                        </p>
                    </div>
                </div>
            </div>

            {/* CTA Section */}
            <div className="bg-gray-100 py-16">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                    <h2 className="text-3xl font-bold mb-4">Ready to Start Your Journey?</h2>
                    <p className="text-lg text-gray-600 mb-8">
                        Answer a few questions and we'll match you with artists who followed similar paths.
                    </p>
                    <Link
                        to="/artists"
                        className="inline-block bg-primary-600 text-white hover:bg-primary-700 px-6 py-3 rounded-lg font-semibold mr-4 transition"
                    >
                        Browse Artists
                    </Link>
                    <Link
                        to="/start"
                        className="inline-block bg-white text-primary-600 border-2 border-primary-600 hover:bg-primary-50 px-6 py-3 rounded-lg font-semibold transition"
                    >
                        Find Your Match
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default Home;
