var MyStack = function () {
  this.q1 = new Array();
  this.q2 = new Array();
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
  while (!!this.q2.length) {
    this.q1.push(this.q2.shift());
  }
  this.q1.push(x);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
  this.top();
  return this.q2.shift();
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
  if (!!this.q2.length) {
    return this.q2[0];
  }
  while (!!this.q1.length) {
    this.q2.push(this.q1.shift());
  }
  while (this.q2.length > 1) {
    this.q1.push(this.q2.shift());
  }
  return this.q2[0];
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
  return !this.q1.length && !this.q2.length;
};

var obj = new MyStack();
obj.push(1);
console.log("q1", obj.q1);
console.log("q2", obj.q2);
console.log("=======");
obj.push(2);
console.log("q1", obj.q1);
console.log("q2", obj.q2);
console.log("=======");

console.log(obj.top());
console.log("q1", obj.q1);
console.log("q2", obj.q2);
console.log("=======");

console.log(obj.pop());
console.log("q1", obj.q1);
console.log("q2", obj.q2);
console.log("=======");

// console.log(obj.top());
// console.log("q1", obj.q1);
// console.log("q2", obj.q2);
// console.log("=======");

/*
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
