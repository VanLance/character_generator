import { useParams } from 'react-router-dom';

import Body from '../components/Body';
import CharacterCard from '../components/CharacterCard';
import { CompleteCharacter } from '../types';

export default function CharactersView({
    character,
}: {
    character: CompleteCharacter;
}) {
    const { characterId } = useParams();

    function getCharacter() {
        console.log(characterId);
    }

    return (
        <Body sidebar>
            <CharacterCard character={character} />
        </Body>
    );
}
