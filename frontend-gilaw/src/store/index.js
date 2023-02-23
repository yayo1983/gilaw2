import { configureStore } from '@reduxjs/toolkit';
import notificationReducer from './notification';


const store = configureStore({
    reducer: { notificationr: notificationReducer },
  });

export default store;

