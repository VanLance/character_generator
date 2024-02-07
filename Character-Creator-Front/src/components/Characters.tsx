import { useContext } from 'react';
import { useParams } from 'react-router-dom';
import Container from 'react-bootstrap/esm/Container';
import Spinner from 'react-bootstrap/Spinner';

import CharacterCard from './CharacterCard';
import { AuthContext } from '../contexts/UserProvider';
import useCharacterContext from '../hooks/usCharacterContext';
import { Character, CharacterWithStats } from '../types';

export default function Characters() {
    const { user } = useContext(AuthContext);
    const { username } = useParams();
    const { characters } = useCharacterContext();

    if (characters.length === 0) return <Spinner />;

    return (
        <div>
            <h1 className="heading">
                {username && username.concat("'s ")}Characters
            </h1>
            <Container className="character-cards">
                {(username ? user.characters : characters).map(
                    (character: CharacterWithStats) => (
                        <CharacterCard
                            character={character}
                            key={character.id}
                        />
                    )
                )}
            </Container>
        </div>
    );
}
