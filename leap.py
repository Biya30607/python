from datetime import date
current_year=date.today().year
final_year=int(input("Enter the final year:"))
print(f"\nLeap years from {current_year} to {final_year}:")
for year in range(current_year,final_year+1):
    if(year%4==0 and year % 100!=0)or(year % 400 == 0):
        print (year)
