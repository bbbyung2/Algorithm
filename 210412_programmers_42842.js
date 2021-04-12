function solution(brown, yellow) {
    const total = brown + yellow;

    for (let index = Math.floor(total / 2); index > 0; index--) {
        if (total % index !== 0) continue;

        const width = index;
        const height = total / index;

        if ((width * 2 + height * 2) - 4 === brown) return [width, height];
    }
}
