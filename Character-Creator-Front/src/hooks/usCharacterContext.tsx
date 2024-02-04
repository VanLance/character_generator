import { useContext } from 'react';
import { CharacterContext } from '../contexts/CharacterProvider';

export default function useCharacterContext() {
  return useContext(CharacterContext);
}
