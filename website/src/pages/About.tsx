import { useNavigate } from 'react-router-dom';
import Company from './Company';

// About page redirects to Company page for simplicity
function About() {
  return <Company />;
}

export default About;

