'''
DECRYPTION PROGRAM
------------------
An encryption program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a Decryption program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Secret Message: Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*
'''

message = "Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
for x in range(-20, 21):
    decode = ""
    for letter in message:
        e = ord(letter)
        e = e+x
        new_letter = chr(e)
        decode = decode+new_letter
    print(decode)

