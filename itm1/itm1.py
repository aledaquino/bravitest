def isValid(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True  
    return False
  
def isNested(S):
    stack = []
      
    for symbol in S:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if not isValid(last, symbol):
                return False
      
    if len(stack) != 0:
        return False
              
    return True
 
 
def main():
    print('Informe a quantidade de vezes que deseja realizar a validação:')
    N = int(input())
 
    for _ in range(N):
        print('Informe a sequencia de parenteses, colchetes ou chaves que deseja validar sem espaço entre eles:')
        s = input()
        if isNested(s):
            print('Válido')
        else:
            print('Inválido')
 
 
if __name__ == '__main__':
    main()