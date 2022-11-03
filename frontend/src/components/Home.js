import React from "react";
import { Link } from "react-router-dom";


const Home = () => {
    return (
        <div>
            <h1>Kefis Store</h1>
            <Link className="btn" to="/login" >login</Link>
        </div>
    );
};

export default Home;

