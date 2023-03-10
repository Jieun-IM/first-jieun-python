def function(**kwargs):
    for k, v in kwargs.items():    
        print(k, v)

if __name__ == "__main__":
    function(n1=1, n2=2, n3=3)
