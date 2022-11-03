import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './Login';
import Home from './Home';
import Navbar from './Navbar';
import Products from './Products';

const IndexPage = () => {
  return (        
    <Router>
        {/* <Navbar/> */}
        <Routes>
        <Route  exact path="/" element={<Home/>}/>
        <Route  exact path="/products" element={<Products/>}/>
        <Route exact path="/login" element={<LoginPage/>} className="btn"/>
        </Routes>
    </Router>
  );
};

export default IndexPage;
