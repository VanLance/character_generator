import { Dispatch, SetStateAction, useContext } from 'react';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/esm/ListGroup';

import { CharacterWithStats } from '../types';
import { AuthContext } from '../contexts/UserProvider';
import useCharacterContext from '../hooks/usCharacterContext';


interface CharacterCardProps {
    character: CharacterWithStats;
    characters?: CharacterWithStats[];
    setCharacters?: Dispatch<SetStateAction<CharacterWithStats[]>>;
}

export default function CharacterCard({ character }: CharacterCardProps) {

    const { user } = useContext(AuthContext);
    const { deleteCharacter } = useCharacterContext()

    const {
        hp,
        ac,
        strength,
        dexterity,
        intelligence,
        constitution,
        wisdom,
        charisma,
    } = character.stats;

    async function updateCharacter(characterId: string) {
        console.log(characterId);
        return;
    }

    async function handleDeleteClick() {
        const userDelete = window.confirm(
            'Are you sure you want to delete this post?'
        );
        if (userDelete) {
           deleteCharacter(character.id)
        }
    }

    return (
        <Card style={{ width: '18rem' }} className="c-card">
            {/* {character.pic ?
        <Card.Img variant="top" src="holder.js/100px180?text=Image cap" /> : ''} */}
            <Card.Body>
                <Card.Title>{character.name}</Card.Title>
                <Card.Text>
                    Level {' ' + character.level}{' '}
                    {character._class[0].toUpperCase() +
                        character._class.slice(1)}
                    {' ' +
                        character.race[0].toUpperCase() +
                        character.race.slice(1)}
                </Card.Text>
                <p>
                    hp: {hp} ac: {ac}
                </p>
            </Card.Body>
            <ListGroup className="list-group-flush">
                <ListGroup.Item>Strength: {strength}</ListGroup.Item>
                <ListGroup.Item>Dexterity: {dexterity}</ListGroup.Item>
                <ListGroup.Item>Constitution: {constitution}</ListGroup.Item>
                <ListGroup.Item>Wisdom: {wisdom}</ListGroup.Item>
                <ListGroup.Item>Intelligence: {intelligence}</ListGroup.Item>
                <ListGroup.Item>Charisma: {charisma}</ListGroup.Item>

                {user.id === character.user?.id && (
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
                                handleDeleteClick();
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
