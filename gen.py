def gen1(tokens):
    """
    Display list of tokens of one line
    """
    s = ""
    s += f"""
### Як це надрукувати?
<section>
```
{''.join(tokens)}
```
</section>
    """
    resultlen = 0
    for token in tokens:
        s += f"""
<section>
```
{' '*resultlen}{token}
```
</section>
        """
        resultlen += len(token)
    print(s)

if 1:
    gen1("print|(|\"|Game Over|\"|)".split('|'))
