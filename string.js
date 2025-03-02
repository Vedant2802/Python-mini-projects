// let myName = "Aasasdfffassdsdek";

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

// let frequency = {};

// // [...myName].forEach((char) => (frequency[char] = (frequency[char] || 0) + 1));
// [...myName].forEach((char) => {
//   console.log(char);
//   if (frequency[char] == undefined) {
//     frequency[char] = 1;
//   } else {
//     frequency[char] += 1;
//   }
// });
// console.log(frequency);

// console.log(frequency);

let arr = ["Akshat", "Aksaht", "Akshat", "Vedant", "Vrrrrr"];

// return no unique item

let frequency = {};

for (let element of arr) {
  //   console.log(element);
  if (frequency[element]) {
    console.log(element);
    break;
  }
  frequency[element] = true;
}
