import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Container from 'react-bootstrap/esm/Container';

import Header from './components/Header';
import Login from './views/Login';
import Logout from './components/Logout';
import CharactersView from './views/CharactersView';
import CreateCharacter from './views/CreateCharacter';
import Index from './views/Index';
import Register from './views/Register';
import { ToastContainer } from 'react-toastify'
import useUserContext from './hooks/useUserContext';
// import CharacterView from './views/CharacterView';


function App() {

    const { user } = useUserContext()

    console.log(user);

    return (
        <Container fluid className="app" >
            <BrowserRouter>
                <Header />
                <Routes>
                    <Route path="/" element={<Index />} />
                    <Route path="/characters" element={<CharactersView />} />
                    <Route
                        path="/characters/:username"
                        element={<CharactersView />}
                    />
                    {/* <Route path="/character/:characterId" element={<CharacterView />} /> */}
                    <Route
                        path="/create-character"
                        element={<CreateCharacter />}
                    />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/logout" element={<Logout />} />
                </Routes>
            </BrowserRouter>
            <ToastContainer autoClose={3000} closeOnClick theme='dark'/>
        </Container>
    );
}

export default App;
