import React from "react";

export const saleAction = (product_id) => {
    return (dispatch) => {
        dispatch({
            type: "sell",
            payload: product_id
        });
    }
}