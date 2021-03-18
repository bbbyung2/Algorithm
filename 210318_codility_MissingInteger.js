function solution(A) {
    ASet = new Set(A);
    A = [...ASet].sort((a, b) => a - b)
    let count = 1;

    for(let i = 0; i < A.length; i++) {
        if (A[i] > 0 && A[i] === count) {
            count++;
        } else if (A[i] > 0 && A[i] !== count) {
            break;
        }
    }

    return count;
}
