x="global"

def outer():
    x="outer local"

    def inner():
        nonlocal x
        x="inner local"
        print("inner:",x)

    inner()
    print("outer:",x)

outer()
print("Global:",x)