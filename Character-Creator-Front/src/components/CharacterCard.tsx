import { Dispatch, SetStateAction, useContext } from 'react';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/esm/ListGroup';

import { CharacterWithStats } from '../types';
import { AuthContext } from '../contexts/UserProvider';
import useCharacterContext from '../hooks/usCharacterContext';
import { titleCase } from '../utilityFunc';

interface CharacterCardProps {
    character: CharacterWithStats;
    characters?: CharacterWithStats[];
    setCharacters?: Dispatch<SetStateAction<CharacterWithStats[]>>;
}

export default function CharacterCard({ character }: CharacterCardProps) {
    const { user } = useContext(AuthContext);
    const { deleteCharacter } = useCharacterContext();

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
            deleteCharacter(character.id);
        }
    }

    return (
        <Card style={{ width: '18rem' }} className="c-card" data-bs-theme='dark'>
            {/* {character.pic ?
        <Card.Img variant="top" src="holder.js/100px180?text=Image cap" /> : ''} */}
            <Card.Body style={{
                borderBottom: '3px solid #F1FA8C'
            }}>
                <Card.Title className='heading' style={{color: '#F1FA8C'}}>{character.name}</Card.Title>
                <Card.Text className='blue-txt'>
                    Level {character.level} 
                    {' '.concat(titleCase(character.archetype))}
                    {' '.concat(titleCase(character.race))} <br />
                    HP: {' '+ hp} AC: {' ' + ac}
                </Card.Text>
            </Card.Body>
            <ListGroup className="list-group-flush">
                <ListGroup.Item className="blue-txt">Strength: {strength}</ListGroup.Item>
                <ListGroup.Item className="blue-txt">Dexterity: {dexterity}</ListGroup.Item>
                <ListGroup.Item className="blue-txt">Constitution: {constitution}</ListGroup.Item>
                <ListGroup.Item className="blue-txt">Wisdom: {wisdom}</ListGroup.Item>
                <ListGroup.Item className="blue-txt">Intelligence: {intelligence}</ListGroup.Item>
                <ListGroup.Item className="blue-txt">Charisma: {charisma}</ListGroup.Item>

                <ListGroup.Item className="d-flex justify-content-center">
                    <span>Owner: {character.user ? character.user.username: user.username}</span>
                </ListGroup.Item>
                {user.id === character.user?.id && (
                    <ListGroup.Item className="btn-container">
                        <button
                            className="btn"
                            onClick={() => {
                                updateCharacter(character.id || '');
                            }}
                        >
                            Update
                        </button>
                        <button
                            className="btn"
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
