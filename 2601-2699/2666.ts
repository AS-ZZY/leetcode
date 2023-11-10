type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
  let v = false
	return function (...args) {
		if(!v) {
      v = true
      return fn(...args)
    }
    return
	};
}