import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { actionCreators } from '../store';
import { bindActionCreators } from '@reduxjs/toolkit';

const Products = () => {
    const products = useSelector((state) => state.products);
    const dispatch = useDispatch();
    const { saleAction} = bindActionCreators(actionCreators, dispatch);

    const handleClick = (product_id) => {
        try {
            saleAction(product_id);
        } catch (error) {
            console.log(error)
        }
    }
    return (
        <section>
            <div>
                <h1>Kefis Store Products</h1>
            </div>
            <div>
                <table className='table'>
                    <th>
                        <tr>Product ID</tr>
                        <tr>Product Name</tr>
                    </th>
                    {products.map((product) => {
                    return (
                        <div key={product.id} className='item'>
                            <tr>
                                <td>{product.id}</td>
                                <td>{product.name}</td>
                                <td>
                                    <button className='btn' onClick={handleClick}>
                                        sell
                                    </button>
                                </td>
                            </tr>
                        </div>
                    );
                })}
                </table>
            </div>
        </section>
    
    );
};

export default Products;