import { createAsyncThunk } from '@reduxjs/toolkit';
import serviceAuth from '../../services/auth.service';

export const loginAuth = createAsyncThunk('auth/loginAuth', async (params) => {
    try {
        const { username, password } = params;
        const result = await serviceAuth.loginAuth({ username, password });
        if (result.status !== 200) {
            return false;
        }
        localStorage.setItem("id", result.data.id);
        return result.data;
    } catch (error) {
        return false;
    }
});