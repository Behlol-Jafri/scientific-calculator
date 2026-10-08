import streamlit as st
import math

st.markdown("""
<style>
div[data-testid="stTextInput"] input {
    text-align: right;
    font-size: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
h2 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

if "number" not in st.session_state:
    st.session_state.number = ""

if "result" not in st.session_state:
    st.session_state.result = ""

if "invert" not in st.session_state:
    st.session_state.invert = True

if "mode" not in st.session_state:
    st.session_state.mode = "Deg"

def main():
    if "+" in st.session_state.number:
        n = st.session_state.number.split("+")
        sum = 0
        for i in n:
            sum += float(i)
        st.session_state.result = str(sum)
        st.session_state.number = str(sum)

    elif "-" in st.session_state.number:
        n = st.session_state.number.split("-")
        sub = float(n[0])
        for i in n[1:]:
            sub -= float(i)
        st.session_state.result = str(sub)
        st.session_state.number = str(sub)

    elif "x" in st.session_state.number:
        n = st.session_state.number.split("x")
        multi = 1
        for i in n:
            multi *= float(i)
        st.session_state.result = str(multi)
        st.session_state.number = str(multi)

    elif "/" in st.session_state.number:
        n = st.session_state.number.split("/")
        divid = float(n[0])
        for i in n[1:]:
            divid /= float(i)
        st.session_state.result = str(divid)
        st.session_state.number = str(divid)

    elif "%" in st.session_state.number:
        n = st.session_state.number.split("%")
        mod = float(n[0])
        for i in n[1:]:
            mod %= float(i)
        st.session_state.result = str(mod)
        st.session_state.number = str(mod)

    elif "log( " in st.session_state.number:
        n = st.session_state.number.split()
        num = 0
        for i in n:
            if i.isdigit():
                num = int(i)
        log_num = math.log10(num) 
        st.session_state.result = str(log_num)
        st.session_state.number = str(log_num)

    elif "10^" in st.session_state.number:
        n = st.session_state.number.split("^")
        num = int(n[-1])
        num_10ˣ = math.pow(10,num) 
        st.session_state.result = str(num_10ˣ)
        st.session_state.number = str(num_10ˣ)

    elif "ln( " in st.session_state.number:
        n = st.session_state.number.split()
        num = 0
        for i in n:
            if i.isdigit():
                num = int(i)
        ln_num = math.log(num) 
        st.session_state.result = str(ln_num)
        st.session_state.number = str(ln_num)

    elif "e^" in st.session_state.number:
        n = st.session_state.number.split("^")
        num = int(n[-1])
        num_eˣ = math.exp(num) 
        st.session_state.result = str(num_eˣ)
        st.session_state.number = str(num_eˣ)

    elif "^2" in st.session_state.number:
        n = st.session_state.number.split("^")
        num = int(n[0])
        num_x = math.pow(num,2) 
        st.session_state.result = str(num_x)
        st.session_state.number = str(num_x)

    elif "^" in st.session_state.number:
        n = st.session_state.number.split("^")
        num1 = int(n[0])
        num2 = int(n[-1])
        num_x = math.pow(num1,num2) 
        st.session_state.result = str(num_x)
        st.session_state.number = str(num_x)

    elif "E" in st.session_state.number:
        n = st.session_state.number.split("E")
        num1 = int(str(n[0]))
        num2 = int(str(n[1]))
        num_x = num1 * 10 ** num2
        st.session_state.result = str(num_x)
        st.session_state.number = str(num_x)

    elif "e" in st.session_state.number:
        n = st.session_state.number.split("e")
        if n:
            num1 = n[0] if not n[0] == '' else 1
            num2 = n[1] if not n[1] == '' else 1
            num = int(str(num1)) * int(str(num2))
            num_x = math.e * num
        else:
            num_x = math.e 
        st.session_state.result = str(num_x)
        st.session_state.number = str(num_x)

    elif "√( " in st.session_state.number:
        n = st.session_state.number.split()
        num = 0
        for i in n:
            if i.isdigit():
                num = int(i)
        sqrt_num = math.sqrt(num) 
        st.session_state.result = str(sqrt_num)
        st.session_state.number = str(sqrt_num)

    elif "sin( " in st.session_state.number:
        n = st.session_state.number.split()
        num = 0
        for i in n:
            if i.isdigit():
                    num = int(i)
        if st.session_state.mode == "Deg":
            sin_num = math.sin(math.radians(num)) 
        else:
            sin_num = math.sin(num) 
        st.session_state.result = str(sin_num)
        st.session_state.number = str(sin_num)

    elif "sin⁻¹( " in st.session_state.number:
        n = st.session_state.number.split()
        n.remove("sin⁻¹(")
        num = 0
        for i in n:
            num = float(i)
        if num > 1:
            arcsin_num = "Error"
        elif st.session_state.mode == "Deg":
            arcsin_num = math.degrees(math.asin(num))
        else:
            arcsin_num = math.asin(num) 
        st.session_state.result = str(arcsin_num)
        st.session_state.number = str(arcsin_num)

    elif "cos( " in st.session_state.number:
        n = st.session_state.number.split()
        num = 0
        for i in n:
            if i.isdigit():
                num = int(i)
        if st.session_state.mode == "Deg":
            cos_num = math.cos(math.radians(num)) 
        else:
            cos_num = math.cos(num) 
        st.session_state.result = str(cos_num)
        st.session_state.number = str(cos_num)

    elif "cos⁻¹( " in st.session_state.number:
        n = st.session_state.number.split()
        n.remove("cos⁻¹(")
        num = 0
        for i in n:
            num = float(i)
        if num > 1.0:
            arccos_num = "Error"
        elif st.session_state.mode == "Deg":
            arccos_num = math.degrees(math.acos(num))
        else:
            arccos_num = math.acos(num) 
        st.session_state.result = str(arccos_num)
        st.session_state.number = str(arccos_num)

    elif "tan( " in st.session_state.number:
        n = st.session_state.number.split()
        num = 0
        for i in n:
            if i.isdigit():
                num = int(i)
        if st.session_state.mode == "Deg":
            tan_num = math.tan(math.radians(num)) 
        else:
            tan_num = math.tan(num) 
        st.session_state.result = str(tan_num)
        st.session_state.number = str(tan_num)

    elif "tan⁻¹( " in st.session_state.number:
        n = st.session_state.number.split()
        n.remove("tan⁻¹(")
        num = 0
        for i in n:
            num = float(i)
        if st.session_state.mode == "Deg":
            arctan_num = math.degrees(math.atan(num))
        else:
            arctan_num = math.atan(num) 
        st.session_state.result = str(arctan_num)
        st.session_state.number = str(arctan_num)

    elif " !" in st.session_state.number:
        n = st.session_state.number.split()
        n.remove("!")
        num = 0
        for i in n:
            num = int(i)
        factorial = math.factorial(num)
        st.session_state.result = str(factorial)
        st.session_state.number = str(factorial)

    elif " π " in st.session_state.number:
        n = st.session_state.number.split()
        n.remove("π")
        num = 1
        for i in n:
            num = int(i)
        pi = math.pi * num
        st.session_state.result = str(pi)
        st.session_state.number = str(pi)

    elif "Ans" in st.session_state.number:
        st.session_state.number = st.session_state.result


st.header("Scientific Calculator")

st.text_input("", value=st.session_state.number,)


numbers = [
    ["Rad" if st.session_state.mode == "Deg" else "Deg","x!", " ( ", " ) ", " % ",  "Del", "AC"],
    ["Inv", "sin" if st.session_state.invert else "sin⁻¹", "ln" if st.session_state.invert else "eˣ", "7", "8", "9", " / "],
    ["π", "cos" if st.session_state.invert else "cos⁻¹", "log" if st.session_state.invert else "10ˣ", "4", "5", "6", " x "],
    ["e","tan" if st.session_state.invert else "tan⁻¹", "√" if st.session_state.invert else "x²", "1", "2", "3", " - "],
    ["Ans", "EXP", "xʸ", "0", ".", "=", " + "],
]

for row in numbers:

    columns = st.columns(7)

    for i, button in enumerate(row):

        with columns[i]:

            if st.button(button, use_container_width=True,):

                if button == "AC":
                    st.session_state.number = ""
                elif button == "Del":
                    st.session_state.number = st.session_state.number[:-1]
                elif button == "x!":
                    st.session_state.number += " !"
                elif button == "π":
                    st.session_state.number += " π "
                elif button == "log":
                    st.session_state.number += "log( "
                elif button == "10ˣ":
                    st.session_state.number += "10^"
                elif button == "ln":
                    st.session_state.number += "ln( "
                elif button == "eˣ":
                    st.session_state.number += "e^"
                elif button == "x²":
                    st.session_state.number += "^2"
                elif button == "EXP":
                    st.session_state.number += "E"
                elif button == "e":
                    st.session_state.number += "e"
                elif button == "xʸ":
                    st.session_state.number += "^"
                elif button == "√":
                    st.session_state.number += "√( "
                elif button == "Ans":
                    st.session_state.number += "Ans"
                elif button == "sin":
                    st.session_state.number += "sin( "
                elif button == "sin⁻¹":
                    st.session_state.number += "sin⁻¹( "
                elif button == "cos":
                    st.session_state.number += "cos( "
                elif button == "cos⁻¹":
                    st.session_state.number += "cos⁻¹( "
                elif button == "tan":
                    st.session_state.number += "tan( "
                elif button == "tan⁻¹":
                    st.session_state.number += "tan⁻¹( "
                elif button == "Deg":
                    st.session_state.mode = "Deg"
                elif button == "Rad":
                    st.session_state.mode = "Rad"
                elif button == "Inv":
                    st.session_state.invert = not st.session_state.invert
                elif button == "=":
                    main()
                    
                else:
                    st.session_state.number += button

                st.rerun()


