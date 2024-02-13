def is_correct_brackets(text):
    while '()' in text or '[]' in text or '{}' in text or '<>' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
        text = text.replace('<>', '')

    return not text

def check(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                return False
    return (not stack)

print('1 ', is_correct_brackets('{{[()]}}'), check('{{[()]}}'))
print('2 ', is_correct_brackets('}{}'), check('}{}'))
print('3 ', is_correct_brackets('{{[(])]}}'), check('{{[(])]}}'))
print('4 ', is_correct_brackets('[[{())}]'), check('[[{())}]'))
print('5 ', is_correct_brackets(')('), check(')('))
print('6 ', is_correct_brackets('(()(()'), check('(()(()'))
print('7 ', is_correct_brackets('(()(()()))'), check('(()(()()))'))
print('8 ', is_correct_brackets('())()(()())(()'), check('())()(()())(()'))
print('9 ', is_correct_brackets('([{}])'), check('([{}])'))
print('10', is_correct_brackets('[{'), check('[{'))