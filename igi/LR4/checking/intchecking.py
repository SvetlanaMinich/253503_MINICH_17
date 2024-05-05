def IntChecking(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
    except:
        return False
