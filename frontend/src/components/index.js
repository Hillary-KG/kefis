import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './Login';
import Home from './Home';
import Products from './../features/products/Products';
import { UserView } from '../features/products/Users';

const IndexPage = () => {
  return (        
    <Router>
        <Routes>
        <Route  exact path="/" element={<Home/>}/>
        <Route  exact path="/products" element={<Products/>}/>
        <Route  exact path="/users" element={<UserView/>}/>
        <Route exact path="/login" element={<LoginPage/>}/>
        </Routes>
    </Router>
  );
};

export default IndexPage;
