import kefisApis from "../../utils/api/api";

const initialState = {};
const productsReducer = (state = initialState, action) => {

    switch (action.type) {
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

export default productsReducer;