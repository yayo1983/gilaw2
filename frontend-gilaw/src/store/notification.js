import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  category: null,
  messageNotification: "",
  errorCategory: false,
  errorMessage: false,
};

const notificationSlice = createSlice({
  name: "notification",
  initialState: initialState,
  reducers: {
    clearForm(state) {
      state.category = "";
      state.messageNotification = "";
      state.errorCategory = false;
      state.errorMessage = false;
    },
    setCategory(state, action) {
      state.category = action.payload;
    },
    setMessage(state, action) {
      state.messageNotification = action.payload;
    },
    setErrorCategory(state, action) {
      state.errorCategory = action.payload;
    },
    setErrorMessage(state, action) {
      state.errorMessage = action.payload;
    },
  },
});
export const notificationActions = notificationSlice.actions;

export default notificationSlice.reducer;
