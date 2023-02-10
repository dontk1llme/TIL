T = int(input())
for test_case in range(1, T + 1):
    st = input()
    st1 = '.'+'.#..'*len(st)
    st2 = '.'+'#.#.'*len(st)
    ast = '#'+''.join(['.'+ch+'.#' for ch in st])
    print(st1, st2, ast, st2, st1, sep='\n')