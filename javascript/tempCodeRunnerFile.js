let myName = "Aasasdfffassdsdek";

// let obj = {};

// for (let i = 0; i < myName.length; i++) {
//   let char = myName[i];

//   if (obj[char]) {
//     obj[char] += 1;
//   } else {
//     obj[char] = 1;
//   }
// }

// console.log(obj);

// let frequency = myName.split("").reduce((acc, char) => {
//   acc[char] = (acc[char] || 0) + 1;
//   return acc;
// }, {});

// console.log(frequency);

let frequency = {};

// [...myName].forEach((char) => (frequency[char] = (frequency[char] || 0) + 1));
[...myName].forEach((char) => {
  console.log(char);
});

// console.log(frequency);
