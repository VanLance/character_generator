import { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

import Body from '../components/Body';
import useUserContext from '../hooks/useUserContext';

export default function Register() {
    const usernameField = useRef<HTMLInputElement>(null);
    const emailField = useRef<HTMLInputElement>(null);
    const passwordField = useRef<HTMLInputElement>(null);

    const { user, loginUser } = useUserContext();

    const navigate = useNavigate();

    const base_api_url = import.meta.env.VITE_APP_BASE_API;

    useEffect(() => {
        if (user.token) {
            localStorage.setItem('token', JSON.stringify(user.token));
            localStorage.setItem('username', JSON.stringify(user.username));
        }

        if (user.token || localStorage.getItem('token')) navigate('/');
    }, [user]);

    async function handleRegisterForm(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();

        const res = await fetch(`${base_api_url}/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: usernameField.current?.value,
                email: emailField.current?.value,
                password: passwordField.current?.value,
            }),
        });

        if (res.ok) {
            const data = await res.json();
            
            loginUser(data)
            navigate('/');
        }
    }

    return (
        <Body sidebar={false}>
            <h2>Register Page</h2>
            <form onSubmit={handleRegisterForm} className="center-form">
                <label htmlFor='username'>
                    Username:
                    <br />
                    <input type="text" ref={usernameField} name='username'/>
                </label>
                <br />
                <br />
                <label htmlFor='email'>
                    Email:
                    <br />
                    <input type="email" ref={emailField} name='email'/>
                </label>
                <br />
                <br />
                <label htmlFor='password'>
                    Password:
                    <br />
                    <input type="password" ref={passwordField} name='password'/>
                </label>
                <br />
                <br />
                <button>Register</button>
            </form>
        </Body>
    );
}
