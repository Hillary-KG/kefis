import React, { useState } from 'react';

const OrdersTable = () => {
    const [orders, setOrders] = useState([]);
    return (
        <section>
            <div>
                <h1>Kefis Store Orders</h1>
            </div>
            <div>
                <table className='table'>
                    <th>
                        <tr>Order ID</tr>
                        <tr>Product ID</tr>
                    </th>
                    {orders.map((order) => {
                    return (
                        <div key={order.id} className='item'>
                            <tr>
                                <td>{order.id}</td>
                                <td>{order.product}</td>
                            </tr>
                        </div>
                    );
                })}
                </table>
            </div>
        </section>
    
    );
};

export default OrdersTable;