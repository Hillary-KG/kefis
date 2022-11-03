import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './Login';

const Home = () => {
  return (
    <div>
      <h1>Home Page</h1>
      <Router>
        <Routes>
            <Route exact path="/login" className="btn">
               <LoginPage/>
            </Route>
        </Routes>
    </Router>
    </div>
  );
};

export default Home;