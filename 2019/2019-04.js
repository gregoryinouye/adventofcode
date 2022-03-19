/*

https://adventofcode.com/2019/day/4

*/

const rangeStart = 153517;
const rangeEnd = 630395;
let count = 0;

for (let i = rangeStart; i <= rangeEnd; i++) {
  const string = i.toString();
  let hasConsecutive = false;
  let hasNoDecrease = true;

  for (let j = 0; j < string.length - 1; j++) {
    const curr = string[j];
    const next = string[j + 1];
    if (curr === next) hasConsecutive = true;
    if (Number(curr) > Number(next)) {
      hasNoDecrease = false;
      break;
    }
  }

  if (hasConsecutive && hasNoDecrease) count++;
}

console.log('Part 1: ', count);

// 1729

count = 0;

for (let i = rangeStart; i <= rangeEnd; i++) {
  const string = i.toString();
  let hasConsecutive = false;
  let hasNoDecrease = true;

  for (let j = 0; j < string.length - 1; j++) {
    const curr = string[j];
    const next = string[j + 1];
    if (curr === next && next !== string[j + 2] && curr !== string[j - 1]) hasConsecutive = true;
    if (Number(curr) > Number(next)) {
      hasNoDecrease = false;
      break;
    }
  }

  if (hasConsecutive && hasNoDecrease) count++;
}

console.log('Part 2: ', count);
// 1172
