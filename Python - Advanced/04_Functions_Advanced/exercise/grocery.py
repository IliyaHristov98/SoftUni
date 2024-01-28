def grocery_store(**products):
    result = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{p}: {q}" for p, q in result)
