import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { matchingAPI } from '../services/api';

function UserInput() {
    const navigate = useNavigate();
    const [step, setStep] = useState(1);
    const [loading, setLoading] = useState(false);
    const [formData, setFormData] = useState({
        age: '',
        domain: '',
        experience_level: 'beginner',
        hours_per_week: 10,
        constraints: '',
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const response = await matchingAPI.matchUser(formData);
            // Navigate to results page with data
            navigate('/matches', { state: { matchData: response.data } });
        } catch (error) {
            console.error('Error matching user:', error);
            alert('Error finding matches. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const nextStep = () => setStep(step + 1);
    const prevStep = () => setStep(step - 1);

    return (
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div className="bg-white rounded-lg shadow-md p-8">
                <h1 className="text-3xl font-bold mb-6">Find Your Creative Path</h1>

                {/* Progress Bar */}
                <div className="mb-8">
                    <div className="flex justify-between mb-2">
                        {[1, 2, 3, 4].map((s) => (
                            <div
                                key={s}
                                className={`w-1/4 h-2 rounded ${s <= step ? 'bg-primary-600' : 'bg-gray-200'
                                    }`}
                            ></div>
                        ))}
                    </div>
                    <p className="text-sm text-gray-600">Step {step} of 4</p>
                </div>

                <form onSubmit={handleSubmit}>
                    {/* Step 1: Age */}
                    {step === 1 && (
                        <div>
                            <h2 className="text-xl font-semibold mb-4">How old are you?</h2>
                            <input
                                type="number"
                                name="age"
                                value={formData.age}
                                onChange={handleChange}
                                required
                                min="10"
                                max="100"
                                className="w-full border border-gray-300 rounded-lg px-4 py-3 text-lg"
                                placeholder="Enter your age"
                            />
                            <button
                                type="button"
                                onClick={nextStep}
                                disabled={!formData.age}
                                className="mt-6 w-full bg-primary-600 text-white py-3 rounded-lg font-semibold hover:bg-primary-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
                            >
                                Next
                            </button>
                        </div>
                    )}

                    {/* Step 2: Domain */}
                    {step === 2 && (
                        <div>
                            <h2 className="text-xl font-semibold mb-4">What's your creative domain?</h2>
                            <select
                                name="domain"
                                value={formData.domain}
                                onChange={handleChange}
                                required
                                className="w-full border border-gray-300 rounded-lg px-4 py-3 text-lg"
                            >
                                <option value="">Select a domain</option>
                                <option value="Singer">Singer</option>
                                <option value="Singer-Songwriter">Singer-Songwriter</option>
                                <option value="Rapper">Rapper</option>
                                <option value="Producer">Producer</option>
                                <option value="YouTuber">YouTuber</option>
                                <option value="Musician">Musician</option>
                                <option value="Content Creator">Content Creator</option>
                            </select>
                            <div className="mt-6 flex space-x-4">
                                <button
                                    type="button"
                                    onClick={prevStep}
                                    className="flex-1 border border-gray-300 py-3 rounded-lg font-semibold hover:bg-gray-50"
                                >
                                    Back
                                </button>
                                <button
                                    type="button"
                                    onClick={nextStep}
                                    disabled={!formData.domain}
                                    className="flex-1 bg-primary-600 text-white py-3 rounded-lg font-semibold hover:bg-primary-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
                                >
                                    Next
                                </button>
                            </div>
                        </div>
                    )}

                    {/* Step 3: Experience & Time */}
                    {step === 3 && (
                        <div>
                            <h2 className="text-xl font-semibold mb-4">Tell us about your experience</h2>

                            <div className="mb-6">
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Experience Level
                                </label>
                                <select
                                    name="experience_level"
                                    value={formData.experience_level}
                                    onChange={handleChange}
                                    className="w-full border border-gray-300 rounded-lg px-4 py-3"
                                >
                                    <option value="beginner">Beginner - Just starting out</option>
                                    <option value="intermediate">Intermediate - Some experience</option>
                                    <option value="advanced">Advanced - Experienced</option>
                                </select>
                            </div>

                            <div className="mb-6">
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Hours per week you can dedicate: {formData.hours_per_week}
                                </label>
                                <input
                                    type="range"
                                    name="hours_per_week"
                                    value={formData.hours_per_week}
                                    onChange={handleChange}
                                    min="1"
                                    max="40"
                                    className="w-full"
                                />
                                <div className="flex justify-between text-xs text-gray-500">
                                    <span>1 hour</span>
                                    <span>40 hours</span>
                                </div>
                            </div>

                            <div className="mt-6 flex space-x-4">
                                <button
                                    type="button"
                                    onClick={prevStep}
                                    className="flex-1 border border-gray-300 py-3 rounded-lg font-semibold hover:bg-gray-50"
                                >
                                    Back
                                </button>
                                <button
                                    type="button"
                                    onClick={nextStep}
                                    className="flex-1 bg-primary-600 text-white py-3 rounded-lg font-semibold hover:bg-primary-700"
                                >
                                    Next
                                </button>
                            </div>
                        </div>
                    )}

                    {/* Step 4: Constraints */}
                    {step === 4 && (
                        <div>
                            <h2 className="text-xl font-semibold mb-4">Any constraints or special circumstances?</h2>
                            <textarea
                                name="constraints"
                                value={formData.constraints}
                                onChange={handleChange}
                                rows="4"
                                className="w-full border border-gray-300 rounded-lg px-4 py-3"
                                placeholder="e.g., Working full-time, student, limited budget, small town, etc. (optional)"
                            ></textarea>

                            <div className="mt-6 flex space-x-4">
                                <button
                                    type="button"
                                    onClick={prevStep}
                                    className="flex-1 border border-gray-300 py-3 rounded-lg font-semibold hover:bg-gray-50"
                                >
                                    Back
                                </button>
                                <button
                                    type="submit"
                                    disabled={loading}
                                    className="flex-1 bg-primary-600 text-white py-3 rounded-lg font-semibold hover:bg-primary-700 disabled:bg-gray-300"
                                >
                                    {loading ? 'Finding Matches...' : 'Find My Matches'}
                                </button>
                            </div>
                        </div>
                    )}
                </form>
            </div>
        </div>
    );
}

export default UserInput;
