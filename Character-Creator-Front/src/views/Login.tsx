import { useContext, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

import Body from '../components/Body';
import { AuthContext } from '../contexts/UserProvider';
import { toast } from 'react-toastify';

const base_api_url = import.meta.env.VITE_APP_BASE_API;

export default function LoginPage() {
    const usernameField = useRef<HTMLInputElement>(null);
    const passwordField = useRef<HTMLInputElement>(null);

    const { user, loginUser } = useContext(AuthContext);

    const navigate = useNavigate();

    useEffect(() => {
        if (user.token || localStorage.getItem('token')) {
            toast.success(user.username.concat(' logged in!'));
            navigate('/');
        }
    }, [user]);

    async function handleLoginForm(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        try {
            const res = await fetch(`${base_api_url}/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: usernameField.current?.value,
                    password: passwordField.current?.value,
                }),
            });

            if (res.ok) {
                try {
                    const data = await res.json();

                    loginUser({
                        id: data.id,
                        username: usernameField.current?.value || '',
                        token: data.access_token,
                        characters: data.characters,
                    });
                } catch (e) {
                    console.log(e);
                }
                return;
            }
        } catch (e) {
            console.log(e);
        }
        toast.error('Login Failed / Try Again!');
    }

    return (
        <Body sidebar={false}>
            <h2>Login</h2>
            <form onSubmit={handleLoginForm} className="center-form">
                <label htmlFor="username">
                    Username:
                    <br />
                    <input type="text" name="username" ref={usernameField} />
                </label>
                <br />
                <br />
                <label htmlFor="password">
                    Password:
                    <br />
                    <input
                        type="password"
                        name="password"
                        ref={passwordField}
                    />
                </label>
                <br />
                <input type="submit" value="Submit" className="form-btn" />
            </form>
        </Body>
    );
}
