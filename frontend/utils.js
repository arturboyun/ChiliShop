export const savePersonalData = (payload) => {
  localStorage.setItem('personal_data', JSON.stringify(payload))
}

export const saveDeliveryData = (payload) => {
  localStorage.setItem('delivery_data', JSON.stringify(payload))
}

export const getPersonalData = () => {
  return JSON.parse(localStorage.getItem('personal_data'))
}

export const getDeliveryData = () => {
  return JSON.parse(localStorage.getItem('delivery_data'))
}
