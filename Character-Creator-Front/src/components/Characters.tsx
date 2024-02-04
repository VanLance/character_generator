import { useContext, useEffect, useState } from 'react';
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
        return await fetch(`${base_api_url}/universe`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
    }

    async function getUserCharacters() {
        return await fetch(base_api_url.concat('/api/characters'), {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': user.token,
            },
        });
    }

    useEffect(() => {
        (async () => {
            const res = username
                ? await getUserCharacters()
                : await getAllCharacters();
            const charactersData = await res.json();

            console.log(charactersData);
            setCharacters(charactersData);
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
                            characters={characters}
                            setCharacters={setCharacters}
                        />
                    ))}
            </Container>
        </div>
    );
}
