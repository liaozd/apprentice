function test() {
  console.log(arguments);
  console.log(arguments instanceof Array);
  console.log(arguments instanceof Object);
  console.log("break");
  var a = Array.prototype.slice.call(arguments,1);
  console.log(a);
  console.log(a instanceof Array);
  console.log(a instanceof Object);
}

test(1,2,3,4);
