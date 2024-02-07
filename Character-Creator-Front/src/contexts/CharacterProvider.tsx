import { createContext, useEffect, useState } from 'react';
import { CharacterWithStats } from '../types';
import useUserContext from '../hooks/useUserContext';

interface CharacterContextType {
    characters: CharacterWithStats[];
    setCharacters: React.Dispatch<React.SetStateAction<CharacterWithStats[]>>;
    getCharacters: () => Promise<CharacterWithStats[] | void>;
    deleteCharacter: (characterId: string) => void;
}

export const CharacterContext = createContext<CharacterContextType>(
    {} as CharacterContextType
);

const base_api_url = import.meta.env.VITE_APP_BASE_API;

export default function DeleteProvider({
    children,
}: {
    children: JSX.Element | JSX.Element[];
}) {
    const [characters, setCharacters] = useState<CharacterWithStats[]>([]);
    const { removeUserCharacter, user } = useUserContext();

    useEffect(() => {
        
        if (!characters || characters.length === 0) {
            (async () => {
                const charactersData = await getCharacters();
                if (charactersData) {
                    setCharacters(charactersData);
                }
            })();
        }

        

    }, [characters]);


    async function getCharacters() {
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

    async function deleteCharacter(characterId: string) {
        const res = await fetch(`${base_api_url}/character/${characterId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                Authorization: 'Bearer '.concat(user.token),
            },
        });

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
        getCharacters,
        deleteCharacter,
    };

    return (
        <CharacterContext.Provider value={value}>
            {children}
        </CharacterContext.Provider>
    );
}
