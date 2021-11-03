const personalDataKey = 'personal_data';
const deliveryDataKey = 'delivery_data';
const basketItemsKey = 'basket_items';


// LocalStorage

const getLocalStorageItem = (key) => {
  return JSON.parse(localStorage.getItem(key));
}

const setLocalStorageItem = (key, payload) => {
  localStorage.setItem(key, JSON.stringify(payload));
}


// Forms

export const savePersonalData = (payload) => {
  setLocalStorageItem(personalDataKey, payload);
}

export const getPersonalData = () => {
  return getLocalStorageItem(personalDataKey);
}

export const saveDeliveryData = (payload) => {
  setLocalStorageItem(deliveryDataKey, payload);
}

export const getDeliveryData = () => {
  return getLocalStorageItem(deliveryDataKey);
}


// Basket

export const getBasketItems = () => {
  return getLocalStorageItem(basketItemsKey);
}

export const setBasketItems = (payload) => {
  return setLocalStorageItem(basketItemsKey, payload);
}

export const addItemToBasket = (product, size, quantity) => {
  const basketItems = getBasketItems();

  if (!basketItems) {
    setBasketItems([{ product, size, quantity }]);
  } else {
    let itemExists = basketItems.find(item => item.product.id === product.id && item.size === size);

    if (itemExists) {
      const updatedBasketItems = basketItems.map((item) => {
        if (item.product.id === product.id && item.size === size) {
          item.product = product;
          item.size = size;
          if (item.quantity + quantity > 0 || item.quantity > item.product.quantity) {
            item.quantity += quantity;
          }
        }
        return item;
      })

      setBasketItems(updatedBasketItems);
    } else {
      basketItems.push({ product, size, quantity });
      setBasketItems(basketItems);
    }
  }
}

export const removeBasketItem = (product_id, size) => {
  const basketItems = getBasketItems();

  const updatedBasketItems = basketItems.filter((item) => {
    return item.product.id !== product_id || item.size !== size;
  });

  setBasketItems(updatedBasketItems);
  return updatedBasketItems;
}

export const decreaseProductQuantity = (product_id, size) => {
  const basketItems = getBasketItems();
  const updatedBasketItems = basketItems.map((item) => {
    if (item.product.id === product_id && item.size === size) {
      if (item.quantity - 1 > 0 || item.quantity > item.product.quantity) {
        item.quantity--;
      }
    }
    return item;
  })
  setBasketItems(updatedBasketItems);
  return updatedBasketItems;
}
