import { createContext, useState } from 'react';

interface UserContextType {
  user: User;
  setUser: React.Dispatch<React.SetStateAction<User>>;
}

interface User {
  readonly id?: string;
  token: string;
  username: string;
  email?: string;
  loggedIn: boolean;
}

export const AuthContext = createContext<UserContextType>({} as UserContextType);

export default function AuthProvider({
  children,
}: {
  children: JSX.Element | JSX.Element[];
}) {
  const [user, setUser] = useState<User>({
    username: '',
    token: '',
    email: '',
    loggedIn: false,
  });

  const value = {
    user,
    setUser,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
