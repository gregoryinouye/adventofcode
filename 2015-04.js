/*

https://adventofcode.com/2015/day/4

*/

const crypto = require('crypto');

const prefix = 'yzbqklnj';

for (let i = 1; i < 2000000; i++) {
  const hash = crypto.createHash('md5').update(prefix + i).digest('hex');
  if (hash.slice(0, 5) === '00000') {
    console.log('Part 1: ', i);
    break;
  }
}

// 282749

for (let i = 1; i < 10000000; i++) {
  const hash = crypto.createHash('md5').update(prefix + i).digest('hex');
  if (hash.slice(0, 6) === '000000') {
    console.log('Part 2: ', i);
    break;
  }
}

// 9962624
