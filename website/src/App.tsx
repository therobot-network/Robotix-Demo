import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import Products from './pages/Products';
import ProductDetail from './pages/ProductDetail';
import Documentation from './pages/Documentation';
import CustomerPortal from './pages/CustomerPortal';
import Support from './pages/Support';
import About from './pages/About';
import Company from './pages/Company';
import DemoFiles from './pages/DemoFiles';
import NotFound from './pages/NotFound';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<Products />} />
          <Route path="/products/:productId" element={<ProductDetail />} />
          <Route path="/documentation" element={<Documentation />} />
          <Route path="/documentation/:docId" element={<Documentation />} />
          <Route path="/customer-portal" element={<CustomerPortal />} />
          <Route path="/demo-files" element={<DemoFiles />} />
          <Route path="/support" element={<Support />} />
          <Route path="/about" element={<About />} />
          <Route path="/company" element={<Company />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;

