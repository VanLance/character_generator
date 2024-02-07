import { useState, useContext } from 'react';
import { Container } from 'react-bootstrap';

import CharacterCard from '../components/CharacterCard';
import { AuthContext } from '../contexts/UserProvider';
import { Character, CharacterWithStats, CharacterOptions } from '../types';
import Body from '../components/Body';
import useCharacterContext from '../hooks/usCharacterContext';
import { titleCase } from '../utilityFunc';
import useUserContext from '../hooks/useUserContext';

const base_api_url = import.meta.env.VITE_APP_BASE_API;

export default function CreateCharacter() {
    const { user } = useContext(AuthContext);

    const [character, setCharacter] = useState<
        Character | CharacterWithStats
    >();
    const { characters, setCharacters } = useCharacterContext();
    const { updateUserCharacters } = useUserContext()

    const characterOptions: CharacterOptions = {
        races: [
            'dragonborn',
            'dwarf',
            'elf',
            'gnome',
            'half-elf',
            'halfling',
            'half-orc',
            'tiefling',
        ],
        archetypes: [
            'barbarian',
            'bard',
            'cleric',
            'druid',
            'fighter',
            'dex_fighter',
            'monk',
            'paladin',
            'ranger',
            'rogue',
            'sorcerer',
            'warlock',
            'wizard',
        ],
        genders: ['male', 'female'],
        levels: [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            'random',
        ],
    };

    const handleCharacterForm = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        const formData = new FormData(e.target as HTMLFormElement);

        const characterInfo = {
            name: formData.get('name')?.toString() || '',
            level: formData.get('level')?.toString() || '',
            race: formData.get('race')?.toString() || '',
            archetype: formData.get('archetype')?.toString() || '',
            gender: formData.get('gender')?.toString() || '',
        };

        await apiCall(characterInfo);
    };

    const apiCall = async (characterInfo: Character) => {
        console.log(characterInfo);
        
        const res = await fetch(base_api_url.concat('/character'), {
            method: 'POST',
            headers: {
                Authorization: 'Bearer '.concat(user.token),
                'Content-Type': 'application/json',
            },
            body: JSON.stringify( characterInfo ),
        });

        if (res.ok) {
            const characterData = await res.json();
            setCharacter(characterData);
            setCharacters([...characters, characterData]);
            updateUserCharacters([...user.characters, characterData])
        } else console.log(res.status);
    };

    return (
        <Body sidebar>
            <h1 className="heading">
                Create Character <br /> for {user.username}{' '}
            </h1>

            <Container className="flex-col-center">
                <form onSubmit={handleCharacterForm}>
                    <label htmlFor="name">
                        Name: <br />
                        <input type="text" name="name" required />
                    </label>
                    <br />
                    {Object.entries(characterOptions).map(
                        ([att, options], i) => {
                            return (
                                <div key={i}>
                                    <label htmlFor={att}>
                                        {titleCase(att.slice(0,-1))}: <br />
                                        <select
                                            name={att.slice(0,-1)}
                                            id={att.concat('-select')}
                                            style={{ width: '10rem' }}
                                        >
                                            {options.map(
                                                (
                                                    choice: string | number,
                                                    i: number
                                                ) => {
                                                    return (
                                                        <option
                                                            key={i}
                                                            value={choice}
                                                        >
                                                            {choice}
                                                        </option>
                                                    );
                                                }
                                            )}
                                            <option value="random">
                                                Random
                                            </option>
                                        </select>
                                    </label>
                                    <br />
                                </div>
                            );
                        }
                    )}
                    <input type="submit" value="Create" className="form-btn" />
                </form>

                {character?.name && (
                    <CharacterCard
                        character={character as CharacterWithStats}
                    />
                )}
            </Container>
        </Body>
    );
}
