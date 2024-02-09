import { NavLink } from 'react-router-dom';
import Container from 'react-bootstrap/esm/Container';
import { GiWomanElfFace } from 'react-icons/gi';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import useUserContext from '../hooks/useUserContext';
import NavDropdown from 'react-bootstrap/esm/NavDropdown';
import { ToastContainer } from 'react-toastify';

export default function Header() {
    const { user } = useUserContext();

    return (
        <>
            <Navbar
                data-bs-theme="dark"
                bg="dark"
                sticky="top"
                className="header mb-3"
            >
                <Container>
                    <Navbar.Brand style={{ color: '#FF79C6' }}>
                        Character Generator
                    </Navbar.Brand>
                    {user.username ? (
                        <Nav.Link as={NavLink} to="/logout">
                            Logout
                        </Nav.Link>
                    ) : (
                        <NavDropdown
                            title={<GiWomanElfFace />}
                            id="basic-nav-dropdown"
                            style={{ marginRight: '2rem' }}
                        >
                            <NavDropdown.Item as={NavLink} to="/login">
                                Login
                            </NavDropdown.Item>
                            <NavDropdown.Item as={NavLink} to="/register">
                                Register
                            </NavDropdown.Item>
                        </NavDropdown>
                    )}
                </Container>
            </Navbar>
            <ToastContainer autoClose={3000} closeOnClick theme="dark" />
        </>
    );
}
