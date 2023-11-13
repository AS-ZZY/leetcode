type F = (x: number) => number;

function compose(functions: F[]): F {
	return function(x) {
    return functions.reverse().reduce((v, fn) => fn(v), x)
  }
};
