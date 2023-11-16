class TimeLimitedCache {
  private cache: Record<number, { exTime: number, value: number }>

  constructor() {
    this.cache = {}
  }

  set(key: number, value: number, duration: number): boolean {
    let re
    if (!this.cache[key]) {
      re = false
    } else if(this._isEx(this.cache[key].exTime)) {
      re = true
    }
    this.cache[key] = {
      exTime: new Date().getTime() + duration,
      value
    }
    return re
  }

  get(key: number): number {
    if(!this.cache[key]) {
      return -1
    }
    if(this._isEx(this.cache[key])) {
      return -1
    }
    return this.cache[key].value
  }

  count(): number {
    return Object.values(this.cache).filter((i) => !this._isEx(i)).length
  }

  _isEx(v) {
    return v.exTime <= new Date().getTime()
  }
}