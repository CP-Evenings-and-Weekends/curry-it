const curry = require("./curry");

const add3 = (a, b, c) => a + b + c;
const mul2 = (a, b) => a * b;
const add4 = (a, b, c, d) => a + b + c + d;

const curriedAdd = curry(add3);
console.log(curriedAdd(1)(2)(3) === 6);
console.log(curriedAdd(10)(20)(30) === 60);
console.log(curriedAdd(-5)(5)(0) === 0);

const curriedMul = curry(mul2);
console.log(curriedMul(4)(5) === 20);
console.log(curriedMul(0)(100) === 0);

const curriedAdd4 = curry(add4);
console.log(curriedAdd4(1)(2)(3)(4) === 10);
