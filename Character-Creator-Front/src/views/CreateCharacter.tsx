import { useState, useContext } from 'react';
import { Container } from 'react-bootstrap';

import CharacterCard from '../components/CharacterCard';
import { AuthContext } from '../contexts/UserProvider';
import { Character, CharacterWithStats } from '../types';
import Body from '../components/Body';
import useCharacterContext from '../hooks/usCharacterContext';

const base_api_url = import.meta.env.VITE_APP_BASE_API;

export default function CreateCharacter() {
    const { user } = useContext(AuthContext);

    const [character, setCharacter] = useState<Character | CharacterWithStats>();
    const { characters, setCharacters } = useCharacterContext();


    const handleCharacterForm = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        const formData = new FormData(e.target as HTMLFormElement);

        const characterInfo = {
            name: formData.get('name')?.toString() || '',
            level: formData.get('level')?.toString() || '',
            race: formData.get('race')?.toString() || '',
            _class: formData.get('_class')?.toString() || '',
            gender: formData.get('gender')?.toString() || '',
        };

        await apiCall(characterInfo);
    };

    const apiCall = async (characterInfo: Character) => {

        const res = await fetch(base_api_url.concat('/character'), {
            method: 'POST',
            headers: {
                Authorization: 'Bearer '.concat(user.token) ,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: characterInfo.name,
                level: characterInfo.level,
                race: characterInfo.race,
                _class: characterInfo._class,
                gender: characterInfo.gender,
            }),
        });

        if (res.ok) {
            //  bug check character context and make func to update characters
            const characterData = await res.json();
            setCharacter(characterData);
            setCharacters([...characters, characterData])
        } else console.log(res.status);
    };

    return (
        <Body sidebar>
            <h1 className="heading">Create Character <br/> for {user.username} </h1>

            <Container className="flexContainer">
                <form onSubmit={handleCharacterForm}>
                    <label htmlFor="name">
                        Name: <br />
                        <input type="text" name="name" required />
                    </label>
                    <br />
                    <label htmlFor="gender">
                        Gender:
                        <br /> <input type="text" name="gender" required />
                    </label>
                    <br />
                    <label htmlFor="level">
                        Level:
                        <br /> <input type="text" name="level" />
                    </label>

                    <br />
                    <label htmlFor="race">
                        Race: <br />
                        <input type="text" name="race" required />
                    </label>

                    <br />
                    <label htmlFor="_class">
                        Class: <br />
                        <input type="text" name="_class" />
                    </label>
                    <br />
                    <button>Submit</button>
                </form>

                {character?.name && (
                    <CharacterCard character={character as CharacterWithStats} />
                )}

            </Container>
        </Body>
    );
}
