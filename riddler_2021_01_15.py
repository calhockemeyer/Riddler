import itertools as it

# find the possible combinations of single digit numbers which combine to make row products
def get_multiples(product):
    x = 1
    y = 1
    z = 1
    mult_list = []
    for x in range(0, 10):
        for y in range(0, 10):
            for z in range(0, 10):
                if x*y*z == product:
                    mult_list.append((x,y,z))

    return mult_list

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

def get_combs(row_prod):
    row_prods = sorted(row_prod)
    combinations = it.product(*(row_prod[prod] for prod in row_prods))

    return combinations

def get_cols(combinations, col_prod):

    col_prods = sorted(col_prod)
    for comb in combinations:
        col_1_list = []
        col_2_list = []
        col_3_list = []
        for mult_list in comb:
            col_1_list.append(mult_list[0])
            col_2_list.append(mult_list[1])
            col_3_list.append(mult_list[2])
        col_1_prod = multiplyList(col_1_list)
        col_2_prod = multiplyList(col_2_list)
        col_3_prod = multiplyList(col_3_list)
        if col_1_prod == col_prods[0] and col_2_prod == col_prods[1] and col_3_prod == col_prods[2]:
            col_prod[col_prods[0]].append(col_1_list)
            col_prod[col_prods[1]].append(col_2_list)
            col_prod[col_prods[2]].append(col_3_list)
            
            print("Found solution :)")
            return col_prod, comb

    print("Did not find the solution :(")
    return col_prod, []

def Summary(correct_comb, row_prod, col_prod):
    if correct_comb == []:
        print("Sorry, I didn't find the solution.")
    else:
        row_index = 0
        print(f"Column products are assumed to be in this order: {sorted(col_prod)}")
        for row in sorted(row_prod):
            print(f"The correct values for the row with product {row} are: {correct_comb[row_index]}")
            row_index += 1
        



# make lists for row and column products
row_prod = {40: [], 84: [], 98: [], 112: [], 135: [], 216: [], 245: [], 294: []}
col_prod = {55566: [], 156800: [], 8890560: []}

# get list of possible combinations for row products
for product in row_prod.keys():
    row_prod[product] = get_multiples(product)

combinations = get_combs(row_prod)
col_prod, correct_comb = get_cols(list(combinations), col_prod)
Summary(correct_comb, row_prod, col_prod)
