import { configureStore } from '@reduxjs/toolkit'
import userReducer from '../features/products/userSlice'
import productReducer from '../features/products/productSlice'

export const store = configureStore({
  reducer: {
    user: userReducer,
    product: productReducer
  }
})