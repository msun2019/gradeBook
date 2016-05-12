grades = [[100, 97, 98, 93, 91],
		 [   0,  0, 50, 79, 60],
		 [  85, 89, 92, 79, 80]]
		 
		 
def average_rows(grid, targetRow):
	rowCounter = -1 
	answer = 0 
	for row in grid:
		itemCounter = 0.0
		rowCounter += 1 
		if rowCounter == targetRow:
			for item in row:
				itemCounter += 1 
				answer += item
			
			return answer / itemCounter 
def average_all(grid):
	answer = 0
	itemCounter = 0.0 
	for row in grid:
		for item in row: 
			itemCounter += 1 
			answer += item
	return answer / itemCounter 
print("The average of all the grades are: {}".format(average_all(grades)))
print("The average of the grades in the first row are: {}".format(average_rows(grades, 0)))
print("The average of the grades in the first row are: {}".format(average_rows(grades, 1)))
print("The average of the grades in the first row are: {}".format(average_rows(grades, 2)))