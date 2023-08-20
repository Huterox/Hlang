"""
Hlang is a Sample Language shell
Just a sample example for learning by Huterox
"""
import hlang_basic

while True:

    input_text = input("Hlang交互终端->>>")
    result, error = hlang_basic.run('<标准输入>', input_text)

    if error: print(error.as_string())
    else: print(result)