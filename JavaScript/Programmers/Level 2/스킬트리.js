function solution(skill, skill_trees) {
    return skill_trees
        .map((tree) => [...tree].filter((item) => skill.includes(item)).join(""))
        .filter((tree) => [...new Set([...tree, ...skill])].join("") === skill)
        .length
}