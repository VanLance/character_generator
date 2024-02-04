import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { NavLink } from 'react-router-dom';
import { useContext, useEffect } from 'react';
import { AuthContext } from '../contexts/UserProvider';

export default function Sidebar() {
    const { user, setUser } = useContext(AuthContext);

    useEffect(() => {
        const storedToken = localStorage.getItem('token');
        if (storedToken && !user.token) {
            setUser({
                username: JSON.parse(localStorage.getItem('username') || ''),
                token: JSON.parse(storedToken),
                loggedIn: true,
            });
        }
    });

    return (
        <Navbar sticky="top" className="flex-column sidebar">
            <Nav.Item>
                <Nav.Link as={NavLink} to="/characters">
                    Character Universe
                </Nav.Link>
            </Nav.Item>
            {user.username && (
                <>
                    <Nav.Item>
                        <Nav.Link
                            as={NavLink}
                            to={`/characters/${user.username}`}
                        >
                            My Characters
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link as={NavLink} to="/create-character">
                            Create Character
                        </Nav.Link>
                    </Nav.Item>
                </>
            )}
        </Navbar>
    );
}
