import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="bg-white shadow-lg">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                    <div className="flex">
                        <Link to="/" className="flex items-center">
                            <span className="text-2xl font-bold text-primary-600">
                                Creative Pathways
                            </span>
                        </Link>
                    </div>
                    <div className="flex items-center space-x-4">
                        <Link
                            to="/artists"
                            className="text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
                        >
                            Artists
                        </Link>
                        <Link
                            to="/start"
                            className="bg-primary-600 text-white hover:bg-primary-700 px-4 py-2 rounded-md text-sm font-medium"
                        >
                            Get Started
                        </Link>
                    </div>
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
