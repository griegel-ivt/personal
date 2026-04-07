print("Welcome to Caveman Encoder and Decoder v0.1!")
operation = input("Please respond with a singular letter (e,d,l) representing your chosen operation.\nWould you like to encode (e), decode (d), or learn more (l)?")
v_asc,v_bin,v_chunks,v_bin_chunks,v_char_chunks,encoded_chunks,decoded_chunks = [],[],[],[],[],[],[]
if operation == "e":
    data = str(input("Message to be encoded in OogaBooga:\n"))
    for data_char in data:
        v_asc.append(ord(data_char))
    for asc_char in v_asc:
        v_bin_temp = str(bin(asc_char)[2:])
        if len(v_bin_temp) == 6:
            v_bin_temp = ("00"+v_bin_temp)
        else:
            v_bin_temp = ("0"+v_bin_temp)
        v_bin.append(v_bin_temp)
    v_bin_stream = "".join(v_bin)
    v_bin_chunks_len = 28
    v_bin_chunks = [v_bin_stream[v_bin_chunks_temp:v_bin_chunks_temp+v_bin_chunks_len] for v_bin_chunks_temp in range(0, len(v_bin_stream), v_bin_chunks_len)]
    if len(v_bin_chunks[-1]) <=27:
        v_bin_chunks_char_amt_temp = 28-len(v_bin_chunks[-1])
        for v_bin_chunks_char_temp in range(v_bin_chunks_char_amt_temp):
            v_bin_chunks[-1] = (v_bin_chunks[-1]+"0")
    v_bin_chunk_number = -1
    v_fixed_bin_stream = "".join(v_bin_chunks)
    v_chunks_len = 7
    v_chunks = [v_fixed_bin_stream[v_chunks_temp:v_chunks_temp+v_chunks_len] for v_chunks_temp in range(0, len(v_fixed_bin_stream), v_chunks_len)]
    v_chunk_number = -1
    for v_chunks_amt_temp in v_chunks:
        v_chunk_number = v_chunk_number + 1
        if v_chunks[v_chunk_number] == "0000000":
            encoded_chunks.append("=")
        elif v_chunks[v_chunk_number] == "0000001":
            encoded_chunks.append("A")
        elif v_chunks[v_chunk_number] == "0000010":
            encoded_chunks.append("!")
        elif v_chunks[v_chunk_number] == "0000011":
            encoded_chunks.append("a")
        elif v_chunks[v_chunk_number] == "0000100":
            encoded_chunks.append("@")
        elif v_chunks[v_chunk_number] == "0000101":
            encoded_chunks.append("B")
        elif v_chunks[v_chunk_number] == "0000110":
            encoded_chunks.append("#")
        elif v_chunks[v_chunk_number] == "0000111":
            encoded_chunks.append("b")
        elif v_chunks[v_chunk_number] == "0001000":
            encoded_chunks.append("$")
        elif v_chunks[v_chunk_number] == "0001001":
            encoded_chunks.append("C")
        elif v_chunks[v_chunk_number] == "0001010":
            encoded_chunks.append("%")
        elif v_chunks[v_chunk_number] == "0001011":
            encoded_chunks.append("c")
        elif v_chunks[v_chunk_number] == "0001100":
            encoded_chunks.append("^")
        elif v_chunks[v_chunk_number] == "0001101":
            encoded_chunks.append("D")
        elif v_chunks[v_chunk_number] == "0001110":
            encoded_chunks.append("&")
        elif v_chunks[v_chunk_number] == "0001111":
            encoded_chunks.append("d")
        elif v_chunks[v_chunk_number] == "0010000":
            encoded_chunks.append("*")
        elif v_chunks[v_chunk_number] == "0010001":
            encoded_chunks.append("E")
        elif v_chunks[v_chunk_number] == "0010010":
            encoded_chunks.append("(")
        elif v_chunks[v_chunk_number] == "0010011":
            encoded_chunks.append("e")
        elif v_chunks[v_chunk_number] == "0010100":
            encoded_chunks.append(")")
        elif v_chunks[v_chunk_number] == "0010101":
            encoded_chunks.append("F")
        elif v_chunks[v_chunk_number] == "0010110":
            encoded_chunks.append("_")
        elif v_chunks[v_chunk_number] == "0010111":
            encoded_chunks.append("f")
        elif v_chunks[v_chunk_number] == "0011000":
            encoded_chunks.append("[")
        elif v_chunks[v_chunk_number] == "0011001":
            encoded_chunks.append("G")
        elif v_chunks[v_chunk_number] == "0011010":
            encoded_chunks.append("]")
        elif v_chunks[v_chunk_number] == "0011011":
            encoded_chunks.append("g")
        elif v_chunks[v_chunk_number] == "0011100":
            encoded_chunks.append("|")
        elif v_chunks[v_chunk_number] == "0011101":
            encoded_chunks.append("H")
        elif v_chunks[v_chunk_number] == "0011110":
            encoded_chunks.append(":")
        elif v_chunks[v_chunk_number] == "0011111":
            encoded_chunks.append("h")
        elif v_chunks[v_chunk_number] == "0100000":
            encoded_chunks.append(";")
        elif v_chunks[v_chunk_number] == "0100001":
            encoded_chunks.append("I")
        elif v_chunks[v_chunk_number] == "0100010":
            encoded_chunks.append("<")
        elif v_chunks[v_chunk_number] == "0100011":
            encoded_chunks.append("i")
        elif v_chunks[v_chunk_number] == "0100100":
            encoded_chunks.append(">")
        elif v_chunks[v_chunk_number] == "0100101":
            encoded_chunks.append("J")
        elif v_chunks[v_chunk_number] == "0100110":
            encoded_chunks.append("?")
        elif v_chunks[v_chunk_number] == "0100111":
            encoded_chunks.append("j")
        elif v_chunks[v_chunk_number] == "0101000":
            encoded_chunks.append("~")
        elif v_chunks[v_chunk_number] == "0101001":
            encoded_chunks.append("K")
        elif v_chunks[v_chunk_number] == "0101010":
            encoded_chunks.append("±")
        elif v_chunks[v_chunk_number] == "0101011":
            encoded_chunks.append("k")
        elif v_chunks[v_chunk_number] == "0101100":
            encoded_chunks.append("÷")
        elif v_chunks[v_chunk_number] == "0101101":
            encoded_chunks.append("L")
        elif v_chunks[v_chunk_number] == "0101110":
            encoded_chunks.append("¦")
        elif v_chunks[v_chunk_number] == "0101111":
            encoded_chunks.append("l")
        elif v_chunks[v_chunk_number] == "0110000":
            encoded_chunks.append("©")
        elif v_chunks[v_chunk_number] == "0110001":
            encoded_chunks.append("M")
        elif v_chunks[v_chunk_number] == "0110010":
            encoded_chunks.append("®")
        elif v_chunks[v_chunk_number] == "0110011":
            encoded_chunks.append("m")
        elif v_chunks[v_chunk_number] == "0110100":
            encoded_chunks.append("°")
        elif v_chunks[v_chunk_number] == "0110101":
            encoded_chunks.append("N")
        elif v_chunks[v_chunk_number] == "0110110":
            encoded_chunks.append("֍")
        elif v_chunks[v_chunk_number] == "0110111":
            encoded_chunks.append("n")
        elif v_chunks[v_chunk_number] == "0111000":
            encoded_chunks.append("֎")
        elif v_chunks[v_chunk_number] == "0111001":
            encoded_chunks.append("O")
        elif v_chunks[v_chunk_number] == "0111010":
            encoded_chunks.append("℗")
        elif v_chunks[v_chunk_number] == "0111011":
            encoded_chunks.append("o")
        elif v_chunks[v_chunk_number] == "0111100":
            encoded_chunks.append("℠")
        elif v_chunks[v_chunk_number] == "0111101":
            encoded_chunks.append("P")
        elif v_chunks[v_chunk_number] == "0111110":
            encoded_chunks.append("҂")
        elif v_chunks[v_chunk_number] == "0111111":
            encoded_chunks.append("p")
        elif v_chunks[v_chunk_number] == "1000000":
            encoded_chunks.append("™")
        elif v_chunks[v_chunk_number] == "1000001":
            encoded_chunks.append("Q")
        elif v_chunks[v_chunk_number] == "1000010":
            encoded_chunks.append("℻")
        elif v_chunks[v_chunk_number] == "1000011":
            encoded_chunks.append("q")
        elif v_chunks[v_chunk_number] == "1000100":
            encoded_chunks.append("↖")
        elif v_chunks[v_chunk_number] == "1000101":
            encoded_chunks.append("R")
        elif v_chunks[v_chunk_number] == "1000110":
            encoded_chunks.append("↗")
        elif v_chunks[v_chunk_number] == "1000111":
            encoded_chunks.append("r")
        elif v_chunks[v_chunk_number] == "1001000":
            encoded_chunks.append("↘")
        elif v_chunks[v_chunk_number] == "1001001":
            encoded_chunks.append("S")
        elif v_chunks[v_chunk_number] == "1001010":
            encoded_chunks.append("↙")
        elif v_chunks[v_chunk_number] == "1001011":
            encoded_chunks.append("s")
        elif v_chunks[v_chunk_number] == "1001100":
            encoded_chunks.append("⌢")
        elif v_chunks[v_chunk_number] == "1001101":
            encoded_chunks.append("T")
        elif v_chunks[v_chunk_number] == "1001110":
            encoded_chunks.append("⌣")
        elif v_chunks[v_chunk_number] == "1001111":
            encoded_chunks.append("t")
        elif v_chunks[v_chunk_number] == "1010000":
            encoded_chunks.append("⌜")
        elif v_chunks[v_chunk_number] == "1010001":
            encoded_chunks.append("U")
        elif v_chunks[v_chunk_number] == "1010010":
            encoded_chunks.append("⌝")
        elif v_chunks[v_chunk_number] == "1010011":
            encoded_chunks.append("u")
        elif v_chunks[v_chunk_number] == "1010100":
            encoded_chunks.append("⌞")
        elif v_chunks[v_chunk_number] == "1010101":
            encoded_chunks.append("V")
        elif v_chunks[v_chunk_number] == "1010110":
            encoded_chunks.append("⌟")
        elif v_chunks[v_chunk_number] == "1010111":
            encoded_chunks.append("v")
        elif v_chunks[v_chunk_number] == "1011000":
            encoded_chunks.append("░")
        elif v_chunks[v_chunk_number] == "1011001":
            encoded_chunks.append("W")
        elif v_chunks[v_chunk_number] == "1011010":
            encoded_chunks.append("▒")
        elif v_chunks[v_chunk_number] == "1011011":
            encoded_chunks.append("w")
        elif v_chunks[v_chunk_number] == "1011100":
            encoded_chunks.append("▓")
        elif v_chunks[v_chunk_number] == "1011101":
            encoded_chunks.append("X")
        elif v_chunks[v_chunk_number] == "1011110":
            encoded_chunks.append("▝")
        elif v_chunks[v_chunk_number] == "1011111":
            encoded_chunks.append("x")
        elif v_chunks[v_chunk_number] == "1100000":
            encoded_chunks.append("▘")
        elif v_chunks[v_chunk_number] == "1100001":
            encoded_chunks.append("Y")
        elif v_chunks[v_chunk_number] == "1100010":
            encoded_chunks.append("▖")
        elif v_chunks[v_chunk_number] == "1100011":
            encoded_chunks.append("y")
        elif v_chunks[v_chunk_number] == "1100100":
            encoded_chunks.append("▗")
        elif v_chunks[v_chunk_number] == "1100101":
            encoded_chunks.append("Z")
        elif v_chunks[v_chunk_number] == "1100110":
            encoded_chunks.append("◉")
        elif v_chunks[v_chunk_number] == "1100111":
            encoded_chunks.append("z")
        elif v_chunks[v_chunk_number] == "1101000":
            encoded_chunks.append("■")
        elif v_chunks[v_chunk_number] == "1101001":
            encoded_chunks.append("1")
        elif v_chunks[v_chunk_number] == "1101010":
            encoded_chunks.append("□")
        elif v_chunks[v_chunk_number] == "1101011":
            encoded_chunks.append("2")
        elif v_chunks[v_chunk_number] == "1101100":
            encoded_chunks.append("▪")
        elif v_chunks[v_chunk_number] == "1101101":
            encoded_chunks.append("3")
        elif v_chunks[v_chunk_number] == "1101110":
            encoded_chunks.append("▫")
        elif v_chunks[v_chunk_number] == "1101111":
            encoded_chunks.append("4")
        elif v_chunks[v_chunk_number] == "1110000":
            encoded_chunks.append("◯")
        elif v_chunks[v_chunk_number] == "1110001":
            encoded_chunks.append("5")
        elif v_chunks[v_chunk_number] == "1110010":
            encoded_chunks.append("§")
        elif v_chunks[v_chunk_number] == "1110011":
            encoded_chunks.append("6")
        elif v_chunks[v_chunk_number] == "1110100":
            encoded_chunks.append("¡")
        elif v_chunks[v_chunk_number] == "1110101":
            encoded_chunks.append("7")
        elif v_chunks[v_chunk_number] == "1110110":
            encoded_chunks.append("¿")
        elif v_chunks[v_chunk_number] == "1110111":
            encoded_chunks.append("8")
        elif v_chunks[v_chunk_number] == "1111000":
            encoded_chunks.append("¢")
        elif v_chunks[v_chunk_number] == "1111001":
            encoded_chunks.append("9")
        elif v_chunks[v_chunk_number] == "1111010":
            encoded_chunks.append("£")
        elif v_chunks[v_chunk_number] == "1111011":
            encoded_chunks.append("0")
        elif v_chunks[v_chunk_number] == "1111100":
            encoded_chunks.append("‽")
        elif v_chunks[v_chunk_number] == "1111101":
            encoded_chunks.append("+")
        elif v_chunks[v_chunk_number] == "1111110":
            encoded_chunks.append("-")
        elif v_chunks[v_chunk_number] == "1111111":
            encoded_chunks.append("/")   
    encoded_message = "".join(encoded_chunks)
    print("----------------------------------------------------------------------------------------------------\nYour message encoded in OogaBooga:\n"+(encoded_message)+"\n\n----------------------------------------------------------------------------------------------------\n")
    print("\nTo copy the encoded message, drag your cursor from one side of the message to the other, and while still holding down your left click, use CTRL + C to copy, after which you may release left click.")
