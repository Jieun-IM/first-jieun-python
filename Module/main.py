import calcpkg.operation
import calcpkg.geometry

def main():
    print(calcpkg.operation.add(10, 20))
    print(calcpkg.operation.mul(10, 20))
    
    print(calcpkg.geometry.triangle_area(30, 40))
    print(calcpkg.geometry.rectangle_area(30, 40))
    
if __name__ == '__main__':
    main()