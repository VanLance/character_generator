import { useContext } from 'react';
import { AuthContext } from '../contexts/UserProvider';

export default function useUserContext() {
  return useContext(AuthContext);
}
