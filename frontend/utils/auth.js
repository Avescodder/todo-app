import Cookies from 'js-cookie';

const TOKEN_KEY = 'auth_token';

export const saveToken = (token) => {
  if (typeof window !== 'undefined') {
    Cookies.set(TOKEN_KEY, token, { expires: 7 });
  }
};

export const getToken = () => {
  if (typeof window !== 'undefined') {
    return Cookies.get(TOKEN_KEY);
  }
  return null;
};

export const removeToken = () => {
  if (typeof window !== 'undefined') {
    Cookies.remove(TOKEN_KEY);
  }
};

export const isAuthenticated = () => {
  return !!getToken();
};

export const requireAuth = () => {
  if (typeof window !== 'undefined' && !isAuthenticated()) {
    window.location.href = '/login';
    return false;
  }
  return true;
};