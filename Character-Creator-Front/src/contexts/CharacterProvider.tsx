import { createContext, useEffect, useState } from 'react';
import { CharacterWithStats } from '../types';
import useUserContext from '../hooks/useUserContext';

interface CharacterContextType {
    characters: CharacterWithStats[];
    setCharacters: React.Dispatch<React.SetStateAction<CharacterWithStats[]>>,
    deleteCharacter: (characterId: string) => void
}

export const CharacterContext = createContext<CharacterContextType>({} as CharacterContextType);

const base_api_url = import.meta.env.VITE_APP_BASE_API;

export default function DeleteProvider({
    children,
}: {
    children: JSX.Element | JSX.Element[];
}) {
    const [characters, setCharacters] = useState<CharacterWithStats[]>([]);

    const { removeUserCharacter, user } = useUserContext();

    useEffect(()=>{
        if(characters.length > 0 && !characters[0].user){
            console.log('if effect attaching');
            attachUserToCharacters()
        }
    },[characters])

    function attachUserToCharacters(){
        setCharacters( characters.map( character => Object.assign(character, { user: { id: user.id } })))
    }

    async function deleteCharacter(characterId: string) {

         const res = await fetch(
                `${base_api_url}/character/${characterId}`,
                {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: 'Bearer '.concat(user.token),
                    },
                }
            );

            if (res.ok) {
                const data = await res.json();
                console.log(data);
                removeUserCharacter(characterId);
                setCharacters(
                    characters.filter((character) => character.id !== characterId)
                );
            }
            
    }

    const value = {
        characters,
        setCharacters,
        deleteCharacter
    };

    return (
        <CharacterContext.Provider value={value}>
            {children}
        </CharacterContext.Provider>
    );
}
