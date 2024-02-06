import { createContext, useEffect, useState } from 'react';
import { CharacterWithStats, LoggedUser } from '../types';

interface UserContextType {
    user: LoggedUser;
    setUser: React.Dispatch<React.SetStateAction<LoggedUser>>;
    removeUserCharacter: (characterId: string) => void;
    updateUserCharacters: (characters: CharacterWithStats[]) => void;
    loginUser: ( user: LoggedUser) => void
    logoutUser: () => void;
}

export const AuthContext = createContext<UserContextType>(
    {} as UserContextType
);

export default function AuthProvider({
    children,
}: {
    children: JSX.Element | JSX.Element[];
}) {
    const [user, setUser] = useState<LoggedUser>({} as LoggedUser);

    useEffect(() => {
        if (localStorage.getItem('user') && !user.id) {
            updateUserFromLocal();
            return;
        }

        if (user.id && !localStorage.getItem('user')) {
            updateLocalFromUser();
        }
    }, [user]);

    function updateUserFromLocal() {
        setUser(JSON.parse(localStorage.getItem('user') ?? ''));
      
        
    }

    function updateLocalFromUser() {
        localStorage.setItem('user', JSON.stringify(user));
    }

    function loginUser(user: LoggedUser){
      setUser(user)
    }

    function logoutUser() {
        localStorage.removeItem('user');
        setUser({} as LoggedUser);
    }

    function updateUserCharacters(characters: CharacterWithStats[]) {
        setUser({ ...user, characters });
    }

    function removeUserCharacter(characterId: string) {
        const updatedCharacters = user.characters.filter(
            (character) => character.id !== characterId
        );
        setUser({ ...user, characters: updatedCharacters });
    }

    const value = {
        user,
        setUser,
        removeUserCharacter,
        updateUserCharacters,
        loginUser,
        logoutUser,
    };

    return (
        <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
    );
}
