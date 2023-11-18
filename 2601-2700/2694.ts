type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {

  private subscribeFn: Record<string, Callback[]> = {}

	subscribe(eventName: string, callback: Callback): Subscription {
    if (this.subscribeFn[eventName]) {
      this.subscribeFn[eventName].push(callback)
    } else {
      this.subscribeFn[eventName] = [callback]
    }
		return {
			unsubscribe: () => {
        this.subscribeFn[eventName] = this.subscribeFn[eventName].filter((i) => i !== callback)
			}
    };
	}

	emit(eventName: string, args: any[] = []): any[] {
    return (this.subscribeFn[eventName] || []).map((i) => i(...args))
	}
}