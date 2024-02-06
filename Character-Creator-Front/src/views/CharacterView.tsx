
import Body from '../components/Body';
import CharacterCard from '../components/CharacterCard';
import { CharacterWithStats } from '../types';

export default function CharactersView({
    character,
}: {
    character: CharacterWithStats;
}) {

    return (
        <Body sidebar>
            <CharacterCard character={character} />
        </Body>
    );
}
