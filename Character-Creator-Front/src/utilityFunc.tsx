function titleCase(str: string):string{
    return str.split(' ').map((word: string) => word[0].toUpperCase().concat(word.slice(1).toLowerCase())).join(' ')
}

export { titleCase }