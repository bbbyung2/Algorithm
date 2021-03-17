function solution(N) {
    const binaryNumber = N.toString(2);
    const binaryGaps = binaryNumber.slice(binaryNumber.indexOf('1') + 1, binaryNumber.lastIndexOf('1'));
    const zeroCount = binaryGaps.split('1').map(zeros => zeros.length);

    return zeroCount.length ? Math.max(...zeroCount) : 0;
}
