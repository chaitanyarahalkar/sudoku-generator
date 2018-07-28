import random
import itertools

row1,row2,row3,row4,row5,row6,row7,row8,row9=[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]
numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0,9) :
	row1[i] = random.choice(numbers)
	numbers.remove(row1[i])

numbers = [1,2,3,4,5,6,7,8,9]
a = {row1[0] , row1[1] , row1[2] }
b = {row1[3] , row1[4] , row1[5] }
c = {row1[6] , row1[7] , row1[8] }

while(0 in row2) :
	numbers = [3,4,5,6,7,8]
	for number in a :
		i = random.choice(numbers)	
		if(row2[i] ==0) :
			row2[i] = number
			numbers.remove(i)
		else : 
			i = random.choice(numbers)
			row2[i] = number
			numbers.remove(i)
	
	numbers = [0,1,2,6,7,8]
	for number in b:
		i = random.choice(numbers)	
		if(row2[i] ==0) :
			row2[i] = number
			numbers.remove(i)
		else : 
			i = random.choice(numbers)
			row2[i] = number
			numbers.remove(i)
			
	numbers = [0,1,2,3,4,5]
	for number in c:
		i = random.choice(numbers)	
		if(row2[i] ==0) :
			row2[i] = number
			numbers.remove(i)
		else : 
			i = random.choice(numbers)
			row2[i] = number
			numbers.remove(i)
			
	if(0 in row2) : row2 = [0,0,0,0,0,0,0,0,0]

def thirdrow() : 
	for j in [0,3,6] :
		numbers = [1,2,3,4,5,6,7,8,9]
		numbers.remove(row1[j])
		numbers.remove(row1[j+1])
		numbers.remove(row1[j+2])
		numbers.remove(row2[j])
		numbers.remove(row2[j+1])
		numbers.remove(row2[j+2])
		place = [j,j+1,j+2]
		for number in numbers :
			i = random.choice(place)
			if(row3[i] ==0) :
				row3[i] = number
				place.remove(i)
			else : 
				i = random.choice(place)
				row3[i] = number
				place.remove(i)
	return row3

row3 = thirdrow()

def rows_4789(rowno , row) :
	while(0 in row):
		for i in range(0,9) :
			numbers = [1,2,3,4,5,6,7,8,9]
			numbers.remove(row1[i])
			numbers.remove(row2[i])
			numbers.remove(row3[i])
			if(rowno>4) :
				numbers.remove(row4[i])
				numbers.remove(row5[i])
				numbers.remove(row6[i])
				if(rowno>7) :
					numbers.remove(row7[i])
				if(rowno==9) :
					numbers.remove(row8[i])
			j=i
			while(j>0) :
				j=j-1
				if(row[j] in numbers) : numbers.remove(row[j])
			if(len(numbers) != 0) : row[i] = random.choice(numbers)
		if(0 in row) : row = [0,0,0,0,0,0,0,0,0]
	return row

row4 = rows_4789(4,row4)

def fifthrow(row5) :
	while(0 in row5) :
		for i in range(0,9) :
			numbers = [1,2,3,4,5,6,7,8,9]
			numbers.remove(row1[i])
			numbers.remove(row2[i])
			numbers.remove(row3[i])
			if(i<=2) : 
				for k in range(0,3) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
			if(i<=5 and i>2) : 
				for k in range(3,6) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
			if(i>5) : 
				for k in range(6,9) :
					if(row4[k] in numbers) : numbers.remove(row4[k])
			k=0
			while(k<=i) :
				if(row5[k] in numbers) : numbers.remove(row5[k])
				k=k+1
			if(len(numbers)!=0) : row5[i] = random.choice(numbers)
			else :
				row5 = [0,0,0,0,0,0,0,0,0]
				break
		numbers = {1,2,3,4,5,6,7,8,9}
		for i in [0,3,6] :
			block = {row4[i] , row4[i+1] , row4[i+2] , row5[i] ,row5[i+1],row5[i+2]}
			valid = numbers - block
			for j in range(i,i+3) :
					col = {row1[j] , row2[j] , row3[j]}	
					if( len( list( valid - (col & valid)) )  == 0) : 
						row5 = [0,0,0,0,0,0,0,0,0]
						break
	return row5

row5 = fifthrow(row5)

def sixthrow(row6) :
	numbers = {1,2,3,4,5,6,7,8,9}
	for i in [0,3,6] :
		block = {row4[i] , row4[i+1] , row4[i+2] , row5[i] ,row5[i+1],row5[i+2]}
		valid = numbers - block
		j=i
		while(j<i+3) :			
			col = {row1[j] , row2[j] , row3[j]}	
			choose = list(valid - (col & valid))
			if(not (col & valid) and j!=i+2) :
				if(j==i):row6[j] = 0
				if(j==i+1):row6[j]=0
			else:
				if(len(choose)>0) :
					k=i
					while(k<j) :
						if(row6[k] in choose) : choose.remove(row6[k])
						k=k+1
				if(len(choose)==0) : 
					row6[i]=0
					row6[i+1]=0
					row6[i+2]=0
					j=i-1
				else:
					chosen = random.choice(choose)
					k=0
					while(chosen in row6) :
						k=k+1
						if(k==10): break
						chosen = random.choice(choose)
					row6[j] = chosen 
			j=j+1
			
		if(row6[i]==0) :
			block = {row4[i] , row4[i+1] , row4[i+2] , row5[i] ,row5[i+1],row5[i+2] , row6[i+1],row6[i+2] }		
			valid = list(numbers - block)		
			row6[i] = valid[0]
		if(row6[i+1]==0) :
			block = {row4[i] , row4[i+1] , row4[i+2] , row5[i] ,row5[i+1],row5[i+2] , row6[i],row6[i+2] }		
			valid = list(numbers - block)	
			row6[i+1] = valid[0]
		block.clear()
		valid.clear()
		col.clear()
	return row6

row6 = sixthrow(row6)
row7 = rows_4789(7,row7)
row8 = rows_4789(8,row8)
row9 = rows_4789(9,row9)

get_all = list()


for num in itertools.chain(row1,row2,row3,row4,row5,row6,row7,row8,row9):
	get_all.append(num)


for pos in random.sample(range(0,81),36):
	get_all[pos] = ' '

s = '''


		                   __      __        
   _______  ______/ /___  / /____  __
  / ___/ / / / __  / __ \/ //_/ / / /
 (__  ) /_/ / /_/ / /_/ / ,< / /_/ / 
/____/\__,_/\__,_/\____/_/|_|\__,_/  
                                   
                                                                
		-------------------------
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		-------------------------
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		-------------------------
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		-------------------------


	'''.format(*get_all)

print(s)