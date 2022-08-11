var MyQueue = function () {
  this.stack = new Array();
};

/**
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
  const temp = new Array();

  while (!!this.stack.length) {
    temp.push(this.stack.pop());
  }
  this.stack.push(x);
  while (!!temp.length) {
    this.stack.push(temp.pop());
  }
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function () {
  return this.stack.pop();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function () {
  return this.stack[this.stack.length - 1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
  return !this.stack.length;
};

// const obj = new MyQueue();
// obj.push(1);
// console.log(obj.stack);
// console.log("========");
// obj.push(2);
// console.log(obj.stack);
// console.log("========");
// obj.push(3);
// console.log(obj.stack);
// console.log("========");
// obj.push(4);
// console.log(obj.stack);
// console.log("========");
// console.log(obj.pop());
// console.log(obj.stack);
// console.log("========");
// obj.push(5);
// console.log(obj.stack);
// console.log("========");
// console.log(obj.pop());
// console.log(obj.stack);
// console.log("========");
// console.log(obj.pop());
// console.log(obj.stack);
// console.log("========");
// console.log(obj.pop());
// console.log(obj.stack);
// console.log("========");
// console.log(obj.pop());

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
