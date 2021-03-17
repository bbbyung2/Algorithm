function solution(A) {
    const totalCounter = A.reduce((counter, element) => {
        counter[element] = counter[element] ? counter[element] + 1 : 1;
        return counter;
    }, {})

    for (let index in totalCounter) {
        if (totalCounter[index] % 2 === 1) {
            return Number(index);
        }
    }
}
