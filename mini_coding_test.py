def callnum(digits):
    callnumbers={'1':' ','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
    output = [key for key in callnumbers[digits[0]]]
    print(output)
    for index in range(1, len(digits)):
        number = digits[index]
        if number in [0,1] :
            break
        options = []
        for option in output:
            options += [option+key for key in callnumbers[number]]
        print(options)
        output = options
    return output

callnum(['2','3'])