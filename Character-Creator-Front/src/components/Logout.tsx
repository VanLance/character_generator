import { useContext, useEffect } from 'react';
import { AuthContext } from '../contexts/UserProvider';
import { useNavigate } from 'react-router-dom';
import Spinner from 'react-bootstrap/Spinner';

export default function Logout() {

    const { logoutUser } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        logoutUser()
        navigate('/login');
    });

    return <Spinner animation="border" />;
}
