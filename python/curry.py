def curry(fn):
    arg_count = fn.__code__.co_argcount
    collected = []

    def collector(arg):
        collected.append(arg)
        if len(collected) == arg_count:
            result = fn(*collected)
            collected.clear()
            return result
        else:
            return collector
    return collector