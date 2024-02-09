import { useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Spinner from 'react-bootstrap/Spinner';
import { toast } from 'react-toastify';

import { AuthContext } from '../contexts/UserProvider';

export default function Logout() {

    const { logoutUser } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        logoutUser()
        toast.success("Logged Out!")
        navigate('/login');
    });

    return <Spinner animation="border" />;
}
