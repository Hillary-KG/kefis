import React from 'react';
import { Link } from 'react-router-dom';
const Navbar = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/" className='btn'>Home</Link>
        </li>
        <li>
          <Link to="/login" className='btn'>login</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
