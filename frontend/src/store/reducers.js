import { combineReducers, createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import kefisApis from "../utils/apiService/api";

export const incrementAsync = createAsyncThunk(
  'counter/fetchCount',
  async (product_id) => {
    const response = await kefisApis.makeSale(product_id);
    // The value we return becomes the `fulfilled` action payload
    return response.data;
  }
);

const productsReducer = (state, action) => {
    const products = state.products
    switch (action.type) {
        case "get":
            return products
        case "sell":
            const product_id = action.payload;
            try {
                const res = kefisApis.makeSale(product_id)
                return res.json();
            } catch (error) {
                console.log(error);
                return;
            }
        default:
            return state
    }
}


const reducers = combineReducers({
    product: productsReducer
});

export default reducers;

