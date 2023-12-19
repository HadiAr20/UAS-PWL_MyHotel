import { createSlice } from '@reduxjs/toolkit';
import { loginAuth } from '../actions/auth.action';

const initialState = {
    dataUser: {},
    isAuthenticated: false,
    loading: false,
    error: null,
};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        logoutAuth: (state) => {
            state.isAuthenticated = false;
            state.dataUser = {};
            state.loading = false;
            state.error = null;
        },
    },
    extraReducers: (builder) => {
        builder.addCase(loginAuth.pending, (state) => {
            state.loading = true;
        });
        builder.addCase(loginAuth.fulfilled, (state, action) => {
            state.loading = false;
            state.isAuthenticated = true;
            state.dataUser = action.payload;
        });
        builder.addCase(loginAuth.rejected, (state, action) => {
            state.loading = false;
            state.error = action.payload;
        });
    },
});

export const { logoutAuth } = authSlice.actions;
export default authSlice.reducer;