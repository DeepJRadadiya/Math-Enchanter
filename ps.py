import Package.curvsFitting as curvsFitting
import Package.BasicStatistics as statistics
import Package.Correlation as correlation

def psSolver():
    print('1. curv fitting\n2. Basic Statistics\n3. Correlation and Regression\n0. exit')
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
        elif choice == 0:
            exit
        else:
            print('somthing wrong')
    except ValueError as e:
        print(f"Input Error: {e}")
        return None, None

if __name__ == "__main__":
    psSolver()