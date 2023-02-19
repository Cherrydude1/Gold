import Gold

while True:
    text = input('Gold >')
    result, error = Gold.run(text)

    if error: print(error.string())
    else: print(result)