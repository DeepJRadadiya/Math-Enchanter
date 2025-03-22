import Package.curvsFitting as curvsFitting
import Package.BasicStatistics as statistics
import Package.Correlation as correlation
import Package.Matrix as matrixs
import Package.CoordinateGeometry as corrdinate
def psSolver():
    while True:
        print("\n")
        print('1. curv fitting\n2. Basic Statistics\n3. Correlation and Regression\n4. Matrix\n5. Coordinate Geometry\n0. exit')
        try:
            choice = int(input('enter the choice:'))
        
            if choice == 1:
                try:
                    print('\n')
                    curvsFitting.fit_curve()

                except NameError:
                    Error: NameError 
            elif choice == 2:
                try:
                    print('\n')
                    statistics.statistics_menu()
                except NameError:
                    Error: NameError 
            elif choice == 3:
                try:
                    print('\n')
                    correlation.correlation_regression_menu()
                except NameError:
                    Error: NameError 
            elif choice == 4:
                try:
                    print("\n")
                    matrixs.matrix()
                except NameError:
                    Error: NameError
            elif choice == 5:
                try:
                    print("\n")
                    corrdinate.main()
                except NameError:
                    Error: NameError
            elif choice == 0:
                print("bye....")
                break
            else:
                print('somthing wrong')
        except ValueError as e:
            print(f"Input Error: {e}")
            return None, None

if __name__ == "__main__":
    psSolver()