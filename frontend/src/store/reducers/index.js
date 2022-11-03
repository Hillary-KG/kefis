import { combineReducers } from "@reduxjs/toolkit";
import productsReducer from "./productReducer";


const reducers = combineReducers({
    product: productsReducer
});

export default reducers;    