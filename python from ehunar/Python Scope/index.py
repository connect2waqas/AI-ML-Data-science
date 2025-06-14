phone = "iphone_10_onroad_globle_scope"

def parents_Home():
    phone = "iphone_onparentHome" 
    # parent scope nonlocal
    def myHome():
        # local scope
        nonlocal phone
        # phone = "iphone_10_onmyHome"
        return phone
    return myHome()
   
print(parents_Home())
