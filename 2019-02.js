/*

https://adventofcode.com/2019/day/2

*/

const input = [
  1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 6, 23, 2, 6, 23, 27, 2, 27, 9, 31, 1, 5, 31, 35, 1, 35, 10, 39, 2, 39, 9, 43, 1, 5, 43, 47, 2, 47, 10, 51, 1, 51, 6, 55, 1, 5, 55, 59, 2 ,6, 59, 63, 2, 63, 6, 67, 1, 5, 67, 71, 1, 71, 9, 75, 2, 75, 10, 79, 1, 79, 5, 83, 1, 10, 83, 87, 1, 5, 87, 91, 2, 13, 91, 95, 1, 95, 10, 99, 2, 99, 13, 103, 1, 103, 5, 107, 1, 107, 13, 111, 2, 111 ,9, 115, 1, 6, 115, 119, 2, 119, 6, 123, 1, 123, 6, 127, 1, 127, 9, 131, 1, 6, 131, 135, 1, 135, 2, 139, 1, 139, 10, 0, 99, 2, 0, 14, 0
];

function run(intcode) {
  let ind = 0;

  while (intcode[ind] !== 99) {
    const opcode = intcode[ind];
    const v1 = intcode[intcode[ind + 1]];
    const v2 = intcode[intcode[ind + 2]];
    const resInd = intcode[ind + 3];

    if (opcode === 1) intcode[resInd] = v1 + v2;
    if (opcode === 2) intcode[resInd] = v1 * v2;  
    ind += 4;
  }

  return intcode[0];
};

const input2 = input.slice();
input2[1] = 12;
input2[2] = 2;
run(input2);

// 6730673

for (let noun = 0; noun < 100; noun++) {
  for (let verb = 0; verb < 100; verb++) {
    const input3 = input.slice();
    input3[1] = noun;
    input3[2] = verb;

    if (run(input3) === 19690720) {
      console.log(100 * noun + verb);
      break;
    }
  }
}

// 3749
