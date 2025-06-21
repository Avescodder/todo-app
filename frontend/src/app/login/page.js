'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import AuthForm from '../../../components/AuthForm';
import { authAPI } from '../../../utils/api';
import { saveToken, isAuthenticated } from '../../../utils/auth';

export default function Login() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();

  useEffect(() => {
    if (isAuthenticated()) {
      router.push('/dashboard');
    }
  }, [router]);

  const handleLogin = async (formData) => {
    setIsLoading(true);
    setError('');

    try {
      const response = await authAPI.login({
        username: formData.username,
        password: formData.password
      });

      // Save token and redirect
      saveToken(response.data.access);
      router.push('/dashboard');
    } catch (err) {
      setError(
        err.response?.data?.detail || 
        err.response?.data?.message || 
        'Login failed. Please check your credentials.'
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="w-full max-w-md">
        <AuthForm
          title="Login"
          onSubmit={handleLogin}
          isLoading={isLoading}
          error={error}
          isRegister={false}
        />
        
        <div className="mt-6 text-center">
          <p className="text-gray-600">
            Don't have an account?{' '}
            <Link href="/register" className="text-blue-600 hover:text-blue-500">
              Sign up
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}