elif operation == "d":
    data = str(input("Message to be decoded from OogaBooga:\n"))
    v_encoded_chunks_len = 1
    encoded_chunks = [data[v_encoded_chunks_temp:v_encoded_chunks_temp+v_encoded_chunks_len] for v_encoded_chunks_temp in range(0, len(data), v_encoded_chunks_len)]
    v_encoded_chunk_number = -1
    for v_encoded_chunks_amt_temp in encoded_chunks:
        v_encoded_chunk_number = v_encoded_chunk_number + 1
        if encoded_chunks[v_encoded_chunk_number] == "=":
            v_chunks.append("0000000")
        elif encoded_chunks[v_encoded_chunk_number] == "A":
            v_chunks.append("0000001")
        elif encoded_chunks[v_encoded_chunk_number] == "!":
            v_chunks.append("0000010")
        elif encoded_chunks[v_encoded_chunk_number] == "a":
            v_chunks.append("0000011")
        elif encoded_chunks[v_encoded_chunk_number] == "@":
            v_chunks.append("0000100")
        elif encoded_chunks[v_encoded_chunk_number] == "B":
            v_chunks.append("0000101")
        elif encoded_chunks[v_encoded_chunk_number] == "#":
            v_chunks.append("0000110")
        elif encoded_chunks[v_encoded_chunk_number] == "b":
            v_chunks.append("0000111")
        elif encoded_chunks[v_encoded_chunk_number] == "$":
            v_chunks.append("0001000")
        elif encoded_chunks[v_encoded_chunk_number] == "C":
            v_chunks.append("0001001")
        elif encoded_chunks[v_encoded_chunk_number] == "%":
            v_chunks.append("0001010")
        elif encoded_chunks[v_encoded_chunk_number] == "c":
            v_chunks.append("0001011")
        elif encoded_chunks[v_encoded_chunk_number] == "^":
            v_chunks.append("0001100")
        elif encoded_chunks[v_encoded_chunk_number] == "D":
            v_chunks.append("0001101")
        elif encoded_chunks[v_encoded_chunk_number] == "&":
            v_chunks.append("0001110")
        elif encoded_chunks[v_encoded_chunk_number] == "d":
            v_chunks.append("0001111")
        elif encoded_chunks[v_encoded_chunk_number] == "*":
            v_chunks.append("0010000")
        elif encoded_chunks[v_encoded_chunk_number] == "E":
            v_chunks.append("0010001")
        elif encoded_chunks[v_encoded_chunk_number] == "(":
            v_chunks.append("0010010")
        elif encoded_chunks[v_encoded_chunk_number] == "e":
            v_chunks.append("0010011")
        elif encoded_chunks[v_encoded_chunk_number] == ")":
            v_chunks.append("0010100")
        elif encoded_chunks[v_encoded_chunk_number] == "F":
            v_chunks.append("0010101")
        elif encoded_chunks[v_encoded_chunk_number] == "_":
            v_chunks.append("0010110")
        elif encoded_chunks[v_encoded_chunk_number] == "f":
            v_chunks.append("0010111")
        elif encoded_chunks[v_encoded_chunk_number] == "[":
            v_chunks.append("0011000")
        elif encoded_chunks[v_encoded_chunk_number] == "G":
            v_chunks.append("0011001")
        elif encoded_chunks[v_encoded_chunk_number] == "]":
            v_chunks.append("0011010")
        elif encoded_chunks[v_encoded_chunk_number] == "g":
            v_chunks.append("0011011")
        elif encoded_chunks[v_encoded_chunk_number] == "|":
            v_chunks.append("0011100")
        elif encoded_chunks[v_encoded_chunk_number] == "H":
            v_chunks.append("0011101")
        elif encoded_chunks[v_encoded_chunk_number] == ":":
            v_chunks.append("0011110")
        elif encoded_chunks[v_encoded_chunk_number] == "h":
            v_chunks.append("0011111")
        elif encoded_chunks[v_encoded_chunk_number] == ";":
            v_chunks.append("0100000")
        elif encoded_chunks[v_encoded_chunk_number] == "I":
            v_chunks.append("0100001")
        elif encoded_chunks[v_encoded_chunk_number] == "<":
            v_chunks.append("0100010")
        elif encoded_chunks[v_encoded_chunk_number] == "i":
            v_chunks.append("0100011")
        elif encoded_chunks[v_encoded_chunk_number] == ">":
            v_chunks.append("0100100")
        elif encoded_chunks[v_encoded_chunk_number] == "J":
            v_chunks.append("0100101")
        elif encoded_chunks[v_encoded_chunk_number] == "?":
            v_chunks.append("0100110")
        elif encoded_chunks[v_encoded_chunk_number] == "j":
            v_chunks.append("0100111")
        elif encoded_chunks[v_encoded_chunk_number] == "~":
            v_chunks.append("0101000")
        elif encoded_chunks[v_encoded_chunk_number] == "K":
            v_chunks.append("0101001")
        elif encoded_chunks[v_encoded_chunk_number] == "±":
            v_chunks.append("0101010")
        elif encoded_chunks[v_encoded_chunk_number] == "k":
            v_chunks.append("0101011")
        elif encoded_chunks[v_encoded_chunk_number] == "÷":
            v_chunks.append("0101100")
        elif encoded_chunks[v_encoded_chunk_number] == "L":
            v_chunks.append("0101101")
        elif encoded_chunks[v_encoded_chunk_number] == "¦":
            v_chunks.append("0101110")
        elif encoded_chunks[v_encoded_chunk_number] == "l":
            v_chunks.append("0101111")
        elif encoded_chunks[v_encoded_chunk_number] == "©":
            v_chunks.append("0110000")
        elif encoded_chunks[v_encoded_chunk_number] == "M":
            v_chunks.append("0110001")
        elif encoded_chunks[v_encoded_chunk_number] == "®":
            v_chunks.append("0110010")
        elif encoded_chunks[v_encoded_chunk_number] == "m":
            v_chunks.append("0110011")
        elif encoded_chunks[v_encoded_chunk_number] == "°":
            v_chunks.append("0110100")
        elif encoded_chunks[v_encoded_chunk_number] == "N":
            v_chunks.append("0110101")
        elif encoded_chunks[v_encoded_chunk_number] == "֍":
            v_chunks.append("0110110")
        elif encoded_chunks[v_encoded_chunk_number] == "n":
            v_chunks.append("0110111")
        elif encoded_chunks[v_encoded_chunk_number] == "֎":
            v_chunks.append("0111000")
        elif encoded_chunks[v_encoded_chunk_number] == "O":
            v_chunks.append("0111001")
        elif encoded_chunks[v_encoded_chunk_number] == "℗":
            v_chunks.append("0111010")
        elif encoded_chunks[v_encoded_chunk_number] == "o":
            v_chunks.append("0111011")
        elif encoded_chunks[v_encoded_chunk_number] == "℠":
            v_chunks.append("0111100")
        elif encoded_chunks[v_encoded_chunk_number] == "P":
            v_chunks.append("0111101")
        elif encoded_chunks[v_encoded_chunk_number] == "҂":
            v_chunks.append("0111110")
        elif encoded_chunks[v_encoded_chunk_number] == "p":
            v_chunks.append("0111111")
        elif encoded_chunks[v_encoded_chunk_number] == "™":
            v_chunks.append("1000000")
        elif encoded_chunks[v_encoded_chunk_number] == "Q":
            v_chunks.append("1000001")
        elif encoded_chunks[v_encoded_chunk_number] == "℻":
            v_chunks.append("1000010")
        elif encoded_chunks[v_encoded_chunk_number] == "q":
            v_chunks.append("1000011")
        elif encoded_chunks[v_encoded_chunk_number] == "↖":
            v_chunks.append("1000100")
        elif encoded_chunks[v_encoded_chunk_number] == "R":
            v_chunks.append("1000101")
        elif encoded_chunks[v_encoded_chunk_number] == "↗":
            v_chunks.append("1000110")
        elif encoded_chunks[v_encoded_chunk_number] == "r":
            v_chunks.append("1000111")
        elif encoded_chunks[v_encoded_chunk_number] == "↘":
            v_chunks.append("1001000")
        elif encoded_chunks[v_encoded_chunk_number] == "S":
            v_chunks.append("1001001")
        elif encoded_chunks[v_encoded_chunk_number] == "↙":
            v_chunks.append("1001010")
        elif encoded_chunks[v_encoded_chunk_number] == "s":
            v_chunks.append("1001011")
        elif encoded_chunks[v_encoded_chunk_number] == "⌢":
            v_chunks.append("1001100")
        elif encoded_chunks[v_encoded_chunk_number] == "T":
            v_chunks.append("1001101")
        elif encoded_chunks[v_encoded_chunk_number] == "⌣":
            v_chunks.append("1001110")
        elif encoded_chunks[v_encoded_chunk_number] == "t":
            v_chunks.append("1001111")
        elif encoded_chunks[v_encoded_chunk_number] == "⌜":
            v_chunks.append("1010000")
        elif encoded_chunks[v_encoded_chunk_number] == "U":
            v_chunks.append("1010001")
        elif encoded_chunks[v_encoded_chunk_number] == "⌝":
            v_chunks.append("1010010")
        elif encoded_chunks[v_encoded_chunk_number] == "u":
            v_chunks.append("1010011")
        elif encoded_chunks[v_encoded_chunk_number] == "⌞":
            v_chunks.append("1010100")
        elif encoded_chunks[v_encoded_chunk_number] == "V":
            v_chunks.append("1010101")
        elif encoded_chunks[v_encoded_chunk_number] == "⌟":
            v_chunks.append("1010110")
        elif encoded_chunks[v_encoded_chunk_number] == "v":
            v_chunks.append("1010111")
        elif encoded_chunks[v_encoded_chunk_number] == "░":
            v_chunks.append("1011000")
        elif encoded_chunks[v_encoded_chunk_number] == "W":
            v_chunks.append("1011001")
        elif encoded_chunks[v_encoded_chunk_number] == "▒":
            v_chunks.append("1011010")
        elif encoded_chunks[v_encoded_chunk_number] == "w":
            v_chunks.append("1011011")
        elif encoded_chunks[v_encoded_chunk_number] == "▓":
            v_chunks.append("1011100")
        elif encoded_chunks[v_encoded_chunk_number] == "X":
            v_chunks.append("1011101")
        elif encoded_chunks[v_encoded_chunk_number] == "▝":
            v_chunks.append("1011110")
        elif encoded_chunks[v_encoded_chunk_number] == "x":
            v_chunks.append("1011111")
        elif encoded_chunks[v_encoded_chunk_number] == "▘":
            v_chunks.append("1100000")
        elif encoded_chunks[v_encoded_chunk_number] == "Y":
            v_chunks.append("1100001")
        elif encoded_chunks[v_encoded_chunk_number] == "▖":
            v_chunks.append("1100010")
        elif encoded_chunks[v_encoded_chunk_number] == "y":
            v_chunks.append("1100011")
        elif encoded_chunks[v_encoded_chunk_number] == "▗":
            v_chunks.append("1100100")
        elif encoded_chunks[v_encoded_chunk_number] == "Z":
            v_chunks.append("1100101")
        elif encoded_chunks[v_encoded_chunk_number] == "◉":
            v_chunks.append("1100110")
        elif encoded_chunks[v_encoded_chunk_number] == "z":
            v_chunks.append("1100111")
        elif encoded_chunks[v_encoded_chunk_number] == "■":
            v_chunks.append("1101000")
        elif encoded_chunks[v_encoded_chunk_number] == "1":
            v_chunks.append("1101001")
        elif encoded_chunks[v_encoded_chunk_number] == "□":
            v_chunks.append("1101010")
        elif encoded_chunks[v_encoded_chunk_number] == "2":
            v_chunks.append("1101011")
        elif encoded_chunks[v_encoded_chunk_number] == "▪":
            v_chunks.append("1101100")
        elif encoded_chunks[v_encoded_chunk_number] == "3":
            v_chunks.append("1101101")
        elif encoded_chunks[v_encoded_chunk_number] == "▫":
            v_chunks.append("1101110")
        elif encoded_chunks[v_encoded_chunk_number] == "4":
            v_chunks.append("1101111")
        elif encoded_chunks[v_encoded_chunk_number] == "◯":
            v_chunks.append("1110000")
        elif encoded_chunks[v_encoded_chunk_number] == "5":
            v_chunks.append("1110001")
        elif encoded_chunks[v_encoded_chunk_number] == "§":
            v_chunks.append("1110010")
        elif encoded_chunks[v_encoded_chunk_number] == "6":
            v_chunks.append("1110011")
        elif encoded_chunks[v_encoded_chunk_number] == "¡":
            v_chunks.append("1110100")
        elif encoded_chunks[v_encoded_chunk_number] == "7":
            v_chunks.append("1110101")
        elif encoded_chunks[v_encoded_chunk_number] == "¿":
            v_chunks.append("1110110")
        elif encoded_chunks[v_encoded_chunk_number] == "8":
            v_chunks.append("1110111")
        elif encoded_chunks[v_encoded_chunk_number] == "¢":
            v_chunks.append("1111000")
        elif encoded_chunks[v_encoded_chunk_number] == "9":
            v_chunks.append("1111001")
        elif encoded_chunks[v_encoded_chunk_number] == "£":
            v_chunks.append("1111010")
        elif encoded_chunks[v_encoded_chunk_number] == "0":
            v_chunks.append("1111011")
        elif encoded_chunks[v_encoded_chunk_number] == "‽":
            v_chunks.append("1111100")
        elif encoded_chunks[v_encoded_chunk_number] == "+":
            v_chunks.append("1111101")
        elif encoded_chunks[v_encoded_chunk_number] == "-":
            v_chunks.append("1111110")
        elif encoded_chunks[v_encoded_chunk_number] == "/":
            v_chunks.append("1111111")
    v_bin_stream = "".join(v_chunks)
    while (len(v_bin_stream) % 8) != 0:
        v_bin_stream = v_bin_stream[:-1]
    v_bin_chunks_len = 28
    v_bin_chunks = [v_bin_stream[v_bin_chunks_temp:v_bin_chunks_temp+v_bin_chunks_len] for v_bin_chunks_temp in range(0, len(v_bin_stream), v_bin_chunks_len)]
    v_fixed_bin_stream = "".join(v_bin_chunks)
    v_fixed_bin_chunks_len = 8
    v_fixed_bin_chunks = [v_fixed_bin_stream[v_fixed_bin_chunks_temp:v_fixed_bin_chunks_temp+v_fixed_bin_chunks_len] for v_fixed_bin_chunks_temp in range(0, len(v_fixed_bin_stream), v_fixed_bin_chunks_len)]
    for v_char_temp in v_fixed_bin_chunks:
        v_char_chunks.append(str(chr(int(v_char_temp,2))))
    decoded_message = "".join(v_char_chunks)
    print("----------------------------------------------------------------------------------------------------\nYour message decoded from OogaBooga:\n"+(decoded_message)+"\n\n----------------------------------------------------------------------------------------------------\n")
    print("\nTo copy the decoded message, drag your cursor from one side of the message to the other, and while still holding down your left click, use CTRL + C to copy, after which you may release left click.")
elif operation == "l":
    print("\nAbout Caveman Encoder and Decoder v0.1:\nCaveman Encoder and Decoder is a python script used to encrypt and decrypt text in an exotic language, with customized data conversions, lengthy padding, and specialized encoding characters. Ooga Booga.")