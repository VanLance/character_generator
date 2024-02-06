import { useContext, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Container from 'react-bootstrap/esm/Container';
import Spinner from 'react-bootstrap/Spinner';

import CharacterCard from './CharacterCard';
import { AuthContext } from '../contexts/UserProvider';
import useCharacterContext from '../hooks/usCharacterContext';

const base_api_url = import.meta.env.VITE_APP_BASE_API;

export default function Characters() {
    const { user } = useContext(AuthContext);
    const { username } = useParams();
    const { characters, setCharacters } = useCharacterContext();

    async function getAllCharacters() {
        const res = await fetch(`${base_api_url}/character`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (res.ok) {
            const data = await res.json();
            return data;
        }
    }

    function getUserCharacters() {
        return user.characters;
    }

    useEffect(() => {
        (async () => {
            if (username) {
                setCharacters(getUserCharacters());
                return;
            }
            setCharacters(await getAllCharacters());
        })();
    }, [username]);

    if (characters.length === 0) return <Spinner />;

    return (
        <div>
            <h1 className="heading">Characters</h1>
            <Container className="character-cards">
                {characters &&
                    characters.map((character) => (
                        <CharacterCard
                            character={character}
                            key={character.id}
                        />
                    ))}
            </Container>
        </div>
    );
}
