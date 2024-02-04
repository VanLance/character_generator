import { createContext, useState } from 'react';
import { CompleteCharacter } from '../types';

interface CharacterContextType {
    characters: CompleteCharacter[];
    setCharacters: React.Dispatch<React.SetStateAction<CompleteCharacter[]>>;
    setDeleted: React.Dispatch<React.SetStateAction<boolean>>;
    deleteCharacter: (characterId: string) => void;
    deleted: boolean;
}

export const CharacterContext = createContext<CharacterContextType>({} as CharacterContextType);

export default function DeleteProvider({
    children,
}: {
    children: JSX.Element | JSX.Element[];
}) {
    const [characters, setCharacters] = useState<CompleteCharacter[]>([]);
    const [deleted, setDeleted] = useState(false);

    function deleteCharacter(characterId: string) {
        setCharacters(
            characters.filter((character) => character.id !== characterId)
        );
    }

    const value = {
        characters,
        setCharacters,
        deleted,
        setDeleted,
        deleteCharacter,
    };
    return (
        <CharacterContext.Provider value={value}>
            {children}
        </CharacterContext.Provider>
    );
}
