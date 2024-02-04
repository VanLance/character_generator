export interface Character {
  _class: string;
  name: string;
  race: string;
  gender: string;
  level: string | number;
  id?: string;
}

export interface Stats {
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

export type CompleteCharacter = Character & Stats & {
  user_token? : string
};
