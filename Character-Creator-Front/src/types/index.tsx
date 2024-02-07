interface Character {
  archetype: string;
  name: string;
  race: string;
  gender: string;
  level: string | number;
}

interface Stats {
  strength: string | number;
  wisdom: string | number;
  charisma: string | number;
  constitution: string | number;
  dexterity: string | number;
  intelligence: string | number;
  hp: string | number;
  ac: string | number;
  spellDC: string | number;
}

type CharacterWithStats = Character & {
  id: string
  user: {id:string, username: string}
  stats: Stats
};

interface User {
  username: string;
  email?: string;
}


type LoggedUser = User & {
  readonly id: string
  readonly token: string
  characters: CharacterWithStats[]
}

type CharacterOptions = {
  archetypes: string[],
  races: string[],
  genders: string[],
  levels: Array<string | number>,
}

export type {
  Character, Stats, CharacterWithStats, LoggedUser, User, CharacterOptions
}