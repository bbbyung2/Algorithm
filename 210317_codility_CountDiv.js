function solution(A, B, K) {
    const answer = parseInt(B / K) - parseInt(A / K);
    return A % K === 0 ? answer + 1 : answer;
}
