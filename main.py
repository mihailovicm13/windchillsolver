from sympy import Symbol, Derivative

print("Hello! Let's solve for the change in Wind Chill.")
prompt = input("Do we know the change in temperature (T), "
               "or wind speed (v)? ").lower()

if prompt == "t":
    delta_T = int(input("Input the change in temperature (AT): "))

elif prompt == "v":
    delta_v = int(input("Input the change in wind speed (Av): "))

else:
    print("Invalid input")
    raise SystemExit(0)

T_input = int(input("Input the temperature value in Celsius (T): "))
v_input = int(input("Input the wind speed in km/h (v): "))

T = Symbol('T')
v = Symbol('v')

wind_chill = 13.12 + 0.6215 * T - 11.37 * v ** 0.16 + 0.3965 * T * v ** 0.16

if prompt == "t":
    deriv_arg, delta_val = T, delta_T
elif prompt == "v":
    deriv_arg, delta_val = v, delta_v

partial_deriv = Derivative(wind_chill, deriv_arg)
delta_W = partial_deriv.doit() * delta_val
answer = delta_W.subs(v, v_input)
answer = abs(answer.subs(T, T_input))
answer_rounded = round(answer, 2)
print(answer_rounded)

