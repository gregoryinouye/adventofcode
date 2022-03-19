/*

https://adventofcode.com/2019/day/7

*/

const code = [
  3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99
];

function run(intcode, input) {
  let ind = 0;
  let result = [];

  while (intcode[ind] !== 99) {
    const cmd = intcode[ind];
    const opcode = cmd % 100;
    const modes = cmd.toString().padStart(5, '0').slice(0, 3).split('').reverse().map(value => Number(value));

    const p1 = modes[0] === 0 && opcode !== 3 ? intcode[intcode[ind + 1]] : intcode[ind + 1];
    const p2 = modes[1] === 0 ? intcode[intcode[ind + 2]] : intcode[ind + 2];
    const p3 = modes[2] === 0 ? intcode[ind + 3] : 'error';
    console.log(ind)

    switch (opcode) {
      // add
      case 1:
        intcode[p3] = p1 + p2;
        console.log(p1, p2, p3)
        ind += 4;
        continue;
      // multiply
      case 2:
        intcode[p3] = p1 * p2;
        ind += 4;
        continue;
      // save input
      case 3:
        intcode[p1] = input.shift();
        ind += 2;
        continue;
      // output value
      case 4:
        result.push(p1);
        ind += 2;
        continue;
      // jump if true
      case 5:
        if (p1 !== 0) {
          ind = p2;
          continue;
        }
        ind += 3;
        continue;
      // jump if false
      case 6:
        if (p1 === 0) {
          ind = p2;
          continue;
        }
        ind += 3;
        continue;
      // less than
      case 7:
        intcode[p3] = p1 < p2 ? 1 : 0;
        ind += 4;
        continue;
      // equals
      case 8:
        intcode[p3] = p1 === p2 ? 1 : 0;
        ind += 4;
        continue;
    }
  }

  return result;
};

let max1 = 0;
const used = [];

for (let i = 0; i < 5; i++) {
  used.push(i);
  const A = run(code.slice(), [i, 0])[0];
  for (let j = 0; j < 5; j++) {
    if (used.includes(j)) continue;
    used.push(j);
    const B = run(code.slice(), [j, A])[0];
    for (let k = 0; k < 5; k++) {
      if (used.includes(k)) continue;
      used.push(k);
      const C = run(code.slice(), [k, B])[0];
      for (let l = 0; l < 5; l++) {
        if (used.includes(l)) continue;
        used.push(l);
        const D = run(code.slice(), [l, C])[0];
        for (let m = 0; m < 5; m++) {
          if (used.includes(m)) continue;
          max1 = Math.max(max1, run(code.slice(), [m, D])[0]);
        }
        used.pop();
      }
      used.pop();
    }
    used.pop();
  }
  used.pop();
}

// console.log(max1);
// 17406

// let max2 = 0;

// for (let i = 5; i < 10; i++) {
//   used.push(i);
//   const A = run(code.slice(), [i, 0])[0];
//   for (let j = 5; j < 10; j++) {
//     if (used.includes(j)) continue;
//     used.push(j);
//     const B = run(code.slice(), [j, A])[0];
//     for (let k = 5; k < 10; k++) {
//       if (used.includes(k)) continue;
//       used.push(k);
//       const C = run(code.slice(), [k, B])[0];
//       for (let l = 5; l < 10; l++) {
//         if (used.includes(l)) continue;
//         used.push(l);
//         const D = run(code.slice(), [l, C])[0];
//         for (let m = 5; m < 10; m++) {
//           if (used.includes(m)) continue;
//           let curr = run(code.slice(), [m, D])[0];

//           while (curr) {
//             curr = run(code.slice(), [curr]);
//           }

//           max2 = Math.max(max2, curr);
//         }
//         used.pop();
//       }
//       used.pop();
//     }
//     used.pop();
//   }
//   used.pop();
// }

// const test = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5];
// const test2 = test.slice();
// console.log(run(test2, [9, 0, 7, 8, 6, 5]))
// console.log(test2);
