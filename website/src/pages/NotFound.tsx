import { Link } from 'react-router-dom';
import { Home, Search, ArrowLeft } from 'lucide-react';

function NotFound() {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="text-center max-w-lg">
        <div className="mb-8">
          <div className="text-9xl font-bold font-bold text-primary-600 mb-4">404</div>
          <h1 className="text-4xl font-bold font-bold text-gray-900 mb-4">Page Not Found</h1>
          <p className="text-lg text-gray-600 mb-8">
            Oops! The page you're looking for doesn't exist. It might have been moved or deleted.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link to="/" className="btn-primary inline-flex items-center justify-center">
            <Home className="w-5 h-5 mr-2" />
            Go Home
          </Link>
          <Link to="/products" className="btn-outline inline-flex items-center justify-center">
            <Search className="w-5 h-5 mr-2" />
            Browse Products
          </Link>
        </div>

        <div className="mt-12 pt-8 border-t border-gray-200">
          <p className="text-sm text-gray-600 mb-4">Looking for something specific?</p>
          <div className="flex flex-wrap justify-center gap-4 text-sm">
            <Link to="/products" className="text-primary-600 hover:text-primary-700 transition-colors">
              Products
            </Link>
            <span className="text-gray-400">•</span>
            <Link to="/documentation" className="text-primary-600 hover:text-primary-700 transition-colors">
              Documentation
            </Link>
            <span className="text-gray-400">•</span>
            <Link to="/support" className="text-primary-600 hover:text-primary-700 transition-colors">
              Support
            </Link>
            <span className="text-gray-400">•</span>
            <Link to="/company" className="text-primary-600 hover:text-primary-700 transition-colors">
              About Us
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default NotFound;

