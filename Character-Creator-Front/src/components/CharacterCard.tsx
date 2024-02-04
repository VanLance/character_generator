import Card from 'react-bootstrap/Card';
import { Dispatch, SetStateAction } from 'react';
import { CompleteCharacter } from '../types';
import ListGroup from 'react-bootstrap/esm/ListGroup';
import { useContext } from 'react';
import { AuthContext } from '../contexts/UserProvider';
import useCharacterContext from '../hooks/usCharacterContext';

const base_api_url = import.meta.env.VITE_APP_BASE_API;

interface CharacterCardable {
    character: CompleteCharacter;
    characters?: CompleteCharacter[];
    setCharacters?: Dispatch<SetStateAction<CompleteCharacter[]>>;
}

export default function CharacterCard({
    character,
    characters,
    setCharacters,
}: CharacterCardable) {
    const { user } = useContext(AuthContext);
    const { setDeleted } = useCharacterContext();

    async function updateCharacter(characterId: string) {
        console.log(characterId);
        return;
    }

    async function deleteCharacter(characterId: string) {
        window.confirm('Are you sure you want to delete this post?') &&
            (await fetch(`${base_api_url}/delete/${characterId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'x-access-token': user.token,
                },
            }));
    }

    return (
        <Card style={{ width: '18rem' }} className="c-card">
            {/* {character.pic ?
        <Card.Img variant="top" src="holder.js/100px180?text=Image cap" /> : ''} */}
            <Card.Body>
                <Card.Title>{character.name}</Card.Title>
                <Card.Text>
                    {character.name + ' '}
                    Level {' ' + character.level}{' '}
                    {character._class[0].toUpperCase() +
                        character._class.slice(1)}
                    {' ' +
                        character.race[0].toUpperCase() +
                        character.race.slice(1)}
                </Card.Text>
                <p>
                    hp: {character.hp} ac: {character.ac}
                </p>
            </Card.Body>
            <ListGroup className="list-group-flush">
                <ListGroup.Item>Strength: {character.strength}</ListGroup.Item>
                <ListGroup.Item>
                    Dexterity: {character.dexterity}
                </ListGroup.Item>
                <ListGroup.Item>
                    Constitution: {character.constitution}
                </ListGroup.Item>
                <ListGroup.Item>Wisdom: {character.wisdom}</ListGroup.Item>
                <ListGroup.Item>
                    Intellegence: {character.intellegence}
                </ListGroup.Item>
                {user.token === character.user_token && (
                    <ListGroup.Item className="buttonSection">
                        <button
                            onClick={() => {
                                updateCharacter(character.id || '');
                            }}
                        >
                            Update
                        </button>
                        <button
                            onClick={() => {
                                deleteCharacter(character.id || '');
                                setDeleted(true);
                                if (setCharacters && characters) {
                                    setCharacters(
                                        characters.filter(
                                            (current_character) =>
                                                current_character.id !==
                                                character.id
                                        )
                                    );
                                }
                            }}
                        >
                            Delete
                        </button>
                    </ListGroup.Item>
                )}
            </ListGroup>
        </Card>
    );
}
