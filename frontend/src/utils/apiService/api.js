import { get, post, put } from "./base";

const BASE_URL = "http://localhost:5000";

const kefisApis = {
    registerUser: (newUser) => post(BASE_URL + "/users/register", newUser),
    login: (user) => post(BASE_URL + "/users/login", user),
    getProducts: (products) => get(BASE_URL + "/products/get-all", products),
    addProduct: (newProduct) => post(BASE_URL + "/users/register", newProduct),
    makeSale: (product_id) => post(BASE_URL + "/products/sell/"+product_id),
    getReorders: (reorders) => get(BASE_URL + "/reorders/ge-all", reorders),
}

export default kefisApis;