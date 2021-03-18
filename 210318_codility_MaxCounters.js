function solution(N, A) {
    const counter = new Array(N).fill(0);
    let maxCounter = 0;
    let tempMaxCounter = 0;

    A.forEach((element) => {
        const index = element - 1;

        if (element <= N) {
            counter[index] = Math.max(counter[index], maxCounter);
            counter[index]++;
            tempMaxCounter = Math.max(counter[index], tempMaxCounter);
        } else {
            maxCounter = tempMaxCounter;
        }
    })

    counter.forEach((element, index, array) => {
        array[index] = Math.max(element, maxCounter);
    })

    return counter;
}
