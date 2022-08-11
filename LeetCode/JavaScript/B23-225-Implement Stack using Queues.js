var MyStack = function () {
  this.q = new Array();
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
  this.q.push(x);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
  return this.q.pop();
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
  return this.q.slice(-1);
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
  return !this.q.length;
};

var obj = new MyStack();
obj.push(1);
obj.push(2);
console.log(obj.top());
console.log(obj.q);
obj.pop();
/*
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
