/*

https://adventofcode.com/2019/day/12

*/

// const moonsTest = {
//   io: { x: -1, y: 0, z: 2, dx: 0, dy: 0, dz: 0 },
//   europa: { x: 2, y: -10, z: -7, dx: 0, dy: 0, dz: 0 },
//   ganymede: { x: 4, y: -8, z: 8, dx: 0, dy: 0, dz: 0 },
//   callisto: { x: 3, y: 5, z: -1, dx: 0, dy: 0, dz: 0 },
// };

const moons = {
  io: { x: 17, y: -12, z: 13, dx: 0, dy: 0, dz: 0 },
  europa: { x: 2, y: 1, z: 1, dx: 0, dy: 0, dz: 0 },
  ganymede: { x: -1, y: -17, z: 7, dx: 0, dy: 0, dz: 0 },
  callisto: { x: 12, y: -14, z: 18, dx: 0, dy: 0, dz: 0 },
};
const moonNames = Object.keys(moons);
const directions = ['x', 'y', 'z'];

const updateVelocity = (moon1, moon2) => {
  for (let i = 0; i < directions.length; i++) {
    let delta = 0;
    const dir = directions[i];
    if (moon1[dir] < moon2[dir]) {
      delta = 1;
    } else if (moon1[dir] > moon2[dir]) {
      delta = -1;
    }

    moon1['d' + dir] += delta;
    moon2['d' + dir] -= delta;
  }
};

const updatePosition = (moon) => {
  for (let i = 0; i < directions.length; i++) {
    const dir = directions[i];
    moon[dir] += moon['d' + dir];
  }
};

const timeStep = (moons) => {
  moonNames.forEach((name, index) => {
    for (let i = index + 1; i < moonNames.length; i++) {
      updateVelocity(moons[name], moons[moonNames[i]]);
    }
  });
  moonNames.forEach(name => updatePosition(moons[name]));
}

const calcEnergy = moon => {
  let pE = 0;
  let kE = 0;
  
  for (let i = 0; i < directions.length; i++) {
    const dir = directions[i];
    pE += Math.abs(moon[dir]);
    kE += Math.abs(moon['d' + dir]);
  }
  
  return pE * kE;
}

for (let i = 0; i < 1000; i++) {
  timeStep(moons);
}

const energy = moonNames.reduce((acc, name) => calcEnergy(moons[name]) + acc, 0);
console.log(energy);
// 8960

// const history = {};

// const serializePosition = (moons) => {
//   let serialization = '';
//   for (let i = 0; i < moonNames.length; i++) {
//     let pos = '';
//     let v = '';

//     for (let j = 0; j < directions.length; j++) {
//       const dir = directions[j];
//       pos += moons[moonNames[i]][dir].toString() + '.';
//       v += moons[moonNames[i]]['d' + dir].toString() + '.';
//     }
//     serialization += pos + v;
//   }
//   return serialization;
// }

// let steps = 0;

// while (true) {
//   const curr = serializePosition(moons);
//   if (history.hasOwnProperty(curr)) break;
//   history[curr] = true;
//   steps++;
//   timeStep(moons);
//   if (steps % 100000 === 0) console.log(steps)
// }

// console.log(steps)
