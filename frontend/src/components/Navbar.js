import React from 'react';
import { Link } from 'react-router-dom';
const Navbar = () => {
  return (
    <nav className='nav'>
      <span><Link to="/" className='btn'>Kefis-Store</Link></span>
      <span><Link to="/" className='btn'>Home</Link></span>
      <span><Link to="/login" className='btn'>login</Link></span>
    </nav>
  );
};

export default Navbar;
