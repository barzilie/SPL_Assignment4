#from numpy import product
from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            product = repo.products.find(id=splittedline[0])[0]
            current_quantity = product.quantity
            required_quantity = int(splittedline[1]) 
            if((required_quantity<0 and current_quantity>=required_quantity) or required_quantity > 0):
                repo.products.delete(id=splittedline[0])
                repo.products.insert(Product(product.id, product.description, product.price, current_quantity+required_quantity))
                repo.activities.insert(Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3]))
            # elif(required_quantity>0):
            #     repo.products.delete(id=splittedline[0])
            #     repo.products.insert(Product(product.id, product.description, product.price, current_quantity+required_quantity))
            #     repo.activities.insert(Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3]))

if __name__ == '__main__':
    main(sys.argv